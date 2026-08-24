


from fastapi import FastAPI, Query, Depends
from sqlalchemy.orm import Session
from db import SessionLocal
from models import Product
from schemas import ProductOut
from nlp.parser import extract_price_limit
from nlp.preprocessor import extract_dynamic_entities
from nlp.ranker import rank_products
from seed import seed_products

app = FastAPI(title="NLP Product Search Engine API")

def get_db():  #har request ke liye naya db banata ha ,requeest khatam hote hi session band kar deta ha 
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/search", response_model=list[ProductOut])
def search_products(q: str = Query(...), db: Session = Depends(get_db)):
    #  Auto-seed if table empty
    if db.query(Product).count() == 0:
        seed_products(db)

    max_price = extract_price_limit(q)
    entities = extract_dynamic_entities(q)
    if max_price:
        entities["max_price"] = max_price

    query = db.query(Product)
    if max_price:
        query = query.filter(Product.price <= max_price)

    raw_products = [p.__dict__ for p in query.all()]
    ranked = rank_products(user_query=q, products=raw_products)

    return ranked[:3]

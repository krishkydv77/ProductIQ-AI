import random
import numpy as np
from sqlalchemy.orm import Session
from models import Product

categories = ['shoes', 'jacket', 'shirt', 'pants', 't-shirt','watch','shirt','top','belt','lipstik','mobile']
colors = ['black', 'brown', 'white', 'red', 'blue']
styles = ['formal', 'sports', 'casual']

def seed_products(db: Session, n: int = 50):
    prices = np.random.randint(999, 5000, size=n)
    products = []
    for i in range(n):
        cat, col, sty = random.choice(categories), random.choice(colors), random.choice(styles)
        products.append(Product(
            id=f"P{101+i}",
            name=f"{col.title()} {sty.title()} {cat.title()}",
            description=f"Comfortable {col} {sty} {cat} perfect for daily wear.",
            price=int(prices[i]),
            category=cat,
            color=col,
            style=sty
        ))
    db.add_all(products) # sabi products ko session me ada karega
    db.commit()

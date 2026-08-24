
from pydantic import BaseModel

class ProductBase(BaseModel):
    id: str
    name: str
    description: str
    price: int
    category: str
    color: str
    style: str

class ProductOut(ProductBase):
    match_score: float | None = None

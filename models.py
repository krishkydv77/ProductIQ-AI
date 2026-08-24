
from sqlalchemy import Column, String, Integer, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = "products"

    id = Column(String(10), primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    price = Column(Integer, nullable=False)
    category = Column(String(50), nullable=True)
    color = Column(String(20), nullable=True)
    style = Column(String(20), nullable=True)

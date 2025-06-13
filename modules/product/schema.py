from pydantic import BaseModel, Field
from typing import Optional


class Product(BaseModel):
    id: int
    name: str
    price: float
    quantity: int


class CreateProductRequest(BaseModel):
    name: str = Field(min_length=5)
    price: float = Field(gt=0)
    quantity: int = Field(ge=0)


class UpdateProductRequest(BaseModel):
    name: Optional[str] = Field(default=None, min_length=5)
    price: Optional[float] = Field(default=None, gt=0)
    quantity: Optional[int] = Field(default=None, ge=0)

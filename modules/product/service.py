from sqlmodel import Session, select
from fastapi import HTTPException

from .model import Product
from .schema import CreateProductRequest, UpdateProductRequest


class ProductService:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self):
        return self.session.exec(select(Product)).all()

    def get_by_id(self, id: int):
        product = self.session.get(Product, id)
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        return product

    def create(self, data: CreateProductRequest):
        product = Product(**data.model_dump())
        self.session.add(product)
        self.session.commit()
        self.session.refresh(product)
        return product

    def update(self, id: int, data: UpdateProductRequest):
        product = self.session.get(Product, id)
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")

        update_data = data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(product, key, value)

        self.session.add(product)
        self.session.commit()
        self.session.refresh(product)
        return product

    def delete(self, id: int):
        product = self.session.get(Product, id)
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        self.session.delete(product)
        self.session.commit()
        return True

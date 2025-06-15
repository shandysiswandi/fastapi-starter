from fastapi import APIRouter, Depends, Path
from sqlmodel import Session
from typing import Annotated

from modules.database import get_session
from .service import ProductService
from .schema import CreateProductRequest, UpdateProductRequest

ProductRouter = APIRouter(tags=["Products"], prefix="/products")


def get_service(session: Session = Depends(get_session)) -> ProductService:
    return ProductService(session)


@ProductRouter.get("/")
async def list(service: ProductService = Depends(get_service)):
    return service.get_all()


@ProductRouter.get("/{id}")
async def get(
    id: Annotated[int, Path()],
    service: ProductService = Depends(get_service),
):
    return service.get_by_id(id)


@ProductRouter.post("/")
async def create(
    data: CreateProductRequest,
    service: ProductService = Depends(get_service),
):
    return service.create(data)


@ProductRouter.put("/{id}")
async def update(
    id: Annotated[int, Path()],
    data: UpdateProductRequest,
    service: ProductService = Depends(get_service),
):
    return service.update(id, data)


@ProductRouter.delete("/{id}")
async def delete(
    id: Annotated[int, Path()],
    service: ProductService = Depends(get_service),
):
    ok = service.delete(id)

    return {"success": ok}

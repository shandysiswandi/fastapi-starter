from fastapi import APIRouter, Depends
from sqlmodel import Session

from modules.database import get_session
from .service import ProductService
from .schema import CreateProductRequest, UpdateProductRequest

ProductRouter = APIRouter(tags=["Products"], prefix="/products")


def get_service(session: Session = Depends(get_session)) -> ProductService:
    return ProductService(session)


@ProductRouter.get("/")
async def list(service: ProductService = Depends(get_service)):
    return service.get_all()


@ProductRouter.get("/<int:id>")
async def get(id: int, service: ProductService = Depends(get_service)):
    return service.get_by_id(id)


@ProductRouter.post("/")
async def create(
    data: CreateProductRequest,
    service: ProductService = Depends(get_service),
):
    return service.create(data)


@ProductRouter.put("/<int:id>")
async def update(
    id: int,
    data: UpdateProductRequest,
    service: ProductService = Depends(get_service),
):
    return service.update(id, data)


@ProductRouter.delete("/<int:id>")
async def delete(id: int, service: ProductService = Depends(get_service)):
    return service.delete(id)

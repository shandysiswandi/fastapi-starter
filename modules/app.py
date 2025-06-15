from fastapi import APIRouter
from modules.base.handler import BaseRouter
from modules.product.handler import ProductRouter


class ApplicationModule:
    def router(self) -> APIRouter:
        router = APIRouter()

        router.include_router(BaseRouter)
        router.include_router(ProductRouter)

        return router

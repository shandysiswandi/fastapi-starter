from fastapi import APIRouter

BaseRouter = APIRouter(tags=["Base"])


@BaseRouter.get("/")
async def home():
    return {"message": "Welcome to FastAPI with Clean Architecture!"}


@BaseRouter.get("/health")
async def health():
    return {"status": "healthy"}

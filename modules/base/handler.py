from fastapi import APIRouter

BaseRouter = APIRouter(tags=["Base"])


@BaseRouter.get(
    path="/",
    summary="Home Route",
    description="Returns a welcome message for the FastAPI application.",
    response_description="A simple welcome message.",
)
async def home():
    """Handle the root path and return a welcome message."""
    return {"message": "Welcome to FastAPI with Clean Architecture!"}


@BaseRouter.get(
    path="/health",
    summary="Health Check",
    description="Checks the health status of the application.",
    response_description="A health status indicator.",
)
async def health():
    """Health check endpoint to verify the service is running."""
    return {"message": "healthy"}

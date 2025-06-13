from fastapi import APIRouter

from modules.auth.handler import AuthRouter
from modules.base.handler import BaseRouter


class Application:
    """Main application class for setting up application."""

    def router(self) -> APIRouter:  # noqa: PLR6301
        """Configure and return the main API router."""
        router = APIRouter()

        router.include_router(BaseRouter)
        router.include_router(AuthRouter)

        return router

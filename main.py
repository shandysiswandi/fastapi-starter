import os
from contextlib import asynccontextmanager

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware

from modules.app import Application
from modules.database import create_db_and_tables

load_dotenv()


@asynccontextmanager  # type: ignore
async def lifespan(app: FastAPI):  # noqa: RUF029
    """Lifespan context manager for FastAPI startup and shutdown events.

    Initializes the database schema before the application starts.
    """
    create_db_and_tables()

    yield


app = FastAPI(
    debug=os.getenv("APP_DEBUG", "false").lower() == "true",
    title="Clean Architecture FastAPI Application",
    summary="A scalable and maintainable FastAPI backend following Clean Architecture principles.",
    description="""
    This API serves as a backend foundation built using FastAPI and Clean Architecture principles.

    ## Overview

    - Modular and maintainable structure
    - Designed for scalability
    - Ideal for production-grade applications

    ## Features

    - Health checks
    - Future extensibility

    ---
    """,
    version="0.1.0",
    terms_of_service="https://example.com/terms/",
    contact={
        "name": "SHANDY SISWANDI",
        "url": "https://shandysiswandi.com",
        "email": "shandysiswandi@mail.com",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    },
    swagger_ui_oauth2_redirect_url=None,
    redoc_url=None,
    lifespan=lifespan,
)
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(GZipMiddleware, compresslevel=5)

app_module = Application()
app.include_router(app_module.router())

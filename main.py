import os
from dotenv import load_dotenv
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware

from modules.app import ApplicationModule
from modules.database import create_db_and_tables

load_dotenv()


@asynccontextmanager  # type: ignore
async def lifespan(app: FastAPI):
    create_db_and_tables()

    yield


app = FastAPI(
    debug=os.getenv("APP_DEBUG", "false").lower() == "true",
    title="Clean Architecture FastAPI App",
    summary="Deadpond's favorite app. Nuff said.",
    description="""
    Clean Architecture API helps you do awesome stuff. 🚀

    ## Products

    You can **read more**.
    """,
    version="0.1.0",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Shandy Siswandi",
        "url": "https://shandysiswandi.com",
        "email": "shandysiswandi@mail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
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

app_module = ApplicationModule()
app.include_router(app_module.router())

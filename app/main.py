import uvicorn

from fastapi import FastAPI
from app.api.api_v1.router import api_router
from starlette.middleware.cors import CORSMiddleware
from app.core.config import settings

app = FastAPI()

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix=settings.API_V1_STR)


def start():
    uvicorn.run("app.main:app", host="localhost", port=8000, reload=True)

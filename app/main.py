from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.core.database import connect_database
from app.api.router import api_router
from app.core.config import settings
from app.middleware.logging import LoggingMiddleware


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

app.add_middleware(LoggingMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        settings.FRONTEND_URL
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@asynccontextmanager
async def lifespan(app: FastAPI):

    connect_database()
    print("🚀 Application Started")

    yield

    print("👋 Application Shutdown")


app = FastAPI(
    title="Rubel Mart API",
    version="1.0.0",
    lifespan=lifespan
)


@app.get("/")
async def root():
    return {
        "message": "FastAPI server is up and running...", 
        "success": True, 
        "status_code": 200,
        "data": {}
    }

@app.get("/health")
async def health():
    return {
        "message": "Healthy",
        "success": True,
        "status_code": 200,
        "data": {}
    }


app.include_router(api_router)



 
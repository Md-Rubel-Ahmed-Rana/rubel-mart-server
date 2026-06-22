from contextlib import asynccontextmanager

from app.core.database import (
    connect_database
)


@asynccontextmanager
async def lifespan(app):

    connect_database()

    print("🚀 Application Started")

    yield

    print("👋 Application Shutdown")
from sqlalchemy import create_engine, text
from sqlalchemy.orm import (
    sessionmaker,
    DeclarativeBase
)

from app.core.config import settings


class Base(DeclarativeBase):
    pass


engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


def connect_database():

    try:

        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        print("✅ PostgreSQL Connected")

    except Exception as error:

        print("❌ PostgreSQL Connection Failed")

        raise error
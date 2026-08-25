from app.core.database import Base
from datetime import datetime
import uuid
from sqlalchemy.orm import (
    Mapped,
    mapped_column
)
from sqlalchemy import (
    UUID,
    Boolean,
    Integer,
    String,
    DateTime,
    Text,
    func
)


class Brand(Base):
    __tablename__ = "brands"

    id: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)

    name: Mapped[str] = mapped_column(String(100), nullable=False)
    slug: Mapped[str] = mapped_column(String(120), nullable=False, unique=True)

    description: Mapped[str | None] = mapped_column(Text, nullable=True)

    logo: Mapped[str | None] = mapped_column(String, nullable=True)

    website: Mapped[str | None] = mapped_column(String, nullable=True)

    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    sort_order: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )
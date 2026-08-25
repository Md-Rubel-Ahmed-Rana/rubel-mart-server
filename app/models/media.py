from app.core.database import Base
from datetime import datetime
import uuid
from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from sqlalchemy import (
    String,
    DateTime
)

class Media(Base):

    __tablename__ = "media"

    id: Mapped[str] = mapped_column(
    String(32),
    primary_key=True,
    default=lambda: uuid.uuid4().hex,
    index=True
    )

    public_id: Mapped[str]

    url: Mapped[str]

    provider: Mapped[str | None]

    original_name: Mapped[str]

    mime_type: Mapped[str]

    uploaded_by: Mapped[str | None]

    size: Mapped[int]

    width: Mapped[int | None]

    height: Mapped[int | None]

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.timezone.utc.now
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.timezone.utc.now,
        onupdate=datetime.timezone.utc.now
    )
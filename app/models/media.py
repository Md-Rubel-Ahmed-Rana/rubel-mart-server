from app.core.database import Base
from datetime import datetime
import uuid
from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from sqlalchemy import (
    String,
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

    original_name: Mapped[str]

    mime_type: Mapped[str]

    size: Mapped[int]

    width: Mapped[int | None]

    height: Mapped[int | None]

    created_at: Mapped[datetime]
from app.core.database import Base
from datetime import datetime
import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from sqlalchemy import (
    DateTime,
    func
)

class Media(Base):

    __tablename__ = "media"

    id: Mapped[uuid.UUID] = mapped_column(
            UUID(as_uuid=True),
            primary_key=True,
            default=uuid.uuid4,
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
        default=func.now()
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=func.now(),
        onupdate=func.now()
    )
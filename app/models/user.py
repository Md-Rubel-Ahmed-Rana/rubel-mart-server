from datetime import datetime
from enum import Enum
import uuid


from sqlalchemy import (
    String,
    Boolean,
    DateTime,
    Enum as SQLEnum,
    ForeignKey
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from app.core.database import Base


class UserRole(str, Enum):
    ADMIN = "ADMIN"
    CUSTOMER = "CUSTOMER"


class UserStatus(str, Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    BLOCKED = "BLOCKED"


class User(Base):
    __tablename__ = "users"
    
    id: Mapped[str] = mapped_column(
    String(32),
    primary_key=True,
    default=lambda: uuid.uuid4().hex,
    index=True
    )

    first_name: Mapped[str] = mapped_column(
        String(100)
    )

    last_name: Mapped[str] = mapped_column(
        String(100)
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False
    )

    phone: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True
    )

    password: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    image_id: Mapped[str | None] = mapped_column(
            ForeignKey("media.id"),
            nullable=True
    )
    
    image = relationship(
        "Media",
        foreign_keys=[image_id]
    )

    role: Mapped[UserRole] = mapped_column(
        SQLEnum(UserRole),
        default=UserRole.CUSTOMER
    )

    status: Mapped[UserStatus] = mapped_column(
        SQLEnum(UserStatus),
        default=UserStatus.ACTIVE
    )

    is_verified: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.timezone.utc.now
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.timezone.utc.now,
        onupdate=datetime.timezone.utc.now
    )
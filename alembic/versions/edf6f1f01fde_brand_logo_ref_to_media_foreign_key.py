
"""Brand logo ref to Media foreign key

Revision ID: edf6f1f01fde
Revises: f36f90cc0fba
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "edf6f1f01fde"
down_revision: Union[str, Sequence[str], None] = "f36f90cc0fba"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Add a nullable reference to the media table.
    op.add_column(
        "brands",
        sa.Column("logo_id", sa.UUID(), nullable=True),
    )

    op.create_foreign_key(
        "fk_brands_logo_id_media",
        "brands",
        "media",
        ["logo_id"],
        ["id"],
        ondelete="RESTRICT",
    )

    # Keep the existing brands.logo column for now.
    # This preserves existing logo URLs.


def downgrade() -> None:
    op.drop_constraint(
        "fk_brands_logo_id_media",
        "brands",
        type_="foreignkey",
    )

    op.drop_column("brands", "logo_id")

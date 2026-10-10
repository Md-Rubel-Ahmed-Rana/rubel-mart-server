"""change user image to media foreign key

Revision ID: f36f90cc0fba
Revises: 761d34823db0
Create Date: 2026-10-11 01:32:07.933527

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f36f90cc0fba'
down_revision: Union[str, Sequence[str], None] = '761d34823db0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None



def upgrade() -> None:
    # Remove only the old category image column.
    # The previous migration added categories.image_id.
    op.drop_column("categories", "image")

    # Do not alter media.id or users.id.
    # Both existing IDs are VARCHAR(32).

    # Ensure the user image relationship uses VARCHAR(32).
    op.drop_constraint(
        "users_image_id_fkey",
        "users",
        type_="foreignkey",
    )

    op.create_foreign_key(
        "users_image_id_fkey",
        "users",
        "media",
        ["image_id"],
        ["id"],
        ondelete="RESTRICT",
    )


def downgrade() -> None:
    op.drop_constraint(
        "users_image_id_fkey",
        "users",
        type_="foreignkey",
    )

    op.create_foreign_key(
        "users_image_id_fkey",
        "users",
        "media",
        ["image_id"],
        ["id"],
    )

    op.add_column(
        "categories",
        sa.Column("image", sa.String(), nullable=True),
    )

"""rename table DoUp to doup_tasks

Revision ID: b458adf3741f
Revises: 421e970e1b56
Create Date: 2026-01-18 01:57:48.095821

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b458adf3741f'
down_revision: Union[str, None] = '421e970e1b56'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.rename_table("DoUp", "doup_tasks")


def downgrade() -> None:
    op.rename_table("doup_tasks", "DoUp")

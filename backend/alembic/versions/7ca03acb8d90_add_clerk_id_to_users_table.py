"""add clerk id to users table

Revision ID: 7ca03acb8d90
Revises: c81762a20381
Create Date: 2024-12-04 12:18:01.416289

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7ca03acb8d90'
down_revision: Union[str, None] = 'c81762a20381'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('users', sa.Column('clerk_id', sa.String(100), nullable=True))

def downgrade():
    op.drop_column('users', 'clerk_id')
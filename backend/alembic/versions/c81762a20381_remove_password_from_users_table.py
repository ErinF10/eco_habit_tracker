"""remove password from users table

Revision ID: c81762a20381
Revises: 2f6560739059
Create Date: 2024-12-04 10:44:06.366709

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c81762a20381'
down_revision: Union[str, None] = '2f6560739059'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.drop_column('users', 'password_hash')

def downgrade():
    op.add_column('users', sa.Column('password_hash', sa.String(20), nullable=False))
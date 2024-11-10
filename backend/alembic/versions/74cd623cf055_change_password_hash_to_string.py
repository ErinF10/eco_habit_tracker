"""change password_hash to string

Revision ID: 74cd623cf055
Revises: 95bfb81774da
Create Date: 2024-10-27 13:28:44.106984

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '74cd623cf055'
down_revision: Union[str, None] = '95bfb81774da'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Convert existing integer values to strings
    op.execute('ALTER TABLE users MODIFY COLUMN password_hash VARCHAR(255)')

def downgrade():
    # Convert back to integer (this may lose data if the strings are not valid integers)
    op.execute('ALTER TABLE users MODIFY COLUMN password_hash INTEGER')

"""Add autoincrement to user id

Revision ID: 278b08c95762
Revises: 90715ba09654
Create Date: 2024-12-04 13:54:27.919980

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '278b08c95762'
down_revision: Union[str, None] = '90715ba09654'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Temporarily drop foreign key constraints
    op.drop_constraint('fk_user_answers_user_id', 'user_answers', type_='foreignkey')
    op.drop_constraint('fk_user_habits_user_id', 'user_habits', type_='foreignkey')
    op.drop_constraint('fk_user_streaks_user_id', 'user_streaks', type_='foreignkey')

    # Modify the 'id' column to be auto-incrementing
    op.alter_column('users', 'id',
                    existing_type=sa.Integer(),
                    nullable=False,
                    autoincrement=True)
    
    # Recreate foreign key constraints
    op.create_foreign_key('fk_user_answers_user_id', 'user_answers', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key('fk_user_habits_user_id', 'user_habits', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key('fk_user_streaks_user_id', 'user_streaks', 'users', ['user_id'], ['id'], ondelete='CASCADE')


def downgrade():
    # Temporarily drop foreign key constraints
    op.drop_constraint('fk_user_answers_user_id', 'user_answers', type_='foreignkey')
    op.drop_constraint('fk_user_habits_user_id', 'user_habits', type_='foreignkey')
    op.drop_constraint('fk_user_streaks_user_id', 'user_streaks', type_='foreignkey')

    # Revert the 'id' column back to not auto-incrementing
    op.alter_column('users', 'id',
                    existing_type=sa.Integer(),
                    nullable=False,
                    autoincrement=False)
    
     # Recreate foreign key constraints
    op.create_foreign_key('fk_user_answers_user_id', 'user_answers', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key('fk_user_habits_user_id', 'user_habits', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key('fk_user_streaks_user_id', 'user_streaks', 'users', ['user_id'], ['id'], ondelete='CASCADE')

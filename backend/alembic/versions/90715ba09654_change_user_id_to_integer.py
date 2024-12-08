"""change user id to integer

Revision ID: 90715ba09654
Revises: 7ca03acb8d90
Create Date: 2024-12-04 13:36:11.829563

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '90715ba09654'
down_revision: Union[str, None] = '7ca03acb8d90'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
   # Temporarily drop foreign key constraints
    # op.drop_constraint('fk_user_answers_user_id', 'user_answers', type_='foreignkey')
    # op.drop_constraint('fk_user_habits_user_id', 'user_habits', type_='foreignkey')
    # op.drop_constraint('fk_user_streaks_user_id', 'user_streaks', type_='foreignkey')

    # Modify the users table
    op.alter_column('users', 'id',
               existing_type=sa.String(length=100),
               type_=sa.Integer(),
               existing_nullable=False)

    # Modify foreign key columns in related tables
    op.alter_column('user_answers', 'user_id',
               existing_type=sa.String(length=100),
               type_=sa.Integer(),
               existing_nullable=True)

    op.alter_column('user_habits', 'user_id',
               existing_type=sa.String(length=100),
               type_=sa.Integer(),
               existing_nullable=False)

    op.alter_column('user_streaks', 'user_id',
               existing_type=sa.String(length=100),
               type_=sa.Integer(),
               existing_nullable=False)

    # Recreate foreign key constraints
    op.create_foreign_key('fk_user_answers_user_id', 'user_answers', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key('fk_user_habits_user_id', 'user_habits', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key('fk_user_streaks_user_id', 'user_streaks', 'users', ['user_id'], ['id'], ondelete='CASCADE')


def downgrade() -> None:
    # Temporarily drop foreign key constraints
    op.drop_constraint('fk_user_answers_user_id', 'user_answers', type_='foreignkey')
    op.drop_constraint('fk_user_habits_user_id', 'user_habits', type_='foreignkey')
    op.drop_constraint('fk_user_streaks_user_id', 'user_streaks', type_='foreignkey')

    # Modify the users table
    op.alter_column('users', 'id',
               existing_type=sa.Integer(),
               type_=sa.String(length=100),
               existing_nullable=False)

    # Modify foreign key columns in related tables
    op.alter_column('user_answers', 'user_id',
               existing_type=sa.Integer(),
               type_=sa.String(length=100),
               existing_nullable=False)

    op.alter_column('user_habits', 'user_id',
               existing_type=sa.Integer(),
               type_=sa.String(length=100),
               existing_nullable=False)

    op.alter_column('user_streaks', 'user_id',
               existing_type=sa.Integer(),
               type_=sa.String(length=100),
               existing_nullable=False)

    # Recreate foreign key constraints
    op.create_foreign_key('fk_user_answers_user_id', 'user_answers', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key('fk_user_habits_user_id', 'user_habits', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key('fk_user_streaks_user_id', 'user_streaks', 'users', ['user_id'], ['id'], ondelete='CASCADE')

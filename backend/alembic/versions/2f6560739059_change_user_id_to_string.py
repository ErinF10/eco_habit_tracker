"""change_user_id_to_string

Revision ID: 2f6560739059
Revises: f9abe4133de5
Create Date: 2024-12-04 08:50:35.262572

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql


# revision identifiers, used by Alembic.
revision: str = '2f6560739059'
down_revision: Union[str, None] = 'f9abe4133de5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade():
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


def downgrade():
    # Temporarily drop foreign key constraints
    op.drop_constraint('fk_user_answers_user_id', 'user_answers', type_='foreignkey')
    op.drop_constraint('fk_user_habits_user_id', 'user_habits', type_='foreignkey')
    op.drop_constraint('fk_user_streaks_user_id', 'user_streaks', type_='foreignkey')

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

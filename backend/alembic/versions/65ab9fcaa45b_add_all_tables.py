"""Add all tables

Revision ID: 65ab9fcaa45b
Revises: 74cd623cf055
Create Date: 2024-11-09 08:46:33.885757

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '65ab9fcaa45b'
down_revision: Union[str, None] = '74cd623cf055'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('questions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question_text', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('answers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=True),
    sa.Column('answer_text', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['question_id'], ['questions.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_streaks',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('current_streak', sa.Integer(), nullable=True),
    sa.Column('best_streak', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_table('habit_suggestions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('habit_id', sa.Integer(), nullable=True),
    sa.Column('answer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['answer_id'], ['answers.id'], ),
    sa.ForeignKeyConstraint(['habit_id'], ['habits.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_answers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('answer_id', sa.Integer(), nullable=True),
    sa.Column('answered_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['answer_id'], ['answers.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_habit_progress',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_habit_id', sa.Integer(), nullable=True),
    sa.Column('week_start_date', sa.Date(), nullable=True),
    sa.Column('monday', sa.Enum('completed', 'partial', 'missed', 'not_scheduled'), nullable=True),
    sa.Column('tuesday', sa.Enum('completed', 'partial', 'missed', 'not_scheduled'), nullable=True),
    sa.Column('wednesday', sa.Enum('completed', 'partial', 'missed', 'not_scheduled'), nullable=True),
    sa.Column('thursday', sa.Enum('completed', 'partial', 'missed', 'not_scheduled'), nullable=True),
    sa.Column('friday', sa.Enum('completed', 'partial', 'missed', 'not_scheduled'), nullable=True),
    sa.Column('saturday', sa.Enum('completed', 'partial', 'missed', 'not_scheduled'), nullable=True),
    sa.Column('sunday', sa.Enum('completed', 'partial', 'missed', 'not_scheduled'), nullable=True),
    sa.ForeignKeyConstraint(['user_habit_id'], ['user_habits.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_habit_schedules',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_habit_id', sa.Integer(), nullable=True),
    sa.Column('monday', sa.Boolean(), nullable=True),
    sa.Column('tuesday', sa.Boolean(), nullable=True),
    sa.Column('wednesday', sa.Boolean(), nullable=True),
    sa.Column('thursday', sa.Boolean(), nullable=True),
    sa.Column('friday', sa.Boolean(), nullable=True),
    sa.Column('saturday', sa.Boolean(), nullable=True),
    sa.Column('sunday', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['user_habit_id'], ['user_habits.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.alter_column('users', 'password_hash',
               existing_type=mysql.VARCHAR(length=255),
               type_=sa.String(length=20),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'password_hash',
               existing_type=sa.String(length=20),
               type_=mysql.VARCHAR(length=255),
               nullable=True)
    op.drop_table('user_habit_schedules')
    op.drop_table('user_habit_progress')
    op.drop_table('user_answers')
    op.drop_table('habit_suggestions')
    op.drop_table('user_streaks')
    op.drop_table('answers')
    op.drop_table('questions')
    # ### end Alembic commands ###

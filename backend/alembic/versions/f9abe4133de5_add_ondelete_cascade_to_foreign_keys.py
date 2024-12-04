"""Add ondelete='CASCADE' to foreign keys

Revision ID: f9abe4133de5
Revises: 65ab9fcaa45b
Create Date: 2024-12-03 17:03:10.288941

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'f9abe4133de5'
down_revision: Union[str, None] = '65ab9fcaa45b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade():
    # HabitSuggestion Model
    op.drop_constraint('habit_suggestions_ibfk_1', 'habit_suggestions', type_='foreignkey')
    op.drop_constraint('habit_suggestions_ibfk_2', 'habit_suggestions', type_='foreignkey')
    # op.drop_constraint('fk_habit_suggestions_habit_id', 'habit_suggestions', type_='foreignkey')
    # op.drop_constraint('fk_habit_suggestions_answer_id', 'habit_suggestions', type_='foreignkey')
    op.alter_column('habit_suggestions', 'habit_id', existing_type=sa.Integer(), nullable=False)
    op.alter_column('habit_suggestions', 'answer_id', existing_type=sa.Integer(), nullable=False)
    op.create_foreign_key('fk_habit_suggestions_habit_id', 'habit_suggestions', 'habits', ['habit_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key('fk_habit_suggestions_answer_id', 'habit_suggestions', 'answers', ['answer_id'], ['id'], ondelete='CASCADE')

    # Answers Model
    op.drop_constraint('answers_ibfk_1', 'answers', type_='foreignkey')
    op.alter_column('answers', 'question_id', existing_type=sa.Integer(), nullable=False)
    op.create_foreign_key('fk_answers_question_id', 'answers', 'questions', ['question_id'], ['id'], ondelete='CASCADE')
  
    # UserAnswer Model
    # op.drop_constraint('fk_user_answers_user_id', 'user_answers', type_='foreignkey')
    # op.drop_constraint('fk_user_answers_answer_id', 'user_answers', type_='foreignkey')
    op.drop_constraint('user_answers_ibfk_1', 'user_answers', type_='foreignkey')
    op.drop_constraint('user_answers_ibfk_2', 'user_answers', type_='foreignkey')
    op.alter_column('user_answers', 'user_id', existing_type=sa.Integer(), nullable=False)
    op.alter_column('user_answers', 'answer_id', existing_type=sa.Integer(), nullable=False)
    op.create_foreign_key('fk_user_answers_user_id', 'user_answers', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key('fk_user_answers_answer_id', 'user_answers', 'answers', ['answer_id'], ['id'], ondelete='CASCADE')

    # UserHabitProgress Model
    op.drop_constraint('user_habit_progress_ibfk_1', 'user_habit_progress', type_='foreignkey')
    # op.drop_constraint('fk_user_habit_progress_user_habit_id', 'user_habit_progress', type_='foreignkey')
    op.alter_column('user_habit_progress', 'user_habit_id', existing_type=sa.Integer(), nullable=False)
    op.create_foreign_key('fk_user_habit_progress_user_habit_id', 'user_habit_progress', 'user_habits', ['user_habit_id'], ['id'], ondelete='CASCADE')

    # UserHabitSchedule Model
    op.drop_constraint('user_habit_schedules_ibfk_1', 'user_habit_schedules', type_='foreignkey')
    # op.drop_constraint('fk_user_habit_schedules_user_habit_id', 'user_habit_schedules', type_='foreignkey')
    op.alter_column('user_habit_schedules', 'user_habit_id', existing_type=sa.Integer(), nullable=False)
    op.create_foreign_key('fk_user_habit_schedules_user_habit_id', 'user_habit_schedules', 'user_habits', ['user_habit_id'], ['id'], ondelete='CASCADE')

    # UserHabit Model
    op.drop_constraint('user_habits_ibfk_1', 'user_habits', type_='foreignkey')
    op.drop_constraint('user_habits_ibfk_2', 'user_habits', type_='foreignkey')
    # op.drop_constraint('fk_user_habits_user_id', 'user_habits', type_='foreignkey')
    # op.drop_constraint('fk_user_habits_habit_id', 'user_habits', type_='foreignkey')
    op.alter_column('user_habits', 'user_id', existing_type=sa.Integer(), nullable=False)
    op.alter_column('user_habits', 'habit_id', existing_type=sa.Integer(), nullable=False)
    op.create_foreign_key('fk_user_habits_user_id', 'user_habits', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key('fk_user_habits_habit_id', 'user_habits', 'habits', ['habit_id'], ['id'], ondelete='CASCADE')

    # UserStreak Model
    op.drop_constraint('user_streaks_ibfk_1', 'user_streaks', type_='foreignkey')
    # op.drop_constraint('fk_user_streaks_user_id', 'user_streaks', type_='foreignkey')
    op.alter_column('user_streaks', 'user_id', existing_type=sa.Integer(), nullable=False)
    op.create_foreign_key('fk_user_streaks_user_id', 'user_streaks', 'users', ['user_id'], ['id'], ondelete='CASCADE')

def downgrade():
    # UserStreak Model
    op.drop_constraint('fk_user_streaks_user_id', 'user_streaks', type_='foreignkey')
    op.alter_column('user_streaks', 'user_id', existing_type=sa.Integer())
    op.create_foreign_key('user_streaks_ibfk_1', 'user_streaks', 'users', ['user_id'], ['id'])

    # UserHabit Model
    op.drop_constraint('fk_user_habits_habit_id', 'user_habits', type_='foreignkey')
    op.drop_constraint('fk_user_habits_user_id', 'user_habits', type_='foreignkey')
    op.alter_column('user_habits', 'habit_id', existing_type=sa.Integer())
    op.alter_column('user_habits', 'user_id', existing_type=sa.Integer())
    op.create_foreign_key('user_habits_ibfk_2', 'user_habits', 'habits', ['habit_id'], ['id'])
    op.create_foreign_key('user_habits_ibfk_1', 'user_habits', 'users', ['user_id'], ['id'])

    # UserHabitSchedule Model
    op.drop_constraint('fk_user_habit_schedules_user_habit_id', 'user_habit_schedules', type_='foreignkey')
    op.alter_column('user_habit_schedules', 'user_habit_id', existing_type=sa.Integer())
    op.create_foreign_key('user_habit_schedules_ibfk_1', 'user_habit_schedules', 'user_habits', ['user_habit_id'], ['id'])

    # UserHabitProgress Model
    op.drop_constraint('fk_user_habit_progress_user_habit_id', 'user_habit_progress', type_='foreignkey')
    op.alter_column('user_habit_progress', 'user_habit_id', existing_type=sa.Integer())
    op.create_foreign_key('user_habit_progress_ibfk_1', 'user_habit_progress', 'user_habits', ['user_habit_id'], ['id'])

    # UserAnswer Model
    op.drop_constraint('fk_user_answers_answer_id', 'user_answers', type_='foreignkey')
    op.drop_constraint('fk_user_answers_user_id', 'user_answers', type_='foreignkey')
    op.alter_column('user_answers', 'answer_id', existing_type=sa.Integer())
    op.alter_column('user_answers', 'user_id', existing_type=sa.Integer())
    op.create_foreign_key('user_answers_ibfk_2', 'user_answers', 'answers', ['answer_id'], ['id'])
    op.create_foreign_key('user_answers_ibfk_1', 'user_answers', 'users', ['user_id'], ['id'])

    # Answers Model
    op.drop_constraint('fk_answers_question_id', 'answers', type_='foreignkey')
    op.alter_column('answers', 'question_id', existing_type=sa.Integer())
    op.create_foreign_key('answers_ibfk_1', 'answers', 'questions', ['question_id'], ['id'])

    # HabitSuggestion Model
    op.drop_constraint('fk_habit_suggestions_answer_id', 'habit_suggestions', type_='foreignkey')
    op.drop_constraint('fk_habit_suggestions_habit_id', 'habit_suggestions', type_='foreignkey')
    op.alter_column('habit_suggestions', 'answer_id', existing_type=sa.Integer())
    op.alter_column('habit_suggestions', 'habit_id', existing_type=sa.Integer())
    op.create_foreign_key('habit_suggestions_ibfk_2', 'habit_suggestions', 'answers', ['answer_id'], ['id'])
    op.create_foreign_key('habit_suggestions_ibfk_1', 'habit_suggestions', 'habits', ['habit_id'], ['id'])
"""Initial migration

Revision ID: c92249860582
Revises: 
Create Date: 2025-05-20 17:12:47.206393

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c92249860582'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin_info',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('price_ticket', sa.Integer(), nullable=False),
    sa.Column('minutes', sa.Integer(), nullable=False),
    sa.Column('price_mini_games', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('info_achieving_the_goal',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('lvl', sa.Integer(), nullable=False),
    sa.Column('xp', sa.Integer(), nullable=False),
    sa.Column('money', sa.Integer(), nullable=False),
    sa.Column('ruby', sa.Integer(), nullable=False),
    sa.Column('cube', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('info_arcade',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title_name', sa.String(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(), nullable=False),
    sa.Column('img', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('info_dice_roll',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('lvl_dice_roll', sa.Integer(), nullable=False),
    sa.Column('xp', sa.Integer(), nullable=False),
    sa.Column('money', sa.Integer(), nullable=False),
    sa.Column('ruby', sa.Integer(), nullable=False),
    sa.Column('cube', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('info_xp',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('lvl', sa.Integer(), nullable=False),
    sa.Column('need_to', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('lottery',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('price_ticket', sa.Integer(), nullable=False),
    sa.Column('accumulation', sa.Integer(), nullable=True),
    sa.Column('time_start', sa.DateTime(), nullable=False),
    sa.Column('time_end', sa.DateTime(), nullable=False),
    sa.Column('win_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('shop_skills_info',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('skill_lvl', sa.Integer(), nullable=False),
    sa.Column('skill_name', sa.String(), nullable=False),
    sa.Column('ru_skill_name', sa.String(), nullable=False),
    sa.Column('skill_value', sa.Integer(), nullable=False),
    sa.Column('ruby_price', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('skills',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('drop_rate_gt_3', sa.Integer(), nullable=False),
    sa.Column('no_die_spend_chance', sa.Integer(), nullable=False),
    sa.Column('double_money_drop_chance', sa.Integer(), nullable=False),
    sa.Column('ruby_drop_chance', sa.Integer(), nullable=False),
    sa.Column('afk_dice', sa.Integer(), nullable=False),
    sa.Column('dice_per_hour', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('statistics',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('xp', sa.Integer(), nullable=False),
    sa.Column('lvl', sa.Integer(), nullable=False),
    sa.Column('cube', sa.Integer(), nullable=False),
    sa.Column('ruby', sa.Integer(), nullable=False),
    sa.Column('money', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('login', sa.String(), nullable=False),
    sa.Column('hash_password', sa.String(), nullable=False),
    sa.Column('is_admin', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vip_info',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('lvl', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('profile',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('statistics_id', sa.Integer(), nullable=False),
    sa.Column('skills_id', sa.Integer(), nullable=False),
    sa.Column('time_now', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['skills_id'], ['skills.id'], ),
    sa.ForeignKeyConstraint(['statistics_id'], ['statistics.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ticket',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('number', sa.Integer(), nullable=False),
    sa.Column('lottery_id', sa.Integer(), nullable=False),
    sa.Column('count_win', sa.Integer(), nullable=True),
    sa.Column('users_id', sa.Integer(), nullable=True),
    sa.Column('time_buy', sa.DateTime(), nullable=False),
    sa.Column('is_win', sa.Boolean(), nullable=True),
    sa.Column('is_trade', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['lottery_id'], ['lottery.id'], ),
    sa.ForeignKeyConstraint(['users_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vip',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('lvl', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('arcade',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name_arcade', sa.String(), nullable=False),
    sa.Column('id_user', sa.Integer(), nullable=False),
    sa.Column('win', sa.Integer(), nullable=False),
    sa.Column('lose', sa.Integer(), nullable=False),
    sa.Column('target_number', sa.Integer(), nullable=True),
    sa.Column('current_number', sa.Integer(), nullable=True),
    sa.Column('current_cube', sa.Integer(), nullable=True),
    sa.Column('status', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['id_user'], ['profile.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('arcade')
    op.drop_table('vip')
    op.drop_table('ticket')
    op.drop_table('profile')
    op.drop_table('vip_info')
    op.drop_table('users')
    op.drop_table('statistics')
    op.drop_table('skills')
    op.drop_table('shop_skills_info')
    op.drop_table('lottery')
    op.drop_table('info_xp')
    op.drop_table('info_dice_roll')
    op.drop_table('info_arcade')
    op.drop_table('info_achieving_the_goal')
    op.drop_table('admin_info')
    # ### end Alembic commands ###

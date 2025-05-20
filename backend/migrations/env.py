from logging.config import fileConfig
import sys
from os.path import abspath, dirname

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))

from backend.database import Base
from backend.achieving_the_goal.models import InfoAchievingTheGoal
from backend.arcade.models import Arcade
from backend.auth.models import Users
from backend.diceroll.models import InfoDicePoll
from backend.info.models import InfoXP
from backend.lottery.models import Lottery
from backend.profile.models import Profile
from backend.shop.models import ShopItem
from backend.skills.models import Skills
from backend.skillshop.models import ShopSkillsInfo
from backend.statistics.models import Statistics
from backend.ticket.models import Ticket
from backend.admin.models import AdminInfo
from backend.vip.models import Vip, VipInfo

from backend.config import settings

config = context.config
config.set_main_option("sqlalchemy.url", f"{settings.DATABASE_URL}?async_fallback=True")

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

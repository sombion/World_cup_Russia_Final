from sqlalchemy import update

from backend.achieving_the_goal.models import InfoAchievingTheGoal
from backend.arcade.dao import ArcadeBaseDAO, InfoArcadeGamesDAO
from backend.arcade.models import Arcade
from backend.database import async_session_maker


class AchievingTheGoalDAO(ArcadeBaseDAO):
    model = Arcade
    arcade_name = "achieving_the_goal"

    @classmethod
    async def set_target_number(cls, user_id, target_number):
        async with async_session_maker() as session:
            stmt = update(cls.model).where(user_id==user_id, cls.model.name_arcade==cls.arcade_name).values(
                target_number=target_number,
                current_cube=3
            )
            await session.execute(stmt)
            await session.commit()
            return {"status": 200}

    @classmethod
    async def set_now_number(cls, user_id, now_number):
        async with async_session_maker() as session:
            stmt = update(cls.model).where(user_id==user_id, cls.model.name_arcade==cls.arcade_name).values(
                current_number=now_number
            )
            await session.execute(stmt)
            await session.commit()
            return {"status": 200}

    @classmethod
    async def reset_target_and_number(cls, user_id, target_number: int = None):
        async with async_session_maker() as session:
            stmt = update(cls.model).where(user_id==user_id, cls.model.name_arcade==cls.arcade_name).values(
                target_number=target_number,
                current_number=0
            )
            await session.execute(stmt)
            await session.commit()
            return {"status": 200}

    @classmethod
    async def set_current_cube(cls, user_id, current_cube):
        async with async_session_maker() as session:
            stmt = update(cls.model).where(user_id==user_id, cls.model.name_arcade==cls.arcade_name).values(
                current_cube=current_cube
            )
            await session.execute(stmt)
            await session.commit()
            return {"status": 200}


class InfoAchievingTheGoalDAO(InfoArcadeGamesDAO):
    model = InfoAchievingTheGoal
from sqlalchemy import select, update

from backend.dao.base import BaseDAO
from backend.database import async_session_maker
from backend.profile.models import Profile
from backend.skills.models import Skills
from backend.statistics.models import Statistics


class ProfileDAO(BaseDAO):
    model = Profile

    @classmethod
    async def find_by_id(cls, user_id: int):
        async with async_session_maker() as session:
            query = (
                select(
                    cls.model.__table__.columns,
                    Skills.__table__.columns,
                    Statistics.__table__.columns
                ).join(Skills, cls.model.skills_id == Skills.id)
                .join(Statistics, cls.model.statistics_id == Statistics.id)
                .filter(Profile.user_id==user_id))
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def find_id_from_user_id(cls, user_id: int):
        async with async_session_maker() as session:
            query = select(cls.model.id).filter(Profile.user_id==user_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def update_time(cls, user_id: int, time):
        async with async_session_maker() as session:
            stmt = update(Profile).where(Profile.user_id==user_id).values(time_now=time)
            await session.execute(stmt)
            await session.commit()
            return {"status": 200}

    @classmethod
    async def create_user(cls, user_id: int):
        async with async_session_maker() as session:
            stmt = Statistics(
                xp=0,
                lvl=1,
                cube=0,
                ruby=10,
                money=0
            )
            session.add(stmt)
            await session.commit()
            statistics_id = stmt.id

        async with async_session_maker() as session:
            stmt = Skills(
                drop_rate_gt_3=0,
                no_die_spend_chance=0,
				double_money_drop_chance=0,
                ruby_drop_chance=10,
                afk_dice=0,
                dice_per_hour=1
            )
            session.add(stmt)
            await session.commit()
            skills_id = stmt.id

        async with async_session_maker() as session:
            stmt = Profile(
                statistics_id=statistics_id,
                skills_id=skills_id,
                user_id=user_id
            )
            session.add(stmt)
            await session.commit()

            return {"status": 200}
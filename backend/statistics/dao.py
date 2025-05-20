from sqlalchemy import insert, select, update, and_, func

from backend.dao.base import BaseDAO
from backend.database import async_session_maker
from backend.info.models import InfoXP
from backend.profile.models import Profile
from backend.statistics.models import Statistics


class StatisticsDAO(BaseDAO):
    model = Statistics

    @classmethod
    async def add(cls, xp: int, lvl: int, cube: int, ruby: int, money: int):
        async with async_session_maker() as session:
            stmt = insert(cls.model).values(
                xp=xp,
                lvl=lvl,
                cube=cube,
                ruby=ruby,
                money=money
            ).returning(cls.model)
            result = await session.execute(stmt)
            await session.commit()
            return result.scalar()

    @classmethod
    async def edit_dice_roll_db(
            cls,
            id_statistics: int,
            cube: int,
            money: int,
            ruby: int,
            lvl: int,
            xp: int
        ):
        async with async_session_maker() as session:
            stmt = update(Statistics).where(Statistics.id == id_statistics).values(cube=cube, money=money, ruby=ruby, lvl=lvl, xp=xp)
            await session.execute(stmt)
            await session.commit()

    @classmethod
    async def edit_ticket(cls, id: int, ticket: int):
        async with async_session_maker() as session:
            stmt = update(Statistics).where(Statistics.id==id).values(ticket=Statistics.ticket-ticket)
            await session.execute(stmt)
            await session.commit()
            return {"status": 200}

    @classmethod
    async def edit_money(cls, id: int, money: int):
        async with async_session_maker() as session:
            stmt = update(Statistics).where(Statistics.id==id).values(money=Statistics.money-money)
            await session.execute(stmt)
            await session.commit()
            return {"status": 200}

    @classmethod
    async def check_statistics_lvl(cls, current_level):
        async with async_session_maker() as session:
            query = select(InfoXP).filter(InfoXP.lvl > current_level).order_by(InfoXP.lvl)
            result = await session.execute(query)
            return result.scalars().all()

    @classmethod
    async def give_cube(cls, statistics_id: str, cube: int):
        async with async_session_maker() as session:
            stmt = update(Statistics).where(Statistics.id==statistics_id).values(
                cube = Statistics.cube + cube
            )
            await session.execute(stmt)
            await session.commit()
            return {"status": 200}

    @classmethod
    async def add_money(cls, user_id: int, money: int):
        async with async_session_maker() as session:
            stmt = (
                update(cls.model)
                .join(Profile, cls.model.id==Profile.statistics_id)
                .where(Profile.id==user_id)
                .values(money=cls.model.money+money)
            )
            result = await session.execute(stmt)
            await session.commit()
            return result.scalar()
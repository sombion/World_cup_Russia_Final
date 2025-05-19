from sqlalchemy import and_, insert, select, update

from backend.arcade.models import InfoArcade
from backend.dao.base import BaseDAO
from backend.database import async_session_maker
from backend.statistics.models import Statistics


class ArcadeBaseDAO(BaseDAO):
    model = None

    @classmethod
    async def create_model(
            cls,
            user_id,
            name_arcade: str,
            target_number: int = None,
            current_number: int = 0,
            current_cube: int = 3):
        async with async_session_maker() as session:
            stmt = insert(cls.model).values(
                id_user = user_id,
                name_arcade = name_arcade,
                win = 0,
				lose = 0,
				status = "games",
                target_number = target_number,
                current_number = current_number,
                current_cube = current_cube
            )
            await session.execute(stmt)
            await session.commit()
            return {"status": 200}

    @classmethod
    async def check_games(cls, user_id, name_arcade):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).where(
                and_(
                    cls.model.name_arcade==name_arcade,
                	cls.model.id_user==user_id,
                 	cls.model.status=="games"
				)
            )
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def win_one_games(cls, id_user, name_arcade):
        async with async_session_maker() as session:
            stmt = update(cls.model).where(cls.model.id_user==id_user, cls.model.name_arcade==name_arcade).values(win=cls.model.win+1)
            await session.execute(stmt)
            await session.commit()
            return {"status": 200}

    @classmethod
    async def lose_one_games(cls, id_user, name_arcade):
        async with async_session_maker() as session:
            stmt = update(cls.model).where(cls.model.id_user==id_user, cls.model.name_arcade==name_arcade).values(lose=cls.model.lose+1)
            await session.execute(stmt)
            await session.commit()
            return {"status": 200}

    @classmethod
    async def give_awards(cls, statistics_id, lvl, xp, money, ruby, cube):
        async with async_session_maker() as session:
            stmt = update(Statistics).where(Statistics.id==statistics_id).values(
				lvl = lvl,
				xp = xp,
				money = Statistics.money + money,
				ruby = Statistics.ruby + ruby,
				cube = Statistics.cube + cube
			)
            await session.execute(stmt)
            await session.commit()
            return {"status": 200}

    @classmethod
    async def end_games(cls, id_user, status, name_arcade):
        async with async_session_maker() as session:
            stmt = update(cls.model).where(
                cls.model.id_user==id_user,
                cls.model.name_arcade==name_arcade
            ).values(status = status)
            await session.execute(stmt)
            await session.commit()
            return {"status": 200}


class InfoArcadeDAO(BaseDAO):
    model = InfoArcade

    @classmethod
    async def find_arcade(cls):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns)
            result = await session.execute(query)
            return result.mappings().all()


class InfoArcadeGamesDAO(BaseDAO):
    model = None

    @classmethod
    async def check_lvl(cls, lvl: int):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).where(cls.model.lvl==lvl)
            result = await session.execute(query)
            return result.mappings().all()
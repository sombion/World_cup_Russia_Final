from sqlalchemy import and_, insert, select, update

from backend.arcade.dao import ArcadeBaseDAO
from backend.arcade.models import Arcade
from backend.dao.base import BaseDAO
from backend.database import async_session_maker
from backend.diceroll.models import InfoDicePoll


class DiceRollDAO(ArcadeBaseDAO):
    model = Arcade

    @classmethod
    async def create_model(cls, user_id):
        async with async_session_maker() as session:
            stmt = insert(Arcade).values(
                id_user = user_id,
                name_arcade = "dice-roll",
                win = 0,
				lose = 0,
				status = "games"
            )
            await session.execute(stmt)
            await session.commit()
            return {"status": 200}

    @classmethod
    async def check_games(cls, user_id):
        async with async_session_maker() as session:
            query = select(Arcade.__table__.columns).where(
                and_(
                    Arcade.name_arcade=="dice-roll",
                	Arcade.id_user==user_id,
                 	Arcade.status=="games"
				)
            )
            result = await session.execute(query)
            return result.mappings().all()



class InfoDicePollDAO(BaseDAO):
    model = InfoDicePoll

    @classmethod
    async def check_lvl(cls, lvl: int):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).where(cls.model.lvl_dice_roll==lvl)
            result = await session.execute(query)
            return result.mappings().all()
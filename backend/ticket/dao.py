from sqlalchemy import delete, desc, func, insert, select, update
from backend.dao.base import BaseDAO
from backend.database import async_session_maker
from backend.ticket.models import Ticket

class TicketDAO(BaseDAO):
    model = Ticket

    @classmethod
    async def add(cls, number: int, lottery_id: int, users_id: int) -> Ticket:
        async with async_session_maker() as session:
            stmt = insert(cls.model).values(
                number=number,
                lottery_id=lottery_id,
                users_id=users_id
            ).returning(cls.model)
            result = await session.execute(stmt)
            await session.commit()
            return result.scalar()

    @classmethod
    async def last_ticket(cls, lottery_id: int):
        async with async_session_maker() as session:
            query = select(Ticket.number).where(cls.model.lottery_id==lottery_id).order_by(desc(Ticket.number)).limit(1)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def count(cls, lottery_id: int):
        async with async_session_maker() as session:
            query = select(func.count(cls.model.lottery_id).label("count")).where(cls.model.lottery_id==lottery_id)
            result = await session.execute(query)
            return result.scalar()

    @classmethod
    async def buy(cls, user_id, lottery_id: int):
        async with async_session_maker() as session:
            stmt = (
                update(cls.model)
                .where(cls.model.lottery_id==lottery_id, cls.model.users_id==None)
                .values(user_id=user_id)
                .limit(1)
                .returning(cls.model)
            )
            result = await session.execute(stmt)
            await session.commit()
            return result.scalar()

    @classmethod
    async def trade(cls, id: int):
        async with async_session_maker() as session:
            stmt = (
                update(cls.model)
                .where(cls.model.id==id)
                .values(is_trade=True)
            )
            result = await session.execute(stmt)
            await session.commit()
            return result.scalar()

    @classmethod
    async def list_ticket_end(cls, lottery_id: int):
        async with async_session_maker() as session:
            query = select(Ticket.number).where(Ticket.lottery_id == lottery_id)
            result = await session.execute(query)
            return result.scalars().all()

    @classmethod
    async def win(cls, lottery_id: int, number: int, count_win: int):
        async with async_session_maker() as session:
            stmt = update(cls.model).where(cls.model.lottery_id==lottery_id, cls.model.number==number).values(is_win=True, count_win=count_win)
            await session.execute(stmt)
            await session.commit()
from backend.dao.base import BaseDAO
from backend.lottery.models import Lottery
from backend.database import async_session_maker
from sqlalchemy import insert, select, update


class UsersDAO(BaseDAO):
    model = Lottery
    
    # Взаимодействие с тикетами, количество оставшихся билетов 
    @classmethod
    async def list_all_lotteries():
        async with async_session_maker() as session:
            query = select()
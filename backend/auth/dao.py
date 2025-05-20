from backend.dao.base import BaseDAO
from backend.auth.models import Users
from backend.database import async_session_maker
from sqlalchemy import insert, select, update


class UsersDAO(BaseDAO):
    model = Users

    @classmethod
    async def add(
        cls,
        username: str,
        login: str,
        hash_password: str,
        is_admin: bool,
    ):
        async with async_session_maker() as session:
            stmt = insert(cls.model).values(
                username=username,
                login=login,
                hash_password=hash_password,
                is_admin=is_admin
            ).returning(cls.model.id)
            result = await session.execute(stmt)
            await session.commit()
            return result.scalar()

    @classmethod
    async def update(cls, user_id: int, **filter):
        async with async_session_maker() as session:
            stmt = update(cls.model).where(cls.model.id==user_id).values(**filter)
            await session.execute(stmt)
            await session.commit()
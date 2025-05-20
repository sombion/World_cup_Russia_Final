from backend.dao.base import BaseDAO
from backend.auth.models import Users
from backend.database import async_session_maker
from sqlalchemy import insert, select, update

from backend.profile.models import Profile
from backend.statistics.models import Statistics


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

    @classmethod
    async def detail(cls, user_id: int):
        async with async_session_maker() as session:
            query = (
                select(cls.model.__tablename__.column)
                .join(Profile, cls.model.id == Profile.user_id)
                .join(Statistics, Statistics.id == Profile.user_id)
            )
            result = await session.execute(query)
            return result.mappings().all()
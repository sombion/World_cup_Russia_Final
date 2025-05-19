from sqlalchemy import insert, select, update
from backend.dao.base import BaseDAO
from backend.database import async_session_maker
from backend.shop.models import BuyShopItem, ShopItem
from backend.statistics.models import Statistics


class InfoShopDAO(BaseDAO):
    model = ShopItem


class BuyShopDAO(BaseDAO):
    model = BuyShopItem

    @classmethod
    async def find_shop_by_date(cls, user_id, date):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(user_id=user_id, time_buy=date)
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def find_shop_by_date_list(cls, user_id, date):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns, ShopItem.__table__.columns).join(ShopItem, cls.model.item_id == ShopItem.id).filter(cls.model.user_id==user_id, cls.model.time_buy==date)
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def find_item_in_shop(cls, user_id, date, item_id):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(user_id=user_id, time_buy=date, item_id=item_id)
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def reduction_count(cls, id_item):
        async with async_session_maker() as session:
            stmt = update(cls.model).where(cls.model.id==id_item).values(
				count_by = (cls.model.count_by - 1)
			)
            await session.execute(stmt)
            await session.commit()
            return {"status": 200}

    @classmethod
    async def create_shop(cls, user_id, item_id, count):
        async with async_session_maker() as session:
            stmt = insert(cls.model).values(
				user_id=user_id,
				item_id=item_id,
    			count_by=count
			)
            await session.execute(stmt)
            await session.commit()
            return {"status": 200}

    @classmethod
    async def reduction_money(cls, profile, count: int):
        async with async_session_maker() as session:
            stmt = update(Statistics).where(Statistics.id==profile['statistics_id']).values(money = Statistics.money - count)
            await session.execute(stmt)
            await session.commit()
            return {"status": 200}

    @classmethod
    async def buy_ticket(cls, profile, count: int):
        async with async_session_maker() as session:
            stmt = update(Statistics).where(Statistics.id==profile['statistics_id']).values(ticket = Statistics.ticket + count)
            await session.execute(stmt)
            await session.commit()
            return {"status": 200}

    @classmethod
    async def buy_ruby(cls, profile, count: int):
        async with async_session_maker() as session:
            stmt = update(Statistics).where(Statistics.id==profile['statistics_id']).values(ruby = Statistics.ruby + count)
            await session.execute(stmt)
            await session.commit()
            return {"status": 200}
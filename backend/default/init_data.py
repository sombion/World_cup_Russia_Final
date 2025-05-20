import asyncio
import json

from sqlalchemy import insert, select
from backend.achieving_the_goal.models import InfoAchievingTheGoal
from backend.admin.models import AdminInfo
from backend.database import async_session_maker


def open_json(model: str):
    with open(f"backend/default/data/{model}.json", encoding="utf-8") as file:
        return json.load(file)


async def is_table_empty(session, model):
    result = await session.execute(select(model).limit(1))
    return result.scalar_one_or_none() is None


async def default_params():
    admin_info = open_json("admin_info")
    info_achieving_the_goal = open_json("info_achieving_the_goal")

    async with async_session_maker() as session:
        if await is_table_empty(session, AdminInfo):
            add_admin_info = insert(AdminInfo).values(admin_info)
            await session.execute(add_admin_info)
        if await is_table_empty(session, InfoAchievingTheGoal):
            add_info_achieving_the_goal = insert(InfoAchievingTheGoal).values(info_achieving_the_goal)
            await session.execute(add_info_achieving_the_goal)

        await session.commit()


if __name__ == "__main__":
    asyncio.run(default_params())

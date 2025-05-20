import asyncio
import json

from sqlalchemy import insert, select
from backend.achieving_the_goal.models import InfoAchievingTheGoal
from backend.admin.models import AdminInfo
from backend.arcade.models import InfoArcade
from backend.database import async_session_maker
from backend.diceroll.models import InfoDicePoll
from backend.info.models import InfoXP
from backend.skillshop.models import ShopSkillsInfo


def open_json(model: str):
    with open(f"backend/default/data/{model}.json", encoding="utf-8") as file:
        return json.load(file)


async def is_table_empty(session, model):
    result = await session.execute(select(model).limit(1))
    return result.scalar_one_or_none() is None


async def default_params():
    admin_info = open_json("admin_info")
    info_achieving_the_goal = open_json("info_achieving_the_goal")
    info_dice_roll = open_json("info_dice_roll")
    info_xp = open_json("info_xp")
    skill_shop_info = open_json("skill_shop_info")
    info_arcade = open_json("info_arcade")

    async with async_session_maker() as session:
        if await is_table_empty(session, AdminInfo):
            add_admin_info = insert(AdminInfo).values(admin_info)
            await session.execute(add_admin_info)
        if await is_table_empty(session, InfoAchievingTheGoal):
            add_info_achieving_the_goal = insert(InfoAchievingTheGoal).values(info_achieving_the_goal)
            await session.execute(add_info_achieving_the_goal)
        if await is_table_empty(session, InfoDicePoll):
            add_info_dice_roll = insert(InfoDicePoll).values(info_dice_roll)
            await session.execute(add_info_dice_roll)
        if await is_table_empty(session, InfoXP):
            add_info_xp = insert(InfoXP).values(info_xp)
            await session.execute(add_info_xp)
        if await is_table_empty(session, ShopSkillsInfo):
            add_skill_shop_info = insert(ShopSkillsInfo).values(skill_shop_info)
            await session.execute(add_skill_shop_info)
        if await is_table_empty(session, InfoArcade):
            add_info_arcade = insert(InfoArcade).values(info_arcade)
            await session.execute(add_info_arcade)
        await session.commit()

if __name__ == "__main__":
    asyncio.run(default_params())

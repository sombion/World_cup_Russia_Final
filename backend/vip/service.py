from backend.profile.dao import ProfileDAO
from backend.profile.models import Profile
from backend.statistics.dao import StatisticsDAO
from backend.statistics.models import Statistics
from backend.vip.dao import VipDAO


async def buy_vip(lvl: int, money: int, user_id: int):
    profile_data: Profile = await ProfileDAO.find_one_or_none(user_id=user_id)
    statistics_data: Statistics = await StatisticsDAO.find_by_id(profile_data.statistics_id)
    vip_data = await VipDAO.find_one_or_none(user_id=user_id)
    if not vip_data:
        await VipDAO.add(user_id, lvl)
    else:
        await VipDAO.update(user_id, lvl)
    # await StatisticsDAO.edit_money(statistics_data.id, money)
from backend.profile.dao import ProfileDAO
from backend.profile.models import Profile
from backend.statistics.dao import StatisticsDAO
from backend.statistics.models import Statistics
from backend.vip.dao import VipDAO


async def buy_vip(money: int, user_id: int):
    profile_data: Profile = ProfileDAO.find_one_or_none(user_id=user_id)
    statistics_data: Statistics = StatisticsDAO.find_by_id(profile_data.statistics_id)
    await StatisticsDAO.edit_money(statistics_data.id, money)
    await VipDAO.add()
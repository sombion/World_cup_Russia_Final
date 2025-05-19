from datetime import datetime, timedelta

from backend.profile.dao import ProfileDAO
from backend.statistics.dao import StatisticsDAO

async def check_cube_in_afk(user_id: int):
    profile = (await ProfileDAO.find_by_id(user_id))[0]
    now = datetime.now()
    now_without_seconds = now.replace(second=0, microsecond=0)
    difference = now_without_seconds - profile['time_now']

    hours = int(difference.total_seconds()) // 3600
    minutes = (int(difference.total_seconds()) % 3600) // 60

    if hours < 1:
        return {"status": 425, "info": "Время не пришло", "h": hours, "m": minutes}
    elif hours >= profile['afk_dice']:
        time = datetime.now()
        give_cube = profile['afk_dice'] * profile['dice_per_hour']
        result_profile = await ProfileDAO.update_time(user_id, time)
        result_cube = await StatisticsDAO.give_cube(profile['statistics_id'], give_cube)
        return {"status": 200, "give_cube": give_cube, "status_db": [result_profile, result_cube]}
    elif 1 <= hours < profile['afk_dice']:
        time = datetime.now() - timedelta(minutes=minutes)
        give_cube = hours * profile['dice_per_hour']
        result_profile = await ProfileDAO.update_time(user_id, time)
        result_cube = await StatisticsDAO.give_cube(profile['statistics_id'], give_cube)
        return {"status": 200, "give_cube": give_cube, "status_db": [result_profile, result_cube]}
    else:
        return {"status": 405, "h": hours, "m": minutes}
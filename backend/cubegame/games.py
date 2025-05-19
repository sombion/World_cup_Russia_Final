import random

from backend.info.dao import InfoXPDAO
from backend.profile.dao import ProfileDAO
from backend.statistics.dao import StatisticsDAO


async def play_cube_game(user_id: int):
    profile = (await ProfileDAO.find_by_user_id(user_id))[0]

    chances_money_not_skills = [16, 16, 16, 16, 16, 16]
    drop_rate_gt_3 = profile['drop_rate_gt_3']
    chances_money = []

    for i in range(0, 6):
        if i < 3:
            chances_money.append(int(chances_money_not_skills[i])-int(drop_rate_gt_3))
        else:
            chances_money.append(chances_money_not_skills[i]+drop_rate_gt_3)

    chances_ruby = [profile['ruby_drop_chance'], 100 - profile['ruby_drop_chance']]
    chances_double_money = [profile['double_money_drop_chance'], 100 - profile['double_money_drop_chance']]
    chances_no_die = [profile['no_die_spend_chance'], 100 - profile['no_die_spend_chance']]

    random_money = random.choices([1, 2, 3, 4, 5, 6], chances_money)[0]
    random_ruby = random.choices([1, 0], chances_ruby)[0]
    double_money = random.choices([int(random_money), 0], chances_double_money)[0]
    no_die = random.choices([1, 0], chances_no_die)[0]

    id_statistics = int(profile['statistics_id'])
    cube = int(profile['cube']) - 1 + no_die
    if cube - no_die < 0:
        return {"status": 404, "error": "Недостаточно кубиков"}
    money = int(profile['money']) + random_money + double_money
    ruby = int(profile['ruby']) + random_ruby
    xp = int(profile['xp']) + random_money
    lvl = profile['lvl']

    next_lvl = await InfoXPDAO.find_target_xp(lvl)
    if xp < int(next_lvl[0]['need_to']):
        lvl_now = lvl
        xp_now = xp
        xp_need_to = next_lvl[0]['need_to']
    else:
        lvl = int(next_lvl[0]['lvl'])
        xp = xp - int(next_lvl[0]['need_to'])
        ruby += 5
        lvl_now = lvl
        xp_now = xp
        next_lvl = await InfoXPDAO.find_target_xp(lvl_now)
        xp_need_to = next_lvl[0]['need_to']

    await StatisticsDAO.edit_dice_roll_db(id_statistics, cube, money, ruby, lvl_now, xp_now)
    return {"status": 200,
            "cube": cube,
            "money": money,
            "ruby": ruby,
            "random_money": random_money,
            "random_ruby": random_ruby,
            "lvl_now": lvl_now,
            "xp_now": xp_now,
            "xp_need_to": xp_need_to,
            "info_money": random_money + double_money}


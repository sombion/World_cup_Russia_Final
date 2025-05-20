import random

from backend.admin.dao import AdminInfoDAO
from backend.diceroll.dao import DiceRollDAO, InfoDicePollDAO
from backend.statistics.dao import StatisticsDAO


async def create_noviciate(profile):
    info_games = await DiceRollDAO.check_games(profile['id'])
    config = (await AdminInfoDAO.find_all())[0]
    prise = config['price_mini_games']
    if info_games == []:
        statistics_id = profile['statistics_id']
        money = profile['money']
        if money - prise < 0:
            return {"status": 402, "error": "Недостаточно монет"}
        else:
            await StatisticsDAO.edit_ticket(statistics_id, prise)
        result = await DiceRollDAO.create_model(profile['id'])
        return result
    else:
        return {"status": 200, "info": "Испытание идет"}

async def games(profile, lst):
	status_one_game = None
	check_game = await create_noviciate(profile)
	if check_game['status'] != 200:
		return check_game

	info_games = (await DiceRollDAO.check_games(profile['id']))[0]

	count = (random.choices([1, 2, 3, 4, 5, 6], [16, 16, 16, 16, 16, 16]))[0]

	if count in lst:
		await DiceRollDAO.win_one_games(profile['id'], "dice-roll")
		status_one_game = "Win"
	else:
		await DiceRollDAO.lose_one_games(profile['id'], "dice-roll")
		status_one_game = "Lose"

	info_games = (await DiceRollDAO.check_games(profile['id']))[0]
	if info_games['win'] >= 12 or info_games['lose'] >= 3:
		awards = await end_game(profile, info_games)
		return {
      		"status": 200,
          	"info": "Испытание окончено",
           	"win": info_games['win'],
			"lose": info_games['lose'],
           	"result": status_one_game,
            "count": count,
            "awards": awards
        }
	else:
		return {
			"status": 200,
   			"info": "Продолжение испытания",
      		"result": status_one_game,
        	"count": count,
         	"win": info_games['win'],
			"lose": info_games['lose']
    	}

async def check_next_lvl(current_xp, current_level, additional_xp):
	total_xp = current_xp + additional_xp

	next_levels = await StatisticsDAO.check_statistics_lvl(current_level)

	max_level = current_level
	remaining_xp = total_xp

	for level in next_levels:
		xp_needed = level.need_to
		if remaining_xp >= xp_needed:
			max_level = level.lvl
			remaining_xp -= xp_needed
		else:
			break

	return {
		"lvl": max_level,
		"xp": remaining_xp
	}

async def end_game(profile, info_games):
	status = ""
	if info_games['win'] >= 12:
		status = "win"
		await DiceRollDAO.end_games(profile['id'], status, "dice-roll")
	if info_games['lose'] >= 3:
		status = "lose"
		await DiceRollDAO.end_games(profile['id'], status, "dice-roll")
	lvl = info_games['win']
	if lvl <= 0 or lvl > 12:
		return {
			"xp": 0,
			"money": 0,
			"ruby": 0,
			"cube": 0
		}
	info_award = (await InfoDicePollDAO.check_lvl(lvl))[0]
	current_xp = profile['xp']
	current_level = profile['lvl']
	additional_xp = info_award['xp']
	lvl_and_xp = await check_next_lvl(current_xp, current_level, additional_xp)
	statistics_id = profile['statistics_id']
	xp = lvl_and_xp['xp']
	lvl = lvl_and_xp['lvl']
	money = info_award['money']
	ruby = info_award['ruby']
	cube = info_award['cube']
	await DiceRollDAO.give_awards(statistics_id, lvl, xp, money, ruby + (lvl - current_level) * 5, cube)
	return {
		"xp": additional_xp,
  		"money": money,
		"ruby": ruby,
		"cube": cube
	}



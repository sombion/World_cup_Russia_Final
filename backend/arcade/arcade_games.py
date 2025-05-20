from backend.admin.dao import AdminInfoDAO
from backend.statistics.dao import StatisticsDAO

class ArcadeGamesBase:
	name_arcade = None
	model_dao = None
	info_model = None

	@classmethod
	async def create_noviciate(cls, profile, target_number: int = None):
		info_games = await cls.model_dao.check_games(profile['id'], cls.name_arcade)
		statistics_data = StatisticsDAO.find_by_id(profile['statistics_id'])
		config = (await AdminInfoDAO.find_all())[0]
		prise = config['price_mini_games']
		if info_games == []:
			statistics_id = profile['statistics_id']
			if statistics_data.money - prise < 0:
				return {"status": 402, "error": "Недостаточно монет"}
			else:
				await StatisticsDAO.edit_money(id=statistics_id, money=prise)
			result = await cls.model_dao.create_model(profile['id'], cls.name_arcade, target_number)
			return result
		else:
			return {"status": 200, "info": "Испытание идет"}


	@classmethod
	async def check_next_lvl(cls, current_xp, current_level, additional_xp):
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

	@classmethod
	async def end_game(cls, profile, info_games):
		status = ""
		if info_games['win'] >= 10:
			status = "win"
			await cls.model_dao.end_games(profile['id'], status, cls.name_arcade)
		if info_games['lose'] >= 3:
			status = "lose"
			await cls.model_dao.end_games(profile['id'], status, cls.name_arcade)
		lvl = info_games['win']
		if lvl <= 0 or lvl > 10:
			return {
				"xp": 0,
				"money": 0,
				"ruby": 0,
				"cube": 0
			}
		info_award = (await cls.info_model.check_lvl(lvl))[0]
		current_xp = profile['xp']
		current_level = profile['lvl']
		additional_xp = info_award['xp']
		lvl_and_xp = await cls.check_next_lvl(current_xp, current_level, additional_xp)
		statistics_id = profile['statistics_id']
		xp = lvl_and_xp['xp']
		lvl = lvl_and_xp['lvl']
		money = info_award['money']
		ruby = info_award['ruby']
		cube = info_award['cube']
		await cls.model_dao.give_awards(statistics_id, lvl, xp, money, ruby + (lvl - current_level) * 10, cube)
		return {
			"xp": additional_xp,
			"money": money,
			"ruby": ruby,
			"cube": cube
		}



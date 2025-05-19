import random

from backend.achieving_the_goal.dao import AchievingTheGoalDAO, InfoAchievingTheGoalDAO
from backend.arcade.arcade_games import ArcadeGamesBase


TARGET_NUMBER = [
    [4, 5, 6], # 0
    [5, 6, 7], # 1
    [6, 7, 8], # 2
    [7, 8, 9], # 3
    [8, 9, 10], # 4
    [9, 10, 11], # 5
    [10, 11, 12], # 6
    [11, 12, 13], # 7
    [12, 13, 14], # 8
    [11, 12, 13, 14], # 9
    [12, 13, 14, 15], # 10
    [13, 14, 15], # 11
    [15, 16], # 12
]


class GamesAchievingTheGoal(ArcadeGamesBase):
	name_arcade = "achieving_the_goal"
	model_dao = AchievingTheGoalDAO
	info_model = InfoAchievingTheGoalDAO

	@classmethod
	async def games(cls, profile):
		status_one_game = None
		check_game = await cls.create_noviciate(profile, random.choice(TARGET_NUMBER[0]))
		if check_game['status'] != 200:
			return check_game

		info_games = (await AchievingTheGoalDAO.check_games(profile['id'], cls.name_arcade))[0]

		if info_games["target_number"] == None:
			target_number = random.choice(TARGET_NUMBER[info_games["win"]])
			await AchievingTheGoalDAO.set_target_number(profile['id'], target_number)
			info_games = (await AchievingTheGoalDAO.check_games(profile['id'], cls.name_arcade))[0]

		count = (random.choices([1, 2, 3, 4, 5, 6], [16, 16, 16, 16, 16, 16]))[0]

		if info_games["current_number"] is None:
			current_number = 0
		else:
			current_number = info_games["current_number"]

		if count + current_number >= info_games["target_number"]:
			await AchievingTheGoalDAO.win_one_games(profile['id'], cls.name_arcade)
			status_one_game = "Win"
			await AchievingTheGoalDAO.reset_target_and_number(profile['id'], random.choice(TARGET_NUMBER[info_games["win"]+1]))
			await AchievingTheGoalDAO.set_current_cube(profile['id'], 3)
		else:
			await AchievingTheGoalDAO.set_now_number(profile['id'], current_number + count)
			await AchievingTheGoalDAO.set_current_cube(profile['id'], info_games['current_cube'] - 1)

		# Проверка на кубик
		if info_games['current_cube'] - 1 <= 0 and status_one_game != "Win":
			await AchievingTheGoalDAO.lose_one_games(profile['id'], cls.name_arcade)
			await AchievingTheGoalDAO.reset_target_and_number(profile['id'], random.choice(TARGET_NUMBER[info_games["win"]]))
			await AchievingTheGoalDAO.set_current_cube(profile['id'], 3)
			status_one_game = "Lose"

		info_games = (await AchievingTheGoalDAO.check_games(profile['id'], cls.name_arcade))[0]

		if info_games['win'] >= 12 or info_games['lose'] >= 3:
			awards = await cls.end_game(profile, info_games)
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
				"target_number": info_games["target_number"],
				"current_number": info_games['current_number'],
				"current_cube": info_games["current_cube"],
				"count": count,
				"win": info_games['win'],
				"lose": info_games['lose']
			}


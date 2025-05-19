from fastapi import APIRouter, Depends

from backend.achieving_the_goal.games import GamesAchievingTheGoal
from backend.achieving_the_goal.dao import AchievingTheGoalDAO
from backend.auth.dependencies import get_current_user
from backend.auth.models import Users
from backend.profile.dao import ProfileDAO


router = APIRouter(
	prefix="/api/achieving-the-goal",
	tags=["API для режима достижение цели"]
)


@router.post("/games")
async def games(current_user: Users = Depends(get_current_user)):
	profile = (await ProfileDAO.find_by_id(current_user.id))[0]
	result = await GamesAchievingTheGoal.games(profile)
	return result

@router.post('/info-games')
async def info_games(current_user: Users = Depends(get_current_user)):
    profile = (await ProfileDAO.find_by_id(current_user.id))[0]
    result = await AchievingTheGoalDAO.check_games(profile['id'], "achieving_the_goal")
    return result
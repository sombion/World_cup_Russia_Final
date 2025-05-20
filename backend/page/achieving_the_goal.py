from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
import random
from backend.achieving_the_goal.dao import AchievingTheGoalDAO
from backend.achieving_the_goal.games import GamesAchievingTheGoal
from backend.profile.dao import ProfileDAO
from backend.auth.dependencies import get_current_user
from backend.auth.models import Users

router = APIRouter()

templates = Jinja2Templates(directory="backend/templates")


@router.get("/games_2/achieving-the-goal")
async def achieving_the_goal(request: Request, current_user: Users = Depends(get_current_user)):
    profile = (await ProfileDAO.find_by_id(current_user.id))[0]
    info_arcade = await GamesAchievingTheGoal.create_noviciate(profile, random.choice([4, 5, 6]))
    if info_arcade['status'] != 200:
        return info_arcade
    info_achieving_the_goal = (await AchievingTheGoalDAO.check_games(profile['id'], "achieving_the_goal"))[0]
    return templates.TemplateResponse("achieving_the_goal.html", {
        "request": request,
        "profile": profile,
        "info_achieving_the_goal": info_achieving_the_goal
    })
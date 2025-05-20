from datetime import datetime

from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates

from backend.achieving_the_goal.dao import AchievingTheGoalDAO
from backend.arcade.dao import InfoArcadeDAO
from backend.diceroll.dao import DiceRollDAO
from backend.profile.dao import ProfileDAO
from backend.auth.dependencies import get_current_user
from backend.auth.models import Users

router = APIRouter()

templates = Jinja2Templates(directory="backend/templates")


@router.get("/arcade")
async def index(request: Request, current_user: Users = Depends(get_current_user)):
    profile = (await ProfileDAO.find_by_id(current_user.id))[0]

    info_dice_roll = await DiceRollDAO.check_games(profile['id'])
    if info_dice_roll != []:
        info_dice_roll = info_dice_roll[0]

    info_achieving_the_goal = await AchievingTheGoalDAO.check_games(profile['id'], "achieving_the_goal")
    if info_achieving_the_goal != []:
        info_achieving_the_goal = info_achieving_the_goal[0]

    info_arcade = await InfoArcadeDAO.find_arcade()

    return templates.TemplateResponse("arcade.html", {
        "request": request,
        "profile": profile,
        "info_dice_roll": info_dice_roll,
        "info_achieving_the_goal": info_achieving_the_goal,
        "info_arcade": info_arcade
    })

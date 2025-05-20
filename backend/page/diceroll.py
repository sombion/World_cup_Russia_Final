from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates

from backend.diceroll.dao import DiceRollDAO
from backend.diceroll.games import create_noviciate
from backend.profile.dao import ProfileDAO
from backend.auth.dependencies import get_current_user
from backend.auth.models import Users

router = APIRouter()

templates = Jinja2Templates(directory="backend/templates")


@router.get("/games_2/diceroll")
async def index(request: Request, current_user: Users = Depends(get_current_user)):
    profile = (await ProfileDAO.find_by_id(current_user.id))[0]
    info_arcade = await create_noviciate(profile)
    if info_arcade['status'] != 200:
        return info_arcade
    info_dice_roll = (await DiceRollDAO.check_games(profile['id']))[0]
    return templates.TemplateResponse("diceroll.html", {
        "request": request,
        "profile": profile,
        "info_dice_roll": info_dice_roll
    })
from fastapi import APIRouter, Depends
from pydantic import BaseModel

from backend.auth.dependencies import get_current_user
from backend.auth.models import Users
from backend.diceroll.dao import DiceRollDAO
from backend.diceroll.games import games, create_noviciate
from backend.diceroll.schemas import SBaseStart
from backend.profile.dao import ProfileDAO

router = APIRouter(
    prefix="/api/dice-roll",
	tags={"АПИ броска кубика"}
)


@router.post('/game')
async def api_games(base_start: SBaseStart, current_user: Users = Depends(get_current_user)):
    if len(base_start.lst) > 3:
        return {"status": 404, "error": "Выбрано больше 3 чисел"}
    profile = (await ProfileDAO.find_by_id(current_user.id))[0]
    result = await games(profile, base_start.lst)
    return result

@router.post('/start-game')
async def start_game(current_user: Users = Depends(get_current_user)):
    profile = (await ProfileDAO.find_by_id(current_user.id))[0]
    result = await create_noviciate(profile)
    return result

@router.post('/info-games')
async def info_games(current_user: Users = Depends(get_current_user)):
    profile = (await ProfileDAO.find_by_id(current_user.id))[0]
    result = await DiceRollDAO.check_games(profile['id'])
    return result

@router.post('/check-ticket')
async def api_check_ticket(current_user: Users = Depends(get_current_user)):
    profile = (await ProfileDAO.find_by_id(current_user.id))[0]
    if profile['ticket'] <= 0:
        return {"status": 402, "error": "Недостаточное кол-во билетов"}
    return {profile}
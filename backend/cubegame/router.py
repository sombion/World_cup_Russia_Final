from fastapi import APIRouter, Depends

from backend.auth.dependencies import get_current_user
from backend.auth.models import Users
from backend.cubegame.games import play_cube_game

router = APIRouter(
    prefix="/api/cube-game",
	tags={"API Главной страницы"}
)


@router.get('/game')
async def role_dice(current_user: Users = Depends(get_current_user)):
    result = await play_cube_game(current_user.id)
    return result
from fastapi import APIRouter, Depends

from backend.profile.dao import ProfileDAO
from backend.profile.afk_cube_farm import check_cube_in_afk
from backend.auth.dependencies import get_current_user
from backend.auth.models import Users


router = APIRouter(
	prefix="/api/profile",
	tags=["API профиля"]
)


@router.post('/info')
async def api_profile_info(current_user: Users = Depends(get_current_user)):
	profile = (await ProfileDAO.find_by_id(current_user.id))[0]
	return profile

@router.post('/time')
async def api_profile_time(current_user: Users = Depends(get_current_user)):
    result = await check_cube_in_afk(current_user.id)
    return result
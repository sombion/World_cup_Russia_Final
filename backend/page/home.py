from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates

from backend.info.dao import InfoXPDAO
from backend.profile.afk_cube_farm import check_cube_in_afk
from backend.profile.dao import ProfileDAO
from backend.statistics.dao import StatisticsDAO
from backend.auth.dependencies import get_current_user
from backend.auth.models import Users

router = APIRouter(
    tags={"Главная страница"}
)

templates = Jinja2Templates(directory="backend/templates")

@router.get("/")
async def index(request: Request, current_user: Users = Depends(get_current_user)):
    profile = await ProfileDAO.find_by_id(current_user.id)
    if profile == []:
        user_name = current_user.username
        await ProfileDAO.create_user(current_user.id, user_name)
        profile = (await ProfileDAO.find_by_id(current_user.id))[0]
    else:
        profile = profile[0]
    info_cube = await check_cube_in_afk(profile['user_id'])
    if info_cube['status'] != 200:
        info_cube = None
    next_lvl = await InfoXPDAO.find_target_xp(profile['lvl'])
    return templates.TemplateResponse("index.html", {"request": request, "profile": profile, "next": next_lvl[0], "info_cube": info_cube})
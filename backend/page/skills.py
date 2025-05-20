from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates

from backend.profile.dao import ProfileDAO
from backend.skillshop.dao import SkillShopDAO
from backend.auth.dependencies import get_current_user
from backend.auth.models import Users

router = APIRouter()

templates = Jinja2Templates(directory="backend/templates")


@router.get("/skills")
async def index(request: Request, current_user: Users = Depends(get_current_user)):
    profile = (await ProfileDAO.find_by_id(current_user.id))[0]
    item_skill = await SkillShopDAO.find_list_now_shop(profile)
    max_skill = await SkillShopDAO.find_max_skill()
    for skill in max_skill:
        if profile[skill['skill_name']] == skill['max_skill_value']:
            item_skill.append({
                "skill_name": skill['skill_name'],
                "ru_skill_name": skill['ru_skill_name'],
                "skill_value": skill['max_skill_value'],
                "skill_max": True,
                "skill_lvl": "Макс. уровень"
            })
    return templates.TemplateResponse("skills.html", {"request": request, "profile": profile, "item_skill": item_skill})
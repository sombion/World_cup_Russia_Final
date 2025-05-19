from fastapi import APIRouter, Depends
from pydantic import BaseModel

from backend.profile.dao import ProfileDAO
from backend.skillshop.dao import SkillShopDAO
from backend.auth.dependencies import get_current_user
from backend.auth.models import Users
from backend.shop.router import SBuyModel

router = APIRouter(
	prefix="/api/info-shop",
	tags={"API улучшение скилов"}
)


@router.get("/")
async def list_up(current_user: Users = Depends(get_current_user)):
    profile = (await ProfileDAO.find_by_id(current_user.id))[0]
    result = await SkillShopDAO.find_list_now_shop(profile)
    return result

@router.get('/max')
async def max_lvl():
    max_skill = await SkillShopDAO.find_max_skill()
    return max_skill

@router.post("/buy-skill")
async def buy_skill(buy_model: SBuyModel, current_user: Users = Depends(get_current_user)):
    skill_name = buy_model.skill_name
    try:
        profile = (await ProfileDAO.find_by_id(current_user.id))[0]
        skill_list = await SkillShopDAO.find_list_now_shop(profile)
        skill = [item for item in skill_list if item['skill_name'] == skill_name]
        if skill[0]['ruby_price'] <= profile['ruby']:
            update_skills = await SkillShopDAO.update_skills(skill=skill[0], skills_id=profile['skills_id'])
            ruby = profile['ruby'] - int(skill[0]['ruby_price'])
            update_profile = await SkillShopDAO.update_profile_skill(statistics_id=profile['statistics_id'], rubies_after_purchase=ruby)
            return {"buy": True, "update_skills": update_skills, "update_profile": update_profile}
        else:
            return {"buy": False, "error": "Недостаточное кол-во рубинов"}
    except IndexError:
        print(f"Попытка купить макс. улучшение, tg_id: {current_user.id}")
        return {"buy": False, "error": "Максимальный уровень"}
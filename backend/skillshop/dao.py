from sqlalchemy import and_, func, or_, select, update

from backend.dao.base import BaseDAO
from backend.database import async_session_maker
from backend.skills.models import Skills
from backend.skillshop.models import ShopSkillsInfo
from backend.statistics.models import Statistics


class SkillShopDAO(BaseDAO):
    model = ShopSkillsInfo

    @classmethod
    async def find_list_now_shop(cls, skills):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).where(
                or_(
					and_(cls.model.skill_name == 'drop_rate_gt_3',
          				cls.model.skill_value == skills['drop_rate_gt_3']+1),
					and_(cls.model.skill_name == 'no_die_spend_chance',
          				cls.model.skill_value == skills['no_die_spend_chance']+1),
     				and_(cls.model.skill_name == 'double_money_drop_chance',
          				cls.model.skill_value == skills['double_money_drop_chance']+1),
					and_(cls.model.skill_name == 'ruby_drop_chance',
          				cls.model.skill_value == skills['ruby_drop_chance']+1),
     				and_(cls.model.skill_name == 'afk_dice',
          				cls.model.skill_value == skills['afk_dice']+1),
					and_(cls.model.skill_name == 'dice_per_hour',
          				cls.model.skill_value == skills['dice_per_hour']+1)
				))
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def find_max_skill(cls):
        async with async_session_maker() as session:
            subquery = select(
                cls.model.skill_name,
                func.max(cls.model.skill_value).label('max_skill_value')
            ).group_by(cls.model.skill_name).subquery()

            query = select(
                cls.model.skill_name,
                cls.model.ru_skill_name,
                subquery.c.max_skill_value.label('max_skill_value')
            ).join(
                subquery,
                (cls.model.skill_name == subquery.c.skill_name) & (cls.model.skill_value == subquery.c.max_skill_value)
            )
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def update_skills(cls, skill, skills_id: int):
        async with async_session_maker() as session:
            if skill['skill_name'] == 'drop_rate_gt_3':
                query = update(Skills).where(Skills.id==skills_id).values(drop_rate_gt_3=int(skill['skill_value']))
            elif skill['skill_name'] == 'no_die_spend_chance':
                query = update(Skills).where(Skills.id==skills_id).values(no_die_spend_chance=int(skill['skill_value']))
            elif skill['skill_name'] == 'double_money_drop_chance':
                query = update(Skills).where(Skills.id==skills_id).values(double_money_drop_chance=int(skill['skill_value']))
            elif skill['skill_name'] == 'ruby_drop_chance':
                query = update(Skills).where(Skills.id==skills_id).values(ruby_drop_chance=int(skill['skill_value']))
            elif skill['skill_name'] == 'afk_dice':
                query = update(Skills).where(Skills.id==skills_id).values(afk_dice=int(skill['skill_value']))
            elif skill['skill_name'] == 'dice_per_hour':
                query = update(Skills).where(Skills.id==skills_id).values(dice_per_hour=int(skill['skill_value']))
            else:
                return {"error": "Not found"}
            result = await session.execute(query)
            await session.commit()
            return {"status": 200}

    @classmethod
    async def update_profile_skill(cls, statistics_id, rubies_after_purchase: int):
        async with async_session_maker() as session:
            query = update(Statistics).where(Statistics.id==statistics_id).values(ruby=rubies_after_purchase)
            result = await session.execute(query)
            await session.commit()
            return {"status": 200}
from sqlalchemy import insert
from backend.dao.base import BaseDAO
from backend.skills.models import Skills
from backend.database import async_session_maker

class SkillsDAO(BaseDAO):
    model = Skills


    @classmethod
    async def add(
        cls,
        drop_rate_gt_3: int,
        no_die_spend_chance: int,
        double_money_drop_chance: int,
        ruby_drop_chance: int,
        afk_dice: int,
        dice_per_hour: int
    ):
        async with async_session_maker() as session:
            stmt = insert(cls.model).values(
                drop_rate_gt_3=drop_rate_gt_3,
                no_die_spend_chance=no_die_spend_chance,
                double_money_drop_chance=double_money_drop_chance,
                ruby_drop_chance=ruby_drop_chance,
                afk_dice=afk_dice,
                dice_per_hour=dice_per_hour,
            ).returning(cls.model)
            result = await session.execute(stmt)
            await session.commit()
            return result.scalar()
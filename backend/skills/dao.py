from backend.dao.base import BaseDAO
from backend.skills.models import Skills

class SkillsDAO(BaseDAO):
    model = Skills
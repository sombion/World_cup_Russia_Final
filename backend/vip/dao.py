from sqlalchemy import select, update

from backend.dao.base import BaseDAO
from backend.database import async_session_maker
from backend.vip.models import VipInfo


class VipDAO(BaseDAO):
    model = VipInfo

    

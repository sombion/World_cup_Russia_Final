from fastapi import APIRouter, Depends

from backend.auth.dependencies import get_current_user
from backend.auth.models import Users
from backend.vip.dao import VipDAO
from backend.vip.schemas import SBuyVip


router = APIRouter(
	prefix="/api/vip",
	tags=["API vip"]
)

@router.post('/info')
async def api_vip_info(current_user: Users = Depends(get_current_user)):
	return await VipDAO.find_by_id(current_user.id)

@router.get('/buy')
async def api_vip_buy(vip_data: SBuyVip, current_user: Users = Depends(get_current_user)):
    await 
    return
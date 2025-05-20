from fastapi import APIRouter, Depends

from backend.auth.dependencies import get_current_user
from backend.auth.models import Users
from backend.vip.dao import VipDAO
from backend.vip.schemas import SBuyVip
from backend.vip.service import buy_vip


router = APIRouter(
	prefix="/api/vip",
	tags=["API vip"]
)

@router.post('/info')
async def api_vip_info(current_user: Users = Depends(get_current_user)):
	return await VipDAO.find_one_or_none(user_id=current_user.id)

@router.post('/buy')
async def api_vip_buy(vip_data: SBuyVip, current_user: Users = Depends(get_current_user)):
    await buy_vip(vip_data.lvl, vip_data.money, current_user.id)
    return {"detail": "Билет успешно куплен"}
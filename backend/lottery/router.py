from datetime import datetime
from fastapi import APIRouter, Depends

from backend.auth.dependencies import get_admin_user
from backend.auth.models import Users
from backend.lottery.dao import LotteryDAO
from backend.lottery.schemas import SCreateLottery
from backend.lottery.service import check_and_finish_lottery, create_lottery, detail_lottery

router = APIRouter(
    prefix="/api/lottery",
    tags=["API лоттереи"]
)

@router.get("/detail/{id}")
async def api_detail_lottery(id: int):
    return await detail_lottery(id)

@router.post("/create")
async def api_create_lottery(lottery_data: SCreateLottery, current_user: Users = Depends(get_admin_user)):
    return await create_lottery(
        lottery_data.title,
        lottery_data.description,
        lottery_data.time_start.replace(second=0, microsecond=0, tzinfo=None)
    )

@router.get("/all")
async def api_all_lottery():
    return {"lotterys": await LotteryDAO.all_future()}

@router.get("/end_all")
async def api_end_all():
    return await end_all()
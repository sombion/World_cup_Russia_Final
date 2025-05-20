from fastapi import APIRouter

from backend.lottery.dao import LotteryDAO
from backend.lottery.schemas import SCreateLottery
from backend.lottery.service import create_lottery, detail_lottery

router = APIRouter(
    prefix="/api/lottery",
    tags=["API лоттереи"]
)

@router.get("/detail/{id}")
async def api_detail_lottery(id: int):
    return await detail_lottery(id)

@router.post("/create")
async def api_create_lottery(lottery_data: SCreateLottery):
    return await create_lottery(
        lottery_data.title,
        lottery_data.description,
        lottery_data.max_count_ticket,
        lottery_data.count_ticket_win,
        lottery_data.time_start,
    )

@router.patch("/update")
async def api_update_lottery():
    return await LotteryDAO.update()


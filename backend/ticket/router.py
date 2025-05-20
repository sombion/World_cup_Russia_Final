from fastapi import APIRouter, Depends

from backend.auth.dependencies import get_current_user
from backend.auth.models import Users
from backend.ticket.dao import TicketDAO
from backend.ticket.schemas import SBuyTicket, STradeLoseTicker
from backend.ticket.service import buy_ticket, trade_lose_ticket

router = APIRouter(
    prefix="/ticket",
    tags=["API ticket"]
)

@router.get("/lottery/{lottery_id}")
async def api_detail_ticket(lottery_id: int, current_user: Users = Depends(get_current_user)):
    return await TicketDAO.find_all(lottery_id=lottery_id, user_id=current_user.id)

@router.post("/buy")
async def api_buy_ticket(buy_ticket_data: SBuyTicket, current_user: Users = Depends(get_current_user)):
    return await buy_ticket(buy_ticket_data.lottery_id, buy_ticket_data.money, current_user.id)

@router.post("/trade-lose")
async def api_trade_lose_ticket(trade_data: STradeLoseTicker, current_user: Users = Depends(get_current_user)):
    return await trade_lose_ticket(trade_data.ticket_id, current_user.id)
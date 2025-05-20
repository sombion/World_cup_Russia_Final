from fastapi import APIRouter, Depends

from backend.auth.dependencies import get_current_user
from backend.auth.models import Users
from backend.ticket.dao import TicketDAO
from backend.ticket.schemas import SBuyTicket, STradeLoseTicker
from backend.ticket.service import buy_ticket, trade_lose_ticket

router = APIRouter(
    prefix="/api/ticket",
    tags=["API ticket"]
)

@router.get("/all/{lottery_id}")
async def api_all_ticket(lottery_id: int):
    return await TicketDAO.find_all(lottery_id=lottery_id)

@router.get("/my")
async def api_my_ticket(current_user: Users = Depends(get_current_user)):
    return {"tickets": await TicketDAO.find_all(users_id=current_user.id)}

@router.post("/buy")
async def api_buy_ticket(buy_ticket_data: SBuyTicket, current_user: Users = Depends(get_current_user)):
    return await buy_ticket(buy_ticket_data.lottery_id, buy_ticket_data.money, current_user.id)

@router.post("/trade-lose")
async def api_trade_lose_ticket(trade_data: STradeLoseTicker, current_user: Users = Depends(get_current_user)):
    return await trade_lose_ticket(trade_data.ticket_id, current_user.id)
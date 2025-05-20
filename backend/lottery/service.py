from datetime import datetime, timedelta
from backend.admin.dao import AdminInfoDAO
from backend.exceptions import LotteryNotFoundException
from backend.lottery.dao import LotteryDAO
from backend.ticket.dao import TicketDAO


async def create_lottery(
    title: str,
    description: str,
    time_start: datetime,
):
    admin_data = await AdminInfoDAO.find_by_id(1)
    price_ticket = admin_data.price_ticket
    minutes = admin_data.minutes
    # Проверка на занятость времени
    lottery_date = await LotteryDAO.add(
        title=title,
        description=description,
        price_ticket=price_ticket,
        time_start=time_start,
        time_end=time_start + timedelta(minutes=minutes)
    )
    return {"detail": "Лотерея успешно создана"}

async def detail_lottery(lottery_id: int):
    lottery_detail = await LotteryDAO.find_by_id(lottery_id)
    if not lottery_detail:
        raise LotteryNotFoundException
    ticket_count = await TicketDAO.count(lottery_id)
    lottery_detail.ticket_count = ticket_count
    return lottery_detail
from datetime import datetime, timedelta
from backend.admin.dao import AdminInfoDAO
from backend.exceptions import LotteryNotFoundException
from backend.lottery.dao import LotteryDAO
from backend.ticket.dao import TicketDAO


async def create_lottery(
    title: str,
    description: str,
    max_count_ticket: int,
    count_ticket_win: int,
    time_start: datetime,
):
    admin_data = await AdminInfoDAO.find_by_id(1)
    price_ticket = admin_data.price_ticket
    minutes = admin_data.minutes
    if count_ticket_win > max_count_ticket//2:
        max_count_ticket = max_count_ticket // 2
    # Проверка на занятость времени
    lottery_date = await LotteryDAO.add(
        title=title,
        description=description,
        max_count_ticket=max_count_ticket,
        count_ticket_win=count_ticket_win,
        price_ticket=price_ticket,
        time_start=time_start,
        time_end=time_start + timedelta(minutes=minutes)
    )
    for i in range(1, max_count_ticket+1):
        await TicketDAO.add(i, lottery_date.id)
    return {"detail": "Лотерея успешно создана"}

async def detail_lottery(lottery_id: int):
    lottery_detail = await LotteryDAO.find_by_id(lottery_id)
    if not lottery_detail:
        raise LotteryNotFoundException
    ticket_count = await TicketDAO.count(lottery_id)
    lottery_detail.ticket_count = ticket_count
    return lottery_detail
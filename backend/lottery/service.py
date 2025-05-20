from datetime import datetime, timedelta
import random
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

async def check_and_finish_lottery():
    now = datetime.utcnow()

    lotteries_to_close = await LotteryDAO.list_end_lottery(now)

    for lottery in lotteries_to_close:
        # Получаем все билеты по этой лотерее
        tickets = await TicketDAO.list_ticket_end(lottery.id)
        if not tickets:
            # Если билетов нет — просто завершаем лотерею
            lottery.win_time = now
            continue
        count_win = len(tickets) // 2
        result = random.sample(tickets, count_win)
        S=sum([1/x for x in range(1, count_win+1)])
        return S
        # win_current_user = int(int(lottery.accumulation)/S)
        # return win_current_user
        for number in result:
            await TicketDAO.win(lottery.id, number, )
        return S
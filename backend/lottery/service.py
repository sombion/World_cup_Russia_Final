from datetime import datetime, timedelta
import random
from backend.admin.dao import AdminInfoDAO
from backend.exceptions import LotteryNotFoundException
from backend.lottery.dao import LotteryDAO
from backend.profile.dao import ProfileDAO
from backend.profile.models import Profile
from backend.statistics.dao import StatisticsDAO
from backend.statistics.models import Statistics
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

async def end_all():
    now = datetime.utcnow()
    lotteries_to_close = await LotteryDAO.list_end_lottery(now)
    for lottery in lotteries_to_close:
        tickets = await TicketDAO.list_ticket_end(lottery.id)
        if not tickets:
            lottery.win_time = now
            continue
        count_win = len(tickets) // 2
        result = random.sample(tickets, count_win)
        S=sum([1/x for x in range(1, count_win+1)])
        win_current_user = int(lottery.accumulation/S)
        start = lottery.time_start
        end = lottery.time_end
        delta = end - start
        random_seconds = random.randint(0, int(delta.total_seconds()))
        random_date = start + timedelta(seconds=random_seconds)
        win_time = random_date.replace(second=0, microsecond=0, tzinfo=None)
        i = 1
        for number in result:
            current_ticket = await TicketDAO.find_one_or_none(lottery_id=lottery.id, number=number)
            if current_ticket.time_buy == win_time:
                profile_data: Profile = (await ProfileDAO.find_by_id(current_ticket.users_id))[0]
                statictics_data: Statistics = await StatisticsDAO.find_by_id(int(profile_data['statistics_id']))
                await StatisticsDAO.add_money(statictics_data.id, int(S * 0.025))
            await TicketDAO.win(lottery.id, number, int(win_current_user*(1/i)))
            i+=1
        await LotteryDAO.update_win_time(lottery.id, win_time)
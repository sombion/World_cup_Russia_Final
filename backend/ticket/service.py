from backend.exceptions import GameNotFinishedException, InvalidCoinsAmountException, TicketAlreadyRedeemedException, TicketNotFoundException, UnableToWithdrawCoinsException
from backend.lottery.dao import LotteryDAO
from backend.lottery.models import Lottery
from backend.profile.dao import ProfileDAO
from backend.profile.models import Profile
from backend.statistics.dao import StatisticsDAO
from backend.statistics.models import Statistics
from backend.ticket.dao import TicketDAO
from backend.ticket.models import Ticket


async def buy_ticket(lottery_id: int, money: int | None, user_id: int):
    lottery_data: Lottery = await LotteryDAO.find_by_id(lottery_id)
    count_ticket = await TicketDAO.count(lottery_id)
    profile_data: Profile = (await ProfileDAO.find_by_id(user_id))[0]
    statictics_data: Statistics = await StatisticsDAO.find_by_id(int(profile_data['statistics_id']))
    if money:
        if lottery_data.price_ticket * 2 == money:
            raise InvalidCoinsAmountException
        if statictics_data.money < lottery_data.price_ticket * 2:
            raise UnableToWithdrawCoinsException
        # Списание денег
        await StatisticsDAO.edit_money(statictics_data.id, money)
    last_ticker = await TicketDAO.last_ticket(lottery_id=lottery_id)
    if last_ticker == None:
        ticket_data: Ticket = await TicketDAO.add(0, lottery_id, user_id)
    else:
        ticket_data: Ticket = await TicketDAO.add(last_ticker+1, lottery_id, user_id)
    # Изменение призового фонда
    await LotteryDAO.add_accumulation(lottery_id)
    lottery_data: Lottery = await LotteryDAO.find_by_id(ticket_data.lottery_id)
    # Начисление бонуса за покупку
    await StatisticsDAO.add_money(statictics_data.id, int(lottery_data.price_ticket * 0.05))
    return {"detail": f"Билет успешно куплен. Номер вашего билета: {ticket_data.number}"}

async def trade_lose_ticket(id: int, user_id: int):
    ticket_data: Ticket = await TicketDAO.find_by_id(id)
    # Обработка ошибок
    if not ticket_data:
        raise TicketNotFoundException
    if not ticket_data.is_win:
        raise GameNotFinishedException
    if ticket_data.is_trade:
        raise TicketAlreadyRedeemedException
    lottery_data: Lottery = await LotteryDAO.find_by_id(ticket_data.lottery_id)
    # Изменение статуса торговли проигранного билета
    await TicketDAO.trade(ticket_data.id)
    # Изменение баланса
    await StatisticsDAO.add_money(user_id, int(lottery_data.accumulation * 0.025))
    return {"detail": "Обмен билета прошел успешно"}

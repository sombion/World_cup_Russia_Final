from datetime import datetime

from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates

from backend.achieving_the_goal.dao import AchievingTheGoalDAO
from backend.arcade.dao import InfoArcadeDAO
from backend.diceroll.dao import DiceRollDAO
from backend.profile.dao import ProfileDAO
from backend.auth.dependencies import get_current_user
from backend.auth.models import Users

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")

def updated_info_arcade (info_arcade):
    updated_info_arcade = []

    for i in range(0, len(info_arcade)):
        arcade = info_arcade[i]
        # Вычисление разницы
        delta = arcade['time_end'] - datetime.now()

        # Получение дней, часов и минут из разницы
        days = delta.days
        hours, remainder = divmod(delta.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        # Формирование результата в нужном формате
        if days > 0:
            result = f"{days} дн{'ей' if days % 10 in [2, 3, 4] else 'я'} {hours} часов до конца"
        else:
            result = f"{hours} часов {minutes} минут до конца"

        updated_arcade = dict(arcade)
        updated_arcade['time_end_now'] = result

        updated_info_arcade.append(updated_arcade)

    return updated_info_arcade

@router.get("/arcade")
async def index(request: Request, current_user: Users = Depends(get_current_user)):
    profile = (await ProfileDAO.find_by_id(current_user.id))[0]

    info_dice_roll = await DiceRollDAO.check_games(profile['id'])
    if info_dice_roll != []:
        info_dice_roll = info_dice_roll[0]

    info_achieving_the_goal = await AchievingTheGoalDAO.check_games(profile['id'], "achieving_the_goal")
    if info_achieving_the_goal != []:
        info_achieving_the_goal = info_achieving_the_goal[0]

    info_arcade = await InfoArcadeDAO.find_arcade()
    info_arcade = updated_info_arcade(info_arcade)

    return templates.TemplateResponse("arcade.html", {
        "request": request,
        "profile": profile,
        "info_dice_roll": info_dice_roll,
        "info_achieving_the_goal": info_achieving_the_goal,
        "info_arcade": info_arcade
    })


'''
{% if info_dice_roll != [] %}
{% else %}

{% if profile.ticket > 0 %}
<!-- Модальное окно подтверждения -->
<div id="confirmationModal" style="display:none;">
    <div class="modal-content">
        <p id="text-1">Вы уверены, что хотите начать испытани?</p>
		<p id="text-2">Стоимость испатания 1 билет</p>
		<div class="btn">
			<button onclick="confirmAction()" id="btn-enter">Подтвердить</button>
			<button onclick="cancelAction()">Отмена</button>
		</div>

    </div>
</div>
{% else %}
<!-- Модальное окно подтверждения -->
<div id="confirmationModal" style="display:none;">
    <div class="modal-content">
        <p id="text-1">Недостаточное кол-во билетов</p>
		<p id="text-2">Вы можете купить билет в магазине</p>
		<div class="btn">
			<button onclick="cancelAction()">Отмена</button>
		</div>
    </div>
</div>
{% endif %}

<script>
	function showConfirmationModal(url) {
		const modal = document.getElementById('confirmationModal');
		modal.style.display = 'flex';

		// Сохраняем URL для перехода
		modal.dataset.url = url;

		// Добавляем обработчик клика вне модального окна
		window.onclick = function(event) {
			if (event.target == modal) {
				cancelAction();
			}
		}
	}

	function confirmAction() {
		const modal = document.getElementById('confirmationModal');
		const url = modal.dataset.url;
		window.location.href = url;
	}

	function cancelAction() {
		const modal = document.getElementById('confirmationModal');
		modal.style.display = 'none';

		// Убираем обработчик клика вне модального окна
		window.onclick = null;
	}
</script>
{% endif %}
'''
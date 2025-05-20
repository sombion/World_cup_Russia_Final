# World_cup_Russia_Final

# Инструкция к запуску проекта
1) Создайте файл `.env` и заполнить его в соответствии с шаблоном
```
DB_HOST=
DB_PORT=
DB_USER=
DB_PASS=
DB_NAME=

SECRET_KEY=lZ/hfmj5lRkMdLyeO9aWFzqwU8L2neTs3Q0N/Xk4oGE=
ALGORITHM=HS256
```
2) Создайте файл `.env-non-dev`
```
DB_HOST=db_app
DB_PORT=1221
DB_USER=
DB_PASS=
DB_NAME=

SECRET_KEY=lZ/hfmj5lRkMdLyeO9aWFzqwU8L2neTs3Q0N/Xk4oGE=
ALGORITHM=HS256

POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=1569
```
3) Запустить команды
```
docker compose build
docker compose up
```


# Документация API

Этот документ описывает доступные API-эндпоинты проекта согласно спецификации OpenAPI.


## 1. Авторизация

### GET /api/auth/me
- **Теги:** Авторизация
- **Summary:** Api Get Me
- **Описание:** Просмотр данных о текущем пользователе

### POST /api/auth/register
- **Теги:** Авторизация
- **Summary:** Api Register User
- **Описание:** Регистрация
- **Тело запроса:** Требуется объект, соответствующий схеме `SUserRegister`

### POST /api/auth/login
- **Теги:** Авторизация
- **Summary:** Api Auth User
- **Описание:** Авторизация
- **Тело запроса:** Требуется объект, соответствующий схеме `SUserAuth`

### POST /api/auth/logout
- **Теги:** Авторизация
- **Summary:** Api Logout User
- **Описание:** Выход из записи

### PATCH /api/auth/edit-username
- **Теги:** Авторизация
- **Summary:** Api Edit Username
- **Описание:** Изменение имени
- **Тело запроса:** Требуется объект, соответствующий схеме `SEdinUsername`

### PATCH /api/auth/edit-password
- **Теги:** Авторизация
- **Summary:** Api Edit Username
- **Описание:** Изменение пароля
- **Тело запроса:** Требуется объект, соответствующий схеме `SEditPassword`

## 2. API admin

### PATCH /api/admin/update
- **Теги:** API admin
- **Summary:** Api Update Admin
- **Тело запроса:** Требуется объект, соответствующий схеме `SConfigAdmin`

### GET /api/admin/config
- **Теги:** API admin
- **Summary:** Api Config Admin

## 3. API лотереи

### GET /api/lottery/detail/{id}
- **Теги:** API лотереи
- **Summary:** Api Detail Lottery
- **Параметры:**
  - `id` (integer, required) - ID лотереи

### POST /api/lottery/create
- **Теги:** API лотереи
- **Summary:** Api Create Lottery
- **Тело запроса:** Требуется объект, соответствующий схеме `SCreateLottery`

### GET /api/lottery/all
- **Теги:** API лотереи
- **Summary:** Api All Lottery

## 4. API ticket

### GET /api/ticket/lottery/{lottery_id}
- **Теги:** API ticket
- **Summary:** Api Detail Ticket
- **Параметры:**
  - `lottery_id` (integer, required) - ID лотереи

### POST /api/ticket/buy
- **Теги:** API ticket
- **Summary:** Api Buy Ticket
- **Тело запроса:** Требуется объект, соответствующий схеме `SBuyTicket`

### POST /api/ticket/trade-lose
- **Теги:** API ticket
- **Summary:** Api Trade Lose Ticket
- **Тело запроса:** Требуется объект, соответствующий схеме `STradeLoseTicker`

## 5. Главная страница

### GET /
- **Теги:** Главная страница
- **Summary:** Index

### GET /api/cube-game/game
- **Теги:** API Главной страницы
- **Summary:** Role Dice

## 6. API улучшение скилов

### GET /skills
- **Summary:** Index

### GET /api/info-shop/
- **Теги:** API улучшение скилов
- **Summary:** List Up

### GET /api/info-shop/max
- **Теги:** API улучшение скилов
- **Summary:** Max Lvl

### POST /api/info-shop/buy-skill
- **Теги:** API улучшение скилов
- **Summary:** Buy Skill
- **Тело запроса:** Требуется объект, соответствующий схеме `SBuyModel`

## 7. АПИ броска кубика

### GET /arcade
- **Summary:** Index

### GET /diceroll
- **Summary:** Index

### POST /api/dice-roll/game
- **Теги:** АПИ броска кубика
- **Summary:** Api Games
- **Тело запроса:** Требуется объект, соответствующий схеме `SBaseStart`

### POST /api/dice-roll/start-game
- **Теги:** АПИ броска кубика
- **Summary:** Start Game

### POST /api/dice-roll/info-games
- **Теги:** АПИ броска кубика
- **Summary:** Info Games

### POST /api/dice-roll/check-ticket
- **Теги:** АПИ броска кубика
- **Summary:** Api Check Ticket

## 8. Другие API

### GET /right-way
- **Summary:** Right Way

### GET /reaction-check
- **Summary:** Game

### GET /achieving-the-goal
- **Summary:** Achieving The Goal

### POST /api/achieving-the-goal/games
- **Теги:** API для режима достижение цели
- **Summary:** Games

### POST /api/achieving-the-goal/info-games
- **Теги:** API для режима достижение цели
- **Summary:** Info Games

### POST /api/profile/info
- **Теги:** API профиля
- **Summary:** Api Profile Info

### POST /api/profile/time
- **Теги:** API профиля
- **Summary:** Api Profile Time

### Настройки который может изменять администратор
    {
        "price_ticket": 100,
        "minutes": 15,
        "price_mini_games": 50
    }
- price_ticket - Цена билета в рублях
- minutes - Задержка между созданием лотереи
- price_mini_games - Цена за мини-игру

### Правила игр
1 мини-игра "Бросок судьбы". Игрок выбирает 3 разных числа от 1 до 6 (например, 2, 4, 5). Бросается стандартный шестигранный кубик. Проверка выигрыша: Если выпавшее число совпадает с одним из трёх выбранных, игрок побеждает. Если выпавшее число не совпадает ни с одним из выбранных, игрок проигрывает. Пример: Выбраны числа: 1, 3, 6 Выпало 3 → Победа! Выпало 5 → Проигрыш.

2 мини-игра "Бросок кубиков". Игрок бросает три шестигранных кубика. Сумма выпавших значений записывается. Если сумма ≥ загаданному числу → победа. Если сумма < загаданного числа → поражение

Игра "Кубик" заключается в бросании кубика и получении бонусов в зависимости от грани, которая выпала. Бонусы, которые можно получить : монетки, опыт и рубин. Например, на кубике выпадает грань "3", значит игрок получит 3 монетки, 3 опыта, а вероятность выпадения рубина изначально ровняется 5%.

Админ может изменять данные в следующих файлах:
В файле admin_info.json содержаться  цена билета для первой игры, длительность тиража, цена для второй игры.
В файле info_achieving_the_goal.json содержаться данные для мини-игры “Бросок кубиков”: уровень игры, сколько пользователь получит опыта,  сколько пользователь получит рубинов,   сколько пользователь получит кубиков.
В файле info_dice_roll.json содержаться данные для мини-игры “Бросок судьбы”: уровень игры, сколько пользователь получит опыта,  сколько пользователь получит рубинов,   сколько пользователь получит кубиков.
В файле info_xp.json содержиться информацию об уровне и сколько нужно опыта, чтобы его получить
В файле skill_shop_info.json содержиться “магазин” прокачки, в котором содержаться названия на русском языке различных улучшения: Шанс выпадения больше 3,Шанс не потратить кубик,Шанс получить х2 монет за выпадение, Шанс выпадения рубина,Количество кубиков при AFK.  Также есть названия на английскому языке, уровень и цена прокачки улучшения.
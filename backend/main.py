from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.auth.router import router as auth_router
from backend.admin.router import router as admin_router
from backend.lottery.router import router as lottery_router
from backend.ticket.router import router as ticket_router

from fastapi.staticfiles import StaticFiles

from backend.page.home import router as router_home_page
from backend.cubegame.router import router as router_cube_game_api

from backend.page.skills import router as router_skills_page
from backend.skillshop.router import router as router_skill_shop_api

from backend.page.arcade import router as router_arcade_page
from backend.page.diceroll import router as router_dice_roll_page
from backend.diceroll.router import router as router_dice_roll_api
from backend.page.rightway import router as router_right_way_page
from backend.page.achieving_the_goal import router as router_achieving_the_goal
from backend.achieving_the_goal.router import router as router_achieving_the_goal_api
from backend.page.reactioncheck import router as router_reaction_check_page

from backend.profile.router import router as router_profile_api

app = FastAPI()


app.include_router(auth_router)
app.include_router(admin_router)
app.include_router(lottery_router)
app.include_router(ticket_router)

app.include_router(router_home_page)
app.include_router(router_cube_game_api)
app.include_router(router_skills_page)
app.include_router(router_skill_shop_api)
app.include_router(router_arcade_page)
app.include_router(router_dice_roll_page)
app.include_router(router_dice_roll_api)
app.include_router(router_right_way_page)
app.include_router(router_reaction_check_page)
app.include_router(router_achieving_the_goal)
app.include_router(router_achieving_the_goal_api)
app.include_router(router_profile_api)


origins = [
    "http://localhost:5500",
    "http://127.0.0.1:5500",
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers",
                   "Access-Control-Allow-Origin", "Authorization"],
)
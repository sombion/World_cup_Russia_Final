from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates

from backend.profile.dao import ProfileDAO
from backend.shop.shop import my_shop
from backend.auth.dependencies import get_current_user
from backend.auth.models import Users

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get("/shop")
async def index(request: Request, current_user: Users = Depends(get_current_user)):
    profile = (await ProfileDAO.find_by_id(current_user.id))[0]
    items_shop = (await my_shop.shop_create_and_list(current_user.id))["shop_items"]
    return templates.TemplateResponse("shop.html", {"request": request, "profile": profile, "items_shop": items_shop})
from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates

from backend.profile.dao import ProfileDAO
from backend.auth.dependencies import get_current_user
from backend.auth.models import Users

router = APIRouter()

templates = Jinja2Templates(directory="backend/templates")


@router.get("/reaction-check")
async def game(request: Request, current_user: Users = Depends(get_current_user)):
    profile = (await ProfileDAO.find_by_id(current_user.id))[0]
    return templates.TemplateResponse("reactioncheck.html", {"request": request, "profile": profile})
from fastapi import APIRouter, Depends

from backend.admin.dao import AdminInfoDAO
from backend.admin.schemas import SConfigAdmin
from backend.auth.dependencies import get_admin_user
from backend.auth.models import Users

router = APIRouter(
    prefix="/api/admin",
    tags=["API admin"]
)

@router.patch("/update")
async def api_update_admin(config_data: SConfigAdmin):
    return await AdminInfoDAO.update(config_data.price_ticket, config_data.minutes)

@router.get("/config")
async def api_config_admin(current_user: Users = Depends(get_admin_user)):
    return await AdminInfoDAO.find_all()
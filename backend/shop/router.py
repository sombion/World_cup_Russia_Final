from fastapi import APIRouter
from pydantic import BaseModel

from backend.shop.shop import my_shop

router = APIRouter(
	prefix="/api/shop",
	tags=["API магазина"]
)

class SBuyModel(BaseModel):
    id_item: int
    tg_id: str = "1076663484"


@router.post("/create_shop")
async def api_create_money(tg_id: str = "1076663484"):
    result = await my_shop.shop_create_and_list(tg_id)
    return result


@router.post("/shop-list")
async def api_create_money(tg_id: str = "1076663484"):
    result = await my_shop.shop_create_and_list(tg_id)
    return result


@router.post('/buy')
async def api_buy(buy_model: SBuyModel):
    result = await my_shop.shop_buy_item(buy_model.id_item, buy_model.tg_id)
    return result
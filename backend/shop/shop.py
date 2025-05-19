from datetime import datetime
import random

from backend.profile.dao import ProfileDAO
from backend.shop.dao import BuyShopDAO, InfoShopDAO

class Shop:

	async def shop_create_and_list(self, user_id: int):
		time = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
		id_profile = await ProfileDAO.find_id_from_id(user_id)

		new_shop = await BuyShopDAO.find_shop_by_date(id_profile, time)
		if len(new_shop) < 6:
			all_shop_item = await InfoShopDAO.find_all()

			target_id = [item["id"] for item in all_shop_item]
			target_change = [item["chance"] for item in all_shop_item]
			for i in range(6):
				x = random.choices(target_id, target_change)[0]
				id_change = target_id.index(x)
				target_id.remove(x)
				target_change.pop(id_change)
				await BuyShopDAO.create_shop(id_profile, x, all_shop_item[x-1]['count'])
			new_shop = await BuyShopDAO.find_shop_by_date_list(id_profile, time)
			return {"status": 200, "info": "магазин обновлен", "shop_items": new_shop}
		else:
			new_shop = await BuyShopDAO.find_shop_by_date_list(id_profile, time)
			return {"shop_items": new_shop}

	async def shop_buy_item(self, id_item: int, user_id: int):
		shop_list = await self.shop_create_and_list(user_id)

		time = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
		profile = (await ProfileDAO.find_by_id(user_id))[0]
		id_profile = await ProfileDAO.find_id_from_id(user_id)
		one_item = await BuyShopDAO.find_item_in_shop(id_profile, time, id_item)
		item = await InfoShopDAO.find_by_id(id_item)
		print(time)

		if one_item != []:
			one_item = one_item[0]
		else:
			return {"status": 500, "error": "error"}

		if one_item["count_by"] <= 0:
			return {"status": 400, "info": "Предметы куплены"}

		if item.title_item.count("ticket") == 1:
			title_item, count = item.title_item.split("_")
			if profile['money'] >= item.price:
				await BuyShopDAO.reduction_money(profile, int(item.price))
				await BuyShopDAO.buy_ticket(profile, int(count))
				await BuyShopDAO.reduction_count(one_item['id'])
				return {"status": 200, "one_item": one_item}
			else:
				return {"status": 402, "error": "Недостаточно монет"}

		if item.title_item.count("ruby") == 1:
			title_item, count = item.title_item.split("_")
			if profile['money'] >= item.price:
				await BuyShopDAO.reduction_money(profile, int(item.price))
				await BuyShopDAO.buy_ruby(profile, int(count))
				await BuyShopDAO.reduction_count(one_item['id'])
				return {"status": 200}
			else:
				return {"status": 402, "error": "Недостаточно монет"}
		return item

my_shop = Shop()
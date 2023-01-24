from datetime import datetime
import random
from typing import Literal

from database.database import db
from texts.texts_ru import TEXTS_RU


def open_shop(shop_id: int, date_time: datetime) -> datetime:
    shop = db.get_shop(shop_id=shop_id)
    shop.open_datetime = date_time
    return shop.open_datetime

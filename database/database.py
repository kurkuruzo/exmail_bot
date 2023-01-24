from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from enum import Enum
from dataclasses import dataclass
from datetime import datetime
from typing import Optional


class GeneralState(StatesGroup):
    SHOP_OPEN_CLOSE = State()


class OpenState(StatesGroup):
    SHOP_NUMBER_REQUESTED = State()
    SHOP_ADDRESS_CONFIRMATION_REQUESTED = State()
    GEOPOSITION_REQUESTED = State()


class CloseState(StatesGroup):
    SHOP_NUMBER_REQUESTED = State()
    SHOP_ADDRESS_CONFIRMATION_REQUESTED = State()
    GEOPOSITION_REQUESTED = State()


Coordinates = tuple[float, float]


@dataclass
class User:
    id: int
    name: Optional[str] = None


@dataclass(slots=True)
class Shop:
    id: int
    address: str
    coords: Coordinates
    open_datetime: Optional[datetime] = None
    close_datetime: Optional[datetime] = None


@dataclass(slots=True)
class Database:
    users: Optional[dict[int, User]] = None
    shop_statuses: Optional[dict[int, Shop]] = None

    def get_shop(self, shop_id: int):
        return self.shop_statuses.get(shop_id)

    def get_user(self, user_id: int):
        return self.users.get(user_id)


def init_db() -> Database:
    db = Database()
    db.users = {}
    db.shop_statuses = {}
    return db


db = init_db()
shop = Shop(1, "ул. Ленина", (56.0, 43.0))
user = User(51531741, "MK")
db.shop_statuses[shop.id] = shop
db.users[user.id] = user

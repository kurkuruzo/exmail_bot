from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from texts.texts_ru import TEXTS_RU

main_shop_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
manage_shop_btn = KeyboardButton(TEXTS_RU.manage_shop_btn)
cancel_shop_btn = KeyboardButton(TEXTS_RU.cancel_btn)
main_shop_kb.add(manage_shop_btn, cancel_shop_btn)

manage_shop_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
open_btn = KeyboardButton(TEXTS_RU.open_btn)
close_btn = KeyboardButton(TEXTS_RU.close_btn)
manage_shop_kb.add(open_btn, close_btn)

address_confirmation_kb = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True
)
yes_btn = KeyboardButton(TEXTS_RU.yes_btn)
no_btn = KeyboardButton(TEXTS_RU.no_btn)
address_confirmation_kb.add(yes_btn, no_btn)


geo_request_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
geo_request_btn = KeyboardButton(
    TEXTS_RU.geolocation_request_btn, request_location=True
)
geo_request_kb.add(geo_request_btn)

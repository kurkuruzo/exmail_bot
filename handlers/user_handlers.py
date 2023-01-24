from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from datetime import datetime

import logging

import config_data.config as config
from database.database import db, User, GeneralState, OpenState, CloseState, Shop
from handlers.other_handlers import send_answer
from keyboards.shop_kb import (
    main_shop_kb,
    manage_shop_kb,
    address_confirmation_kb,
    geo_request_kb,
)
import services.services as services
from texts.texts_ru import TEXTS_RU

logger = logging.getLogger(__name__)


async def process_start_command(message: Message):
    await message.answer(TEXTS_RU.start_message, reply_markup=manage_shop_kb)
    await GeneralState.SHOP_OPEN_CLOSE.set()


async def process_open_shop(message: Message, state: FSMContext):
    user = db.get_user(message.from_user.id)
    await send_shop_number_request(message, state)
    await OpenState.SHOP_NUMBER_REQUESTED.set()


async def send_shop_number_request(message: Message, state: FSMContext):
    await message.answer(TEXTS_RU.request_shop_number_message)


async def process_shop_number(message: Message, state: FSMContext):
    shop = await check_shop_number(message, state)
    await message.answer(
        TEXTS_RU.address_confirmation_message.format(
            operation="открыть", address=shop.address
        ),
        reply_markup=address_confirmation_kb,
    )
    await OpenState.SHOP_ADDRESS_CONFIRMATION_REQUESTED.set()


async def check_shop_number(message: Message, state: FSMContext):
    try:
        shop_id = int(message.text)
        async with state.proxy() as data:
            data["shop_id"] = shop_id
    except Exception as e:
        logger.exception(e)
        return await send_shop_not_found(message)
    else:
        shop = db.get_shop(shop_id=shop_id)
        return shop


async def process_address_confirmation(message: Message, state: FSMContext):
    if message.text == TEXTS_RU.yes_btn:
        await send_geolocation_request(message, state)
        await OpenState.GEOPOSITION_REQUESTED.set()


async def send_geolocation_request(message: Message, state: FSMContext):
    await message.answer(
        TEXTS_RU.geolocation_request_message, reply_markup=geo_request_kb
    )


async def process_geolocation(message: Message, state: FSMContext):
    data = await state.get_data()
    shop_id = data["shop_id"]
    shop = db.get_shop(shop_id)
    open_datetime = services.open_shop(shop_id, date_time=datetime.now())
    await message.answer(
        TEXTS_RU.shop_opened_message.format(
            address=shop.address,
            datetime=open_datetime.strftime(config.load_config().datetime_format),
        )
    )


async def send_user_not_found(message: Message):
    await message.answer(
        TEXTS_RU.user_not_found_message.format(user_id=message.from_user.id)
    )


async def send_shop_not_found(message: Message):
    await message.answer(TEXTS_RU.shop_not_found_message.format(message.text))


async def process_help_command(message: Message):
    await message.answer(TEXTS_RU.help_message)


def register_user_handlers(dp: Dispatcher):
    dp.register_message_handler(process_start_command, commands="start")
    dp.register_message_handler(process_help_command, commands="help")
    dp.register_message_handler(process_open_shop, state=GeneralState.SHOP_OPEN_CLOSE)
    dp.register_message_handler(
        process_shop_number, state=OpenState.SHOP_NUMBER_REQUESTED
    )
    dp.register_message_handler(
        process_address_confirmation,
        Text(equals=[TEXTS_RU.yes_btn, TEXTS_RU.no_btn]),
        state=OpenState.SHOP_ADDRESS_CONFIRMATION_REQUESTED,
    )
    dp.register_message_handler(
        process_geolocation,
        content_types=["location"],
        state=OpenState.GEOPOSITION_REQUESTED,
    )

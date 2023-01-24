from aiogram import Dispatcher
from aiogram.types import Message
import logging

from texts.texts_ru import TEXTS_RU

logger = logging.getLogger(__name__)


async def send_answer(message: Message):
    await message.answer(text=TEXTS_RU.other_answer)


async def debug_handler(message: Message):
    logger.debug(message)


def register_other_handlers(dp: Dispatcher):
    # dp.register_message_handler(send_answer)
    dp.register_message_handler(debug_handler)

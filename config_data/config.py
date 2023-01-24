from dataclasses import dataclass
import os
from typing import Optional
from dotenv import load_dotenv

load_dotenv()


@dataclass(slots=True)
class TgBot:
    token: str


@dataclass(slots=True)
class Config:
    tg_bot: TgBot
    admins: Optional[list] = None
    datetime_format: str = "%H:%M:%S %d.%m.%Y"


def load_config() -> Config:
    return Config(tg_bot=TgBot(token=os.environ["BOT_TOKEN"]))

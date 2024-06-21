from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

import asyncio

from . import game_bot as gb
from .config import *


def start_game_bot():
    bot_game = Bot(token=TOKEN_BOT_GAME, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    asyncio.run(gb.start_bot()(bot_game))
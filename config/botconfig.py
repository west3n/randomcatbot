import logging

from aiogram import Dispatcher, types
from decouple import config

from handlers.commands import register as reg_handlers
from handlers.callbacks import register as reg_callbacks
from handlers.alert import register as reg_alert


bot_token = config("BOT_TOKEN")
logger = logging.getLogger(__name__)
cat_jpg = 'https://api.thecatapi.com/v1/images/search?mime_types=jpg'
cat_gif = 'https://api.thecatapi.com/v1/images/search?mime_types=gif'


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("cat", "Grab a cat!")
    ])


def register_handlers(dp: Dispatcher):
    reg_handlers(dp)
    reg_callbacks(dp)
    reg_alert(dp)

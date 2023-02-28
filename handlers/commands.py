import aiohttp

from aiogram import Dispatcher, types
from keyboards import inline
from config import botconfig


async def bot_start(msg: types.Message):
    await msg.delete()
    name = msg.from_user.first_name
    caption = f"Hello, {name}! Here's your cat! 🐈"
    async with aiohttp.ClientSession() as session:
        async with session.get(botconfig.cat_jpg) as response:
            data = await response.json()
            cat_image_url = data[0]['url']
    await msg.bot.send_photo(chat_id=msg.from_user.id, photo=cat_image_url,
                             caption=caption, reply_markup=inline.more_cat())


def register(dp: Dispatcher):
    dp.register_message_handler(bot_start, commands='start', state='*')

from aiogram import Dispatcher, types
import aiohttp
from config import botconfig


async def alert(msg: types.Message):
    await msg.delete()
    async with aiohttp.ClientSession() as session:
        async with session.get(botconfig.cat_jpg) as response:
            data = await response.json()
            cat_image_url = data[0]['url']
    await msg.bot.send_photo(chat_id=msg.from_user.id, photo=cat_image_url)
    await msg.answer("Use buttons, dear 🐱")


def register(dp: Dispatcher):
    dp.register_message_handler(alert, content_types=["text", "animation", "photo", "document", "location", "sticker"])

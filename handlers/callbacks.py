import aiohttp

from aiogram import types, Dispatcher
from config import botconfig
from keyboards import inline


async def callback_data(call: types.CallbackQuery):
    call_format = call.data
    if call_format == 'jpg':
        async with aiohttp.ClientSession() as session:
            async with session.get(botconfig.cat_jpg) as response:
                data = await response.json()
                cat_image_url = data[0]['url']
        await call.bot.send_photo(chat_id=call.from_user.id,
                                  photo=cat_image_url,
                                  reply_markup=inline.more_cat())
    elif call_format == 'gif':
        async with aiohttp.ClientSession() as session:
            async with session.get(botconfig.cat_gif) as response:
                data = await response.json()
                cat_image_url = data[0]['url']
        await call.bot.send_animation(chat_id=call.from_user.id,
                                      animation=cat_image_url,
                                      reply_markup=inline.more_cat())
    await call.bot.answer_callback_query(call.id)


def register(dp: Dispatcher):
    dp.register_callback_query_handler(callback_data,
                                       lambda query: query.data in ['jpg', 'gif'])

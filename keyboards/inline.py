from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def more_cat() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('More cats!', callback_data='jpg')],
        [InlineKeyboardButton('More animated cats!', callback_data='gif')]
    ])
    return kb

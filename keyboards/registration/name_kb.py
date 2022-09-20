from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def set_name_kb(name):
    name_surname_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=name, callback_data=name)
            ]
        ], resize_keyboard=True, one_time_keyboard=True
    )
    return name_surname_kb
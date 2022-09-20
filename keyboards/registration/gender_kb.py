from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

gender_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Мужчина', callback_data='1'),
            InlineKeyboardButton(text='Женщина', callback_data='0')
        ]
    ], resize_keyboard=True, one_time_keyboard=True
)
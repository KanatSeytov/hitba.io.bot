from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

accept = 'Я согласен'

accept_kb = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text=accept, callback_data='registration')
        ]
    ], resize_keyboard=True, one_time_keyboard=False
)


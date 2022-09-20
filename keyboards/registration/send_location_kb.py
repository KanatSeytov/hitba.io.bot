from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


send_location_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🕹 Share with GEO', request_location=True)
        ]
    ], resize_keyboard=True, one_time_keyboard=True
)
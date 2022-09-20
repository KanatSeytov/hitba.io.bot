from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data import marriage_statuses
from utils.registration import generate_keyboard

marriage_plan_kb = InlineKeyboardMarkup(
    inline_keyboard=generate_keyboard(marriage_statuses), resize_keyboard=True, one_time_keyboard=True
)
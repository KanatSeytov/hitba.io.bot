from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data import has_children_statuses
from utils.registration import generate_keyboard

has_children_kb = InlineKeyboardMarkup(
    inline_keyboard=generate_keyboard(has_children_statuses), resize_keyboard=True, one_time_keyboard=True
)
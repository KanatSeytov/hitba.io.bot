from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils.registration import generate_keyboard
from data import m_statuses, f_statuses

def generate_keyboard(statuses):
    return [[InlineKeyboardButton(text=status, callback_data=status)] for status in statuses]

family_status_m_kb = InlineKeyboardMarkup(
    inline_keyboard=generate_keyboard(m_statuses),
    resize_keyboard=True, one_time_keyboard=True
)

family_status_f_kb = InlineKeyboardMarkup(
    inline_keyboard=generate_keyboard(f_statuses), 
    resize_keyboard=True, one_time_keyboard=True
)
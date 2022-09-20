from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import dp
from states import Registration 
from utils.registration import validation
from keyboards import has_children_kb, marriage_plan_kb
from data import has_children_statuses

@dp.message_handler(Command('cancel'),state=Registration.children)
async def cancel_get_name(message: Message, state: FSMContext):
    pass

@dp.message_handler(state=Registration.children)
async def get_name(message: Message, state: FSMContext):
    has_children = message.text
    if has_children not in has_children_statuses:
        await message.answer('Введите правильный статус\nесли хотите прервать регистрацию, нажмите /cancel')
        return
    await state.update_data(children=has_children)
    await message.answer('Есть ли у вас дети?', reply_markup=has_children_kb)
    await Registration.next()

@dp.callback_query_handler(state=Registration.children)
async def get_family_status(callback: CallbackQuery, state: FSMContext):
    has_children = callback.data

    if has_children not in has_children_statuses:
        await callback.answer('Введите правильный статус\nесли хотите прервать регистрацию, нажмите /cancel')
        return
    await state.update_data(children=has_children)
    
    await callback.message.answer('Планы относительно брака?')
    # await Registration.next()


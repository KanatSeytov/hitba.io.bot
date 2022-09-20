from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from loader import dp
from states import Registration 
from keyboards import has_children_kb
from keyboards import f_statuses, m_statuses

@dp.message_handler(Command('cancel'),state=Registration.family_status)
async def cancel_get_name(message: Message, state: FSMContext):
    pass

@dp.message_handler(state=Registration.family_status)
async def get_name(message: Message, state: FSMContext):
    family_status = message.text
    if family_status not in (m_statuses+f_statuses):
        await message.answer('Введите правильный статус\nесли хотите прервать регистрацию, нажмите /cancel')
        return
    await state.update_data(family_status=family_status)
    await message.answer('Есть ли у вас дети?', reply_markup=has_children_kb)
    await Registration.next()

@dp.callback_query_handler(state=Registration.family_status)
async def get_family_status(callback: CallbackQuery, state: FSMContext):
    family_status = callback.data

    if family_status not in (m_statuses+f_statuses):
        await callback.answer('Введите правильный статус\nесли хотите прервать регистрацию, нажмите /cancel')
        return
    await state.update_data(family_status=family_status)
    
    await callback.message.answer('Есть ли у вас дети?', reply_markup=has_children_kb)
    await Registration.next()


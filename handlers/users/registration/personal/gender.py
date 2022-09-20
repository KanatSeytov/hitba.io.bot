from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram_calendar import dialog_cal_callback, DialogCalendar
from aiogram.types import Message, CallbackQuery
from loader import dp
from states import Registration

# @dp.message_handler(Command('cancel'), state=Registration.gender)
# async def cancel_get_gender(message: Message, state: FSMContext):
#     await cancel_registration(state, message)
#     return
@dp.callback_query_handler(state=Registration.gender)
async def start_registration(callback: CallbackQuery, state: FSMContext):

    genders = ['1', '0']
    gender = callback.data
    if gender not in genders:
        await callback.message.answer('Укажите свой пол корректно\nесли хотите прервать регистрацию, нажмите /cancel')
        return
    # send data to next stae
    await state.update_data(gender=gender)
    await callback.message.delete()
    # await callback.message.delete_reply_markup()  


    await callback.message.answer('Ваша дата рождения', reply_markup = await DialogCalendar().start_calendar())
    await Registration.next()


@dp.message_handler(state=Registration.gender)
async def get_gender(message: Message, state: FSMContext):
    genders = ['Мужчина', 'Женщина']
    gender = message.text
    print(gender)
    print(gender not in genders)
    if gender not in genders:
        await message.answer('Укажите свой пол корректно\nесли хотите прервать регистрацию, нажмите /cancel')
        return
    # send data to next stae
    if gender == genders[0]:
        g = '1'
    else:
        g = '0'
    await state.update_data(gender=g)


    await message.answer('Ваша дата рождения', reply_markup = await DialogCalendar().start_calendar())
    await Registration.next()
    

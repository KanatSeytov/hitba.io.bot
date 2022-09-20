from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram_calendar import dialog_cal_callback, DialogCalendar
from loader import dp
from utils.registration import date_to_age, cancel_registration, incorrect_age
from states import Registration 
from keyboards import send_location_kb

# dialog calendar usage
@dp.callback_query_handler(dialog_cal_callback.filter(), state=Registration.birthday)
async def process_dialog_calendar(callback_query: CallbackQuery, callback_data: dict, state: FSMContext):
    selected, birth_date = await DialogCalendar().process_selection(callback_query, callback_data)
    if not selected:
        return
    age = date_to_age(birth_date)
    text = incorrect_age(age)

    if text == 'old':
        await callback_query.message.answer(
            'Введите свой реальный возраст\nесли хотите прервать регистрацию, нажмите /cancel'
        )
    elif text == 'young':
        await callback_query.message.answer('Извините, но вы слишком молоды для нас, приходите, когда вам исполнится 18!', reply_markup=ReplyKeyboardRemove(selective=False))
        await callback_query.answer()
        await state.finish()
        return
    await state.update_data(birthday=birth_date)
    
    await callback_query.message.answer('От куда вы?', reply_markup=send_location_kb)
    await callback_query.answer()
    await Registration.next()


@dp.message_handler(Command('cancel'), state=Registration.birthday)
async def cancel_get_age(message: Message, state: FSMContext):
    await cancel_registration(state, message)


@dp.message_handler(state=Registration.birthday)
async def get_age(message: Message, state: FSMContext):
    # if user press continue button, his data become empty
    text = message.text
    await message.answer('сначала введите дату')
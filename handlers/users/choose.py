from cgitb import text
from datetime import datetime
from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from loader import dp, db

from filters import IsPrivate
from states import Registration
from utils.misk import rate_limit
from utils.registration import read_file, validation
from keyboards import accept_kb, set_name_kb

start_text = 'Вы начали регистрацию\nВаше имя'
 
@rate_limit(limit=3)
@dp.message_handler(IsPrivate(), Command('choose'))
async def command_start(message: types.Message):
    uid = message.from_user.id
    application_exist, gender = await create_application(uid)
    if application_exist:
        await message.answer('Вы уже отправили свою анкету, пожалуйста, дождитесь рекомендации от администраторов')
    await message.answer('Ваша заявка принята, дождитесь, пока администраторы найдут вам подходящую пару')
    pair_id = await find_pair(id, gender)
    if pair_id:
        await delete_application(pair_id)
        await send_message(pair_id, message, f'вы образовали пару с {message.from_user.first_name}')
        await send_message(pair_id, message, f'вы образовали пару с {message.from_user.first_name}')
        await create_match({
            gender: uid,
            '1' if int(gender)==0 else '0': pair_id,
            'match_date': datetime.now()
        })
        return
    await message.answer('Извините, сейчас мы не можем найти вам пару, когда пара появится, мы сообщим вам')

# create active applicaiton for looking for a pair
async def create_application(id):
    gender = (await db.select_user(id))['gender']
    if gender == '1':
        table = 'males_applications'
    else:
        table = 'females_applications'
    try:
        await db.create_application({
            '_id': id,
            'application_date': datetime.now()
        }, table)
        return True, gender
    except:
        return False, gender

# select all users with vise gender and put them in recommend
async def find_pair(id, gender):
    if gender=='1':
        users = await db.select_all_female_applications()
    else:
        users = await db.select_all_male_applications()
    recommend_id = recommend(id, users)
    return recommend_id

# if we'll add recommendation, it will be here
def recommend(id, users):
    for potential_match in users:
        return potential_match['_id']
    
async def delete_application(uid):
    gender = (await db.select_user(uid))['gender']
    if gender == '1':
        await db.delete_application(uid, 'males_applications')
    else:
        await db.delete_application(uid, 'female_applicaitons')


async def send_message(id, message: types.Message, text: str):
    await message.answer(id, text=text)


async def create_match(match):
    await db.create_match(match=match)
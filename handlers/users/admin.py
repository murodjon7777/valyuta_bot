import asyncio
from states.relama import Reklama
from aiogram.dispatcher import FSMContext
from aiogram import types

from data.config import ADMINS
from loader import dp, db, bot

@dp.message_handler(text="/allusers", user_id=ADMINS)
async def get_all_users(message: types.Message):
    users = db.select_all_users()
    print(users[0][0])
    await message.answer(users)
    # await bot.send_message(
    #     chat_id=ADMINS[0],
    #     text = f"Active {active} Unactive: {unactive}"
    # )

@dp.message_handler(text="/reklama", user_id=ADMINS)
async def rek(message:types.Message):
    await Reklama.reklama.set()
@dp.message_handler(state=Reklama.reklama,user_id=ADMINS)
async def send_ad_to_all(message: types.Message,state=FSMContext):
    users = db.select_all_users()
    text1=message.text
    active=0
    unactive=0
    for user in users:
        try:
            user_id = user[0]
            await bot.send_message(chat_id=user_id, text=text1)
            await asyncio.sleep(0.05) 
            active+=1
        except:
            unactive+=1
    await bot.send_message(
        chat_id=ADMINS[0],
        
        text = f"Active {active} Unactive: {unactive}"
    )
    await state.finish()
@dp.message_handler(text="/active",user_id=ADMINS)
async def send_ad_to_all(message: types.Message):
    users = db.select_all_users()
    active=0
    unactive=0
    for user in users:
        try:
            user_id = user[0]
            await bot.send_message(chat_id=user_id, text="")
            await asyncio.sleep(0.05)
            active+=1
        except:
            unactive+=1
    await bot.send_message(
        chat_id=ADMINS[0],
        text = f"Active {active} Unactive: {unactive}"
    )
    

@dp.message_handler(text="/cleandb", user_id=ADMINS)
async def get_all_users(message: types.Message):
    db.delete_users()
    await message.answer("Baza tozalandi!")
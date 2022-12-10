from email import message
from gettext import translation
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart,Command
from googletrans import Translator
from states.personalData import PersonalData
from loader import dp
from aiogram.dispatcher import FSMContext
from keyboards.default.Keyboard import menu
from keyboards.default.settings import setting
from deep_translator import GoogleTranslator, YandexTranslator
tar={
    "🇺🇿Uzbek":"uzbek",
    "🇷🇺Russian":"russian",
    "🇬🇧English":"english",
    "🇫🇷French":"french",
    "🇩🇪German":"german",
    "🇸🇦Arabic":"arabic",
    "🇰🇷Korean":"korean",
    "🇮🇹Italian":"italian",
    "🇪🇸Spanish":"spanish",
    "🇹🇷Turkish":"turkish",
    "🇰🇷Korean":"korean",
    "🇯🇵Japan":"japanese",
    "🇨🇳China":"zh-TW",
}
@dp.message_handler(text="Tilni sozlash")
async def til(message:types.Message):
    
        await message.answer("Qaysi tildan",reply_markup=menu)
        await PersonalData.tildan.set()
    
@dp.message_handler(state=PersonalData.tildan)
async def tildan(message:types.Message,state=FSMContext):
    if types.Message!="/start":
        dan=tar[f"{message.text}"]
        
        await state.update_data({"tildan":dan} )
        await message.answer("Qaysi tilga",reply_markup=menu)
        await PersonalData.next()
    else:
        await state.finish()
@dp.message_handler(state=PersonalData.tilga)
async def tilga(message:types.Message,state=FSMContext ):
    if types.Message!="/start":
        ga=tar[f"{message.text}"]
        await state.update_data({"tilga":ga})
        await message.answer("matn kiriting",reply_markup=setting)
        await PersonalData.next()  
    else:
        await state.finish()
@dp.message_handler(state=PersonalData.matn)
async def matn(message:types.Message, state=FSMContext):
    matn=message.text
    if matn=="/start":{ await state.finish(), await message.reply_markup(setting)}
    if matn=="Tilni sozlash":{   await PersonalData.tildan.set(),
                     await message.answer("Tildan tarjima qilish kerak",reply_markup=menu)}
    else: await state.update_data(
        {"matn":matn}
    )    
    #  await message.answer(f"{}")
    data =await state.get_data()
    td=data.get("tildan")
    tg=data.get("tilga")
    tm=data.get("matn")

    
    # await message.answer(f"{td}--{tg}--{tm} ")
    # translator=Translator()
    # res=translator.translate(tm,dest=tg,src=td)
    
    rest=GoogleTranslator(source=td,target=tg).translate(tm)
    if matn!="Tilni sozlash" and matn!="/start":await message.answer(f"{td} -> {tg}\n\n{rest}")
    # print(rest)
    # await message.answer(f"salok")
    
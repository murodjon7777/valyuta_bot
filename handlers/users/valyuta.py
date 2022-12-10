import requests
from aiogram import types
from loader import dp
url=f"https://cbu.uz/uz/arkhiv-kursov-valyut/json/"
r= requests.get(url)
r=r.json()
print(r[0]["id"])
usd=r[0]["Rate"]
rubl=r[2]["Rate"]
eur=r[1]["Rate"]



@dp.message_handler(text="valyuta")
async def valyuta(message:types.Message):
    # await message.answer(text=f'{rubl}')
    text1=f"1dollar  {usd} so'm\n 1yeuro   {eur} so'm\n 1rubl  {rubl} so'm\n"
    print(text1)
    await message.answer(text=f"{r[0]['CcyNm_UZ']}\n1{r[0]['Ccy']}={usd} so\'m   o\'zgarish {r[0]['Diff']}so\'m \n"
                         f"{r[1]['CcyNm_UZ']}\n{r[0]['Ccy']}={eur} so\'m  o\'zgarish {r[1]['Diff']}so\'m\n"
                         f"{r[2]['CcyNm_UZ']}\n{r[0]['Ccy']}= {rubl} so\'m  o\'zgarish {r[2]['Diff']}so\'m\n"
                         f"🕒 Sana {r[0]['Date']}"
                         f"🤖 @valyutaa1bot - Markaziy bank valyuta kurslari")
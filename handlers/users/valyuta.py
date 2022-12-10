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
    await message.answer(text=f"🇺🇸{r[0]['CcyNm_UZ']}\n1 {r[0]['Ccy']}={r[0]['Rate']} so\'m   o\'zgarish {r[0]['Diff']}so\'m \n\n"
                         f"🇪🇺{r[1]['CcyNm_UZ']}\n1 {r[1]['Ccy']}={r[1]['Rate']} so\'m  o\'zgarish {r[1]['Diff']}so\'m\n\n"
                         f"🇷🇺{r[2]['CcyNm_UZ']}\n1 {r[2]['Ccy']}= {r[2]['Rate']} so\'m  o\'zgarish {r[2]['Diff']}so\'m\n\n"
                         f"🇬🇧{r[3]['CcyNm_UZ']}\n1 {r[3]['Ccy']}={r[2]['Rate']} so\'m  o\'zgarish {r[3]['Diff']}so\'m\n\n"
                         f"🇯🇵{r[4]['CcyNm_UZ']}\n1 {r[4]['Ccy']}={r[4]['Rate']} so\'m  o\'zgarish {r[4]['Diff']}so\'m\n\n"
                         f"🇨🇳{r[14]['CcyNm_UZ']}\n1 {r[14]['Ccy']}={r[14]['Rate']} so\'m  o\'zgarish {r[14]['Diff']}so\'m\n\n"
                         f"🇨🇭{r[13]['CcyNm_UZ']}\n1 {r[13]['Ccy']}= {r[13]['Rate']} so\'m  o\'zgarish {r[13]['Diff']}so\'m\n\n"
                         f"🇹🇷{r[66]['CcyNm_UZ']}\n1 {r[66]['Ccy']}= {r[66]['Rate']} so\'m  o\'zgarish {r[66]['Diff']}so\'m\n\n"
                         f"🇰🇿{r[37]['CcyNm_UZ']}\n1 {r[37]['Ccy']}= {r[37]['Rate']} so\'m  o\'zgarish {r[37]['Diff']}so\'m\n\n"
                         f"🇰🇷{r[35]['CcyNm_UZ']}\n1 {r[35]['Ccy']}= {r[35]['Rate']} so\'m  o\'zgarish {r[35]['Diff']}so\'m\n\n"
                         f"🇰🇬{r[33]['CcyNm_UZ']}\n1 {r[33]['Ccy']}= {r[33]['Rate']} so\'m  o\'zgarish {r[33]['Diff']}so\'m\n\n"
                         f"🕒 Sana {r[0]['Date']} \n"
                         f"🤖 @valyutaa1bot - Markaziy bank valyuta kurslari")
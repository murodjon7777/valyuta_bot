from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
menu = ReplyKeyboardMarkup(
    keyboard=[
        [ 
         KeyboardButton(text="🇺🇿Uzbek"),
        KeyboardButton(text="🇷🇺Russian"),
        KeyboardButton(text="🇬🇧English"),
        ],
        [
        KeyboardButton(text="🇫🇷French"),
        KeyboardButton(text="🇩🇪German"),
        KeyboardButton(text="🇸🇦Arabic"),
        ],
        [ 
        KeyboardButton(text="🇹🇷Turkish"), 
        KeyboardButton(text="🇮🇹Italian") ,
        KeyboardButton(text="🇪🇸Spanish") ,
        ],
        [ 
        KeyboardButton(text="🇰🇷Korean"), 
        KeyboardButton(text="🇯🇵Japan") ,
        KeyboardButton(text="🇨🇳China") ,
        ]
      
    ],
    resize_keyboard=True
)
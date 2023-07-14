from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

rock = KeyboardButton(text='Камень')
scissors = KeyboardButton(text='Ножницы')
paper = KeyboardButton(text='Бумага')
rock_scissors_paper_keyboard = ReplyKeyboardMarkup(keyboard=[
    [rock, scissors, paper]
])
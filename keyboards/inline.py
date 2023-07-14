from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from callback.games import GameCallbackData

number = InlineKeyboardButton(text='Угадай число',
                              callback_data=GameCallbackData(game='number').pack())
rock = InlineKeyboardButton(text='Камень, ножницы, бумага',
                              callback_data=GameCallbackData(game='rock').pack())
magic = InlineKeyboardButton(text='Магический шар',
                              callback_data=GameCallbackData(game='magic').pack())
number_rock_magic_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [number], [rock], [magic]
])
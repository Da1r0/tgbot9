from magic import AI
from aiogram import Dispatcher, Bot, F
from aiogram.types import Message,CallbackQuery
from aiogram import Router

dp = Dispatcher()
callback_query = CallbackQuery()
number_router = Router()


@number_router.callback_query()
async def magic(message: Message):
    await message.answer('Напишите предсказание')

@dp.message(F.text)
async def text_user(message: Message):
    otvets = AI.generate_answer()
    if otvets:
        await message.answer(otvets)



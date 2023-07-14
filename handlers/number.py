
import random

from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from callback.games import GameCallbackData
from states.game import GuessTheNumberState

number_router = Router()


@number_router.callback_query(
    GameCallbackData.filter(F.game == 'number')
)  # Берём только сообщения, являющиеся командой /start
async def start_command(query: CallbackQuery, state: FSMContext):  # message - сообщение, которое прошло через фильтр
    await query.message.answer(
        "Привет, сыграем в игру - я загадал число от 1 до 3, а ты угадывай\n")  # Отвечаем на полученное сообщение
    await query.answer()
    await state.set_state(GuessTheNumberState.is_running)


@number_router.message(StateFilter(GuessTheNumberState.is_running))
async def handle_number(message: Message):
    if message.text.isdigit():
        number = random.randint(1, 3)  # генерируем число только после ответа пользователя, а не до.
        chat_id = message.chat.id
        if number == int(message.text):
            await message.answer('Да! Вы угадали. Я перезагадал число')
        else:
            await message.answer('Нет! Вы не угадали((( Я перезагадал число')
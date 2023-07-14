from random import choice


from aiogram.types import Message, CallbackQuery
from keyboards.reply_rock import rock_scissors_paper_keyboard
from aiogram import Router, F
from callback.games import GameCallbackData
from states.game import RPSState
from aiogram.fsm.context import FSMContext



rock_router = Router()
@rock_router.callback_query(
    GameCallbackData.filter(F.game == 'rock')
)
async def handle_rgs_game(message: Message, query: CallbackQuery, state: FSMContext):
    await query.message.answer('Нажмите на клавиатуре на одну из кнопок',
                         reply_markup=rock_scissors_paper_keyboard)
    await state.set_state(RPSState.is_running)

    variants = ('Камень', 'Ножницы', 'Бумага')
    user_choice = message.text
    if user_choice in variants:
        bots_choice = choice(variants)
        if (bots_choice == 'Бумага' and user_choice == 'Камень' or
            bots_choice == 'Ножницы' and user_choice == 'Бумага' or
            bots_choice == 'Камень' and user_choice == 'Ножницы'):
                await message.answer('Вы проиграли')
        elif bots_choice == user_choice:
            await message.answer('Ничья')
        else:
            await message.answer('Вы выиграли')
    else:
        await message.answer('Вы написали кринж')

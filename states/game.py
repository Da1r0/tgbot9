from aiogram.fsm.state import StatesGroup, State


class MagicBallState(StatesGroup):
    is_running = State()


class RPSState(StatesGroup):
    is_running = State()


class GuessTheNumberState(StatesGroup):
    is_running = State()
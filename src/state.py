from aiogram.fsm.state import State, StatesGroup


class Quiz(StatesGroup):
    waiting_answer = State()
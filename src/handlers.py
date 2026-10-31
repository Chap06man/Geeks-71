from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext

from src.state import Quiz
from src.questions import QUESTIONS
from src.keyboards import reply_buttons, inline_buttons,inline_buttons2

router = Router()

@router.message(CommandStart())
async def command_start(message: Message):
    await message.answer(
        f"Привет, {message.from_user.full_name}! Я твой бот!",
        reply_markup=reply_buttons
    )
    print(f"Пользователь {message.from_user.full_name} написал /start!")

@router.message(Command('help'))
async def help(message: Message):
    await message.answer(
        '/start - запуск бота\n'
        '/help - список команд',
        reply_markup=inline_buttons
    )

@router.message(Command('about'))
async def about(message: Message):
    await message.answer(
        'Это бот от Сардара\n'
        'Он пока не чего не имеют делать\n'
        'Версия 1.0'
    )

@router.message(F.text.lower() == 'пока')
async def bye(message: Message):
    await message.answer('Пока до свидания')

@router.message(F.text == "Корзина")
async def cmd_group(message: Message):
    await message.answer("Твоя корзина пуста(")


@router.callback_query(F.data == "quiz_start")
async def quiz_start(callback: CallbackQuery, state: FSMContext):
    await callback.answer('Начинаем игру!', show_alert=True)
    await state.update_data(index=0, score=0)       # сохраняем прогресс
    await state.set_state(Quiz.waiting_answer)      # переводим в состояние
    await callback.message.answer(f"Вопрос 1: {QUESTIONS[0]['q']}")

@router.callback_query(F.data == 'restart_start')
async def restart(callback: CallbackQuery, state: FSMContext):
    await callback.answer('Начинаем игру!', show_alert=True)
    await state.update_data(index=0, score=0)   
    await state.set_state(Quiz.waiting_answer)      
    await callback.message.answer(f"Вопрос 1: {QUESTIONS[0]['q']}")

@router.message(Quiz.waiting_answer)
async def handle_answer(message: Message, state: FSMContext):
    data = await state.get_data()
    index = data["index"]
    score = data["score"]

    if message.text.lower() == QUESTIONS[index]['a']:
        score += 1
        await message.answer("Правильно! +1")

    else:
        await message.answer(f"Неверно. Правильный ответ: {QUESTIONS[index]['a']}")

    index += 1
    if index >= len(QUESTIONS):
        await message.answer(f"Конец! Счет: {score}/{len(QUESTIONS)}",
                             reply_markup=inline_buttons2)
        await state.clear()

    else:
        await state.update_data(index=index, score=score)
        await message.answer(f"Вопрос {index + 1}: {QUESTIONS[index]['q']}")


@router.message()
async def echo(message: Message):
    await message.answer(f'Ты написал {message.text} !')

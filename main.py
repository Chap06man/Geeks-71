
import asyncio
from os import getenv
import logging
from aiogram import F
from aiogram.types import Message
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command

TOKEN = getenv("TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def command_start(message: Message):
    await message.answer(
        f"Привет, {message.from_user.full_name}! Я твой бот!"
    )
    print(f"Пользователь {message.from_user.full_name} написал /start!")

@dp.message(Command('help'))
async def help(message: Message):
    await message.answer(
        '/start - запуск бота\n'
        '/help - список команд'
    )

@dp.message(Command('about'))
async def about(message: Message):
    await message.answer(
        'Это бот от Сардара\n'
        'Он пока не чего не имеют делать\n'
        'Версия 1.0'
    )

@dp.message(F.text.lower() == 'пока')
async def bye(message: Message):
    await message.answer('Пока до свидания')

@dp.message()
async def echo(message: Message):
    await message.answer(f'Ты написал {message.text} !')

async def main():
    print("Бот запускается...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
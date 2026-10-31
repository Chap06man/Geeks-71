import asyncio
from os import getenv
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from src.handlers import router
TOKEN=''
bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage()) 

async def main():
    print("Бот запускается...")
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
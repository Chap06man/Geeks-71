import asyncio
from os import getenv
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from db.database import init_db
from config import BOT_TOKEN

from src.handlers import router
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage()) 

async def main():
    init_db()
    print("Бот запускается...")
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
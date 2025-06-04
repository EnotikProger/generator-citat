import asyncio
import json
import logging
import aiohttp
import redis.asyncio as redis
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('bot.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Инициализация бота и Redis
API_TOKEN = "7887020640:AAE4IpXus_s3CIvTwCYK3SQDhvdlhBc8yNs"  # Замените на ваш токен
REDIS_URL = "redis://localhost:6379/0"  # Укажите ваш Redis URL
QUOTABLE_API = "https://api.quotable.io/random"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()
redis_client = redis.from_url(REDIS_URL)

# Обработчик команды /start
@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    logger.info(f"User {message.from_user.id} sent /start command")
    await message.reply(
        "Привет! Я бот случайных цитат. Используй /quote, чтобы получить цитату!"
    )


# Запуск бота
async def main():
    logger.info("Starting bot...")
    try:
        await dp.start_polling(bot)
    except Exception as e:
        logger.critical(f"Bot crashed: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main())
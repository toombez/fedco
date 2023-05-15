from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
import os

load_dotenv()
TOKEN = os.environ['TOKEN']

bot = Bot(TOKEN)

dp = Dispatcher(bot)

executor.start_polling(dp)

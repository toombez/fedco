from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types, utils
import os

load_dotenv()

TOKEN = os.environ['TOKEN']

bot = Bot(TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    reply_message = """Доступные команды:
/help — доступные команды
/contacts — контакты
/news — новости
/about — информация о направлении
/modules — модули направления
    """

    await bot.send_message(message.from_id, reply_message)
    return

@dp.message_handler(commands=['contacts'])
async def contacts_command(message: types.Message):
    reply_message = """Контакты педагога:
<a href="https://vk.com">Вконтакте</a>
<a href="https://discord.com">Discord</a>
<a href="https://github.com">GitHub</a>
<a href="https://telegram.org">telegram</a>
<a href="https://gmail.com">email</a>
    """

    await message.reply(reply_message, parse_mode="html")
    return

@dp.message_handler(commands=['news'])
async def news_command(message: types.Message):
    return

@dp.message_handler(commands=['about'])
async def about_command(message: types.Message):
    return

@dp.message_handler(commands=['modules'])
async def modules_command(message: types.Message):
    return

executor.start_polling(dp)

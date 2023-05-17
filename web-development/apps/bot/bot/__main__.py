from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types, filters
import os
from itertools import cycle

load_dotenv()

news = [
    {
        'label': 'lorem1',
        'content': 'Lorem ipsum dolor sit amet consectetur. Urna pharetra libero nunc id sed pulvinar ipsum porttitor at. Ipsum ultricies orci velit senectus a gravida tellus pellentesque. Lectus leo curabitur odio adipiscing libero. Mauris vestibulum non porta eu pellentesque. Justo facilisis egestas ac eget. Pulvinar aliquam viverra nulla pellentesque tortor etiam lorem. Arcu sed suspendisse risus eu magnis eu urna fermentum arcu. Nunc ac tellus pretium mauris urna. Ullamcorper dignissim odio eu malesuada diam morbi morbi curabitur. Blandit morbi sed elit turpis nulla lectus libero a odio. Senectus ultricies sagittis pharetra nullam scelerisque a gravida aliquam vitae. Ullamcorper imperdiet felis at lorem mattis quam quis. Amet condimentum placerat tempor turpis eget elit ligula. Nullam nunc vitae nulla pharetra. Odio rhoncus nullam at vitae auctor egestas arcu tellus. Risus nam iaculis semper pulvinar sed. Turpis suspendisse odio elementum vitae vitae ultrices risus risus tempus. Ut quam nibh pellentesque odio tincidunt viverra pellentesque posuere.',
        'image': 'https://images.unsplash.com/photo-1575936123452-b67c3203c357?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8aW1hZ2V8ZW58MHx8MHx8&w=1000&q=80'
    },
    {
        'label': 'lorem2',
        'content': 'Lore1 ipsum dolor sit amet consectetur. Urna pharetra libero nunc id sed pulvinar ipsum porttitor at. Ipsum ultricies orci velit senectus a gravida tellus pellentesque. Lectus leo curabitur odio adipiscing libero. Mauris vestibulum non porta eu pellentesque. Justo facilisis egestas ac eget. Pulvinar aliquam viverra nulla pellentesque tortor etiam lorem. Arcu sed suspendisse risus eu magnis eu urna fermentum arcu. Nunc ac tellus pretium mauris urna. Ullamcorper dignissim odio eu malesuada diam morbi morbi curabitur. Blandit morbi sed elit turpis nulla lectus libero a odio. Senectus ultricies sagittis pharetra nullam scelerisque a gravida aliquam vitae. Ullamcorper imperdiet felis at lorem mattis quam quis. Amet condimentum placerat tempor turpis eget elit ligula. Nullam nunc vitae nulla pharetra. Odio rhoncus nullam at vitae auctor egestas arcu tellus. Risus nam iaculis semper pulvinar sed. Turpis suspendisse odio elementum vitae vitae ultrices risus risus tempus. Ut quam nibh pellentesque odio tincidunt viverra pellentesque posuere.',
        'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSULBmlrPlwiurWT3S57xXfVh_PPlvsPFsfZJqEayr4&s'
    },
]
cycle_news = cycle(news)

themes = [
    {
        'label': 'lorem1',
        'module': 'm1',
        'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSULBmlrPlwiurWT3S57xXfVh_PPlvsPFsfZJqEayr4&s',
        'skills': ['lorem1', 'lorem2', 'lorem3'],
        'materials': [
            { 'label': 'lorem1', 'href': 'https://google.com' },
            { 'label': 'lorem2', 'href': 'https://google.com' },
        ]
    },
    {
        'label': 'lorem2',
        'module': 'm1',
        'image': 'https://images.unsplash.com/photo-1575936123452-b67c3203c357?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8aW1hZ2V8ZW58MHx8MHx8&w=1000&q=80',
        'skills': ['lorem1', 'lorem2'],
        'materials': [
            { 'label': 'lorem1', 'href': 'https://google.com' },
        ]
    }
]
cycle_themes = cycle(themes)

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
    news = next(cycle_news)

    markup = types.InlineKeyboardMarkup(2, [
        [
            types.InlineKeyboardButton(
                'следующая новость',
                callback_data='next_news'
            )
        ]
    ])

    await bot.send_photo(
        photo=news['image'],
        caption=f"""<b>{news['label']}</b>
{news['content'][:500] + ' <a href="localhost:5000/news">...</a>'}
""",
        parse_mode='html',
        reply_markup=markup,
        chat_id=message.from_id,
    )
    return

@dp.callback_query_handler(lambda c: c.data == 'next_news')
async def next_news_button(query: types.CallbackQuery):
    news = next(cycle_news)

    message = query.message

    await message.edit_media(
        types.InputMediaPhoto(
            news['image'],
            f"""<b>{news['label']}</b>
{news['content'][:500] + ' <a href="localhost:5000/news">...</a>'}
""",
            parse_mode='html'
        ),
        reply_markup=types.InlineKeyboardMarkup(1, [
            [
                types.InlineKeyboardButton('следующая новость', callback_data='next_news')
            ]
        ])
    )
    return

@dp.message_handler(commands=['about'])
async def about_command(message: types.Message):
    reply_message = """IT-квантум (web-разработка)
Web-разработка
Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quaerat impedit provident sequi! Odit, enim rem!

Чему научатся:
1. Основы html css и js
2. Frontend разработку
3. Backend разработку
4. Современные инструменты

Проекты
1. Discord и telegram боты
2. Сайт с использованием современных библиотек и фреймворках
3. Сайт с применением 3D-графики
    """

    await bot.send_message(message.from_id, reply_message, parse_mode='html')
    return

@dp.message_handler(commands=['modules'])
async def modules_command(message: types.Message):
    theme = next(cycle_themes)
    markup = types.InlineKeyboardMarkup(1, [
        [
            types.InlineKeyboardButton('следующая тема', callback_data='next_theme')
        ]
    ])

    skills = '\n'.join(theme['skills'])
    materials = '\n'.join(map(lambda m: f'<a href="{m["href"]}">{m["label"]}</a>', theme['materials']))

    await bot.send_photo(
        message.from_id,
        theme['image'],
        f"""<b>{theme['label']}(модуль: {theme['module']})</b>

чему научится:
{skills}

Материалы:
{materials}
""",
        parse_mode='html',
        reply_markup=markup,
    )
    return

@dp.callback_query_handler(lambda c: c.data == 'next_theme')
async def next_theme_button(query: types.CallbackQuery):
    message = query.message
    theme = next(cycle_themes)
    markup = types.InlineKeyboardMarkup(1, [
        [
            types.InlineKeyboardButton('следующая тема', callback_data='next_theme')
        ]
    ])

    skills = '\n'.join(theme['skills'])
    materials = '\n'.join(map(lambda m: f'<a href="{m["href"]}">{m["label"]}</a>', theme['materials']))

    await message.edit_media(
        types.InputMediaPhoto(
            theme['image'],
            f"""<b>{theme['label']}(модуль: {theme['module']})</b>

чему научится:
{skills}

Материалы:
{materials}
""",
            parse_mode='html'
        ),
        reply_markup=markup
    )
    return

executor.start_polling(dp)

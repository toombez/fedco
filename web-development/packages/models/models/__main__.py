from models import News
from models import Theme
from models import Module
from models import ThemeMaterial
from models import ThemeSkill
from db import db

NEWS_COUNT = 4
MODULES_COUNT = 2
THEMES_IN_EACH_MODULE_COUNT = 2
SKILLS_IN_EACH_THEME_COUNT = 3
MATERIALS_IN_EACH_THEME_COUNT = 3

with db:
    tables = [News, Theme, Module, ThemeMaterial, ThemeSkill]

    db.drop_tables(tables)
    db.create_tables(tables)

    for i in range(NEWS_COUNT):
        news = News.create(
            heading = f'Новость {i + 1}',
            content = 'Lorem ipsum dolor sit amet consectetur. Urna pharetra libero nunc id sed pulvinar ipsum porttitor at. Ipsum ultricies orci velit senectus a gravida tellus pellentesque. Lectus leo curabitur odio adipiscing libero. Mauris vestibulum non porta eu pellentesque. Justo facilisis egestas ac eget. Pulvinar aliquam viverra nulla pellentesque tortor etiam lorem. Arcu sed suspendisse risus eu magnis eu urna fermentum arcu. Nunc ac tellus pretium mauris urna. Ullamcorper dignissim odio eu malesuada diam morbi morbi curabitur. Blandit morbi sed elit turpis nulla lectus libero a odio. Senectus ultricies sagittis pharetra nullam scelerisque a gravida aliquam vitae. Ullamcorper imperdiet felis at lorem mattis quam quis. Amet condimentum placerat tempor turpis eget elit ligula. Nullam nunc vitae nulla pharetra. Odio rhoncus nullam at vitae auctor egestas arcu tellus. Risus nam iaculis semper pulvinar sed. Turpis suspendisse odio elementum vitae vitae ultrices risus risus tempus. Ut quam nibh pellentesque odio tincidunt viverra pellentesque posuere.',
            image_url = 'https://images.unsplash.com/photo-1575936123452-b67c3203c357?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8aW1hZ2V8ZW58MHx8MHx8&w=1000&q=80'
        )

    for i in range(MODULES_COUNT):
        module_id = Module.create(
            name = f'Модуль {i + 1}'
        )

        for j in range(THEMES_IN_EACH_MODULE_COUNT):
            theme_id = Theme.create(
                name = f'Тема {j + 1}',
                description = 'Описание темы 1',
                module_id = module_id
            )

            for k in range(SKILLS_IN_EACH_THEME_COUNT):
                ThemeSkill.create(
                    label = f'Навык {k + 1}',
                    theme_id = theme_id
                )

            for k in range(MATERIALS_IN_EACH_THEME_COUNT):
                ThemeMaterial.create(
                    label = f'Материал {k + 1}',
                    href = 'https://google.com',
                    theme_id = theme_id
                )

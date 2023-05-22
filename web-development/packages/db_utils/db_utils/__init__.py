from models import News, Module, Theme, ThemeMaterial, ThemeSkill

def fetch_news():
    news = News.select()

    return tuple(map(lambda n: (n.heading, n.content, n.image_url), news))

def fetch_modules():
    modules = Module.select()

    return tuple(map(
        lambda m: (
            m.name,
            tuple(map(
                lambda t: (
                    t.name,
                    t.image_url,
                    tuple(map(
                        lambda s: s.label,
                        ThemeSkill.select().where(ThemeSkill.theme_id == t.id)
                    )),
                    tuple(map(
                        lambda material: (material.label, material.href),
                        ThemeMaterial.select().where(ThemeMaterial.theme_id == t.id)
                    ))
                ),
                Theme.select().where(Theme.module_id == m.id)
            ))
        ),
        modules
    ))

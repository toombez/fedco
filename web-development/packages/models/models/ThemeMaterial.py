from models.BaseModel import BaseModel
from models.Theme import Theme
from peewee import CharField, ForeignKeyField

class ThemeMaterial(BaseModel):
    label = CharField()
    href = CharField()
    theme_id = ForeignKeyField(Theme)

    class Meta:
        db_table = 'theme_material'

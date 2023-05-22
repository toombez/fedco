from models.BaseModel import BaseModel
from models.Theme import Theme
from peewee import CharField, ForeignKeyField

class ThemeSkill(BaseModel):
    label = CharField()
    theme_id = ForeignKeyField(Theme)

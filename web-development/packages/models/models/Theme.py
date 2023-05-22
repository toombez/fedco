from models.BaseModel import BaseModel
from models.Module import Module
from peewee import CharField, ForeignKeyField

class Theme(BaseModel):
    name = CharField()
    description = CharField()
    module_id = ForeignKeyField(Module)

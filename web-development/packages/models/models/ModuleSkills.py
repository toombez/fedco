from models.BaseModel import BaseModel
from models.Module import Module
from peewee import CharField, ForeignKeyField

class ModuleSkill(BaseModel):
    label = CharField()
    module_id = ForeignKeyField(Module)

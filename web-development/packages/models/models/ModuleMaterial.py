from models.BaseModel import BaseModel
from models.Module import Module
from peewee import CharField, ForeignKeyField

class ModuleMaterial(BaseModel):
    label = CharField()
    href = CharField()
    module_id = ForeignKeyField(Module)

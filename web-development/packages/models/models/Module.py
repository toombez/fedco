from models.BaseModel import BaseModel
from peewee import CharField

class Module(BaseModel):
    name = CharField()

from models.BaseModel import BaseModel
from peewee import CharField

class News(BaseModel):
    heading = CharField()
    content = CharField()
    image_url = CharField(null=True)

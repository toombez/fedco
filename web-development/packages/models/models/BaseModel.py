from peewee import PrimaryKeyField, Model
from db import db

class BaseModel(Model):
    id = PrimaryKeyField(unique = True)

    class Meta:
        database = db
        order_by = 'id'

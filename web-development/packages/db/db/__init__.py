from peewee import SqliteDatabase
from os.path import join, dirname

DATABASE_PATH = join(dirname(__file__), '..', 'database.db')

db = SqliteDatabase(DATABASE_PATH)

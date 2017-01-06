import datetime
from peewee import Model, CharField, DateTimeField, BooleanField, ForeignKeyField, TextField
from lib.db import db


class BaseModel(Model):
    created_at = DateTimeField()
    updated_at = DateTimeField(default=datetime.datetime.now)
    status = BooleanField(default=True)

    class Meta:
        database = db




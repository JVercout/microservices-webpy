import datetime
from peewee import Model, CharField, DateTimeField, BooleanField, ForeignKeyField, TextField
from lib.db import db


class BaseModel(Model):
    created_at = DateTimeField()
    updated_at = DateTimeField(default=datetime.datetime.now)
    status = BooleanField(default=True)

    class Meta:
        database = db


class Device(BaseModel):
    token = CharField()

    def __repr__(self):
        return "<Device('%s')>" % (self.id)


class DeviceParameter(BaseModel):
    device_id = ForeignKeyField(Device, related_name='parameters', index=True)
    identifier = CharField(null=False, max_length=32)
    value_lsp = TextField(null=False)
    value_sent = TextField(null=False)
    value_device = TextField(null=False)

    def __repr__(self):
        return "<DeviceParameter('%s')>" % (self.identifier)


class Workflow(BaseModel):
    device_id = ForeignKeyField(Device, related_name='workflows', index=True)
    workflow_type = CharField(null=False)
    config_json = TextField()

    def __repr__(self):
        return "<Workflow('%s', '%s')>" % (self.device_id, self.workflow_type)

from base import *
from state import State

class City(BaseModel):
    """Parent table is State"""
    name = peewee.CharField(128, null=False, unique=True)
    state = peewee.ForeignKeyField(State, related_name="cities", on_delete='cascade')

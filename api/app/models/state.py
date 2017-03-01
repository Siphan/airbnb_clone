from base import *

class State(BaseModel):
    name = peewee.CharField(128, null=False, unique=True)

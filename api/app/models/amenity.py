from base import *

class Amenity(BaseModel):
    name = peewee.CharField(128, null=False)

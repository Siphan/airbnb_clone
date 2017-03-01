from base import *
from place import Place
from user import User

class PlaceBook(BaseModel):
    place = peewee.ForeignKeyField(Place)
    user = peewee.ForeignKeyField(User, related_name="places_booked")
    is_validated = peewee.BooleanField(default=False)
    date_start = peewee.DateTimeField(null=False)
    number_nights = peewee.IntegerField(default=1)

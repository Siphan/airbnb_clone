from base import *
from place import Place
from user import User

class PlaceBook(BaseModel):
    """Define booking model"""
    place = peewee.ForeignKeyField(Place)
    user = peewee.ForeignKeyField(User, related_name="places_booked")
    is_validated = peewee.BooleanField(default=False)
    date_start = peewee.DateTimeField(null=False)
    number_nights = peewee.IntegerField(default=1)

    def to_hash(self):
        """Return a hash with info on booking made"""
        hash = {
            'id': self.id,
            'created_at': self.created_at.strftime("%Y/%m/%d %H:%M:%S"),
            'updated_at': self.updated_at.strftime("%Y/%m/%d %H:%M:%S"),
            'place_id': self.place_id,
            'user_id': self.user_id,
            'is_validated': self.is_validated,
            'date_start': self.date_start.strftime("%Y/%m/%d %H:%M:%S"),
            'number_nights': self.number_nights
        }
        return hash

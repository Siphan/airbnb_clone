from base import *
from user import User
from city import City

class Place(BaseModel):
    owner = peewee.ForeignKeyField(User, related_name="places")
    city = peewee.ForeignKeyField(City, related_name="places")
    name = peewee.CharField(128, null=False)
    description = peewee.TextField()
    number_rooms = peewee.IntegerField(default=0)
    number_bathrooms = peewee.IntegerField(default=0)
    max_guest = peewee.IntegerField(default=0)
    price_by_night = peewee.IntegerField(default=0)
    latitude = peewee.FloatField()
    longitude = peewee.FloatField()

    def to_hash(self):
        """Return a hash with all info on bookable accomodation"""
        hash = {
            'id': self.id,
            'created_at': self.created_at.strftime("%Y/%m/%d %H:%M:%S"),
            'updated_at': self.updated_at.strftime("%Y/%m/%d %H:%M:%S"),
            'owner_id': self.owner_id,
            'city_id': self.city_id,
            'name': self.name,
            'description': self.description,
            'number_rooms': self.number_rooms,
            'number_bathrooms': self.number_bathrooms,
            'max_guest': self.max_guest,
            'price_by_night': self.price_by_night,
            'latitude': self.latitude,
            'longitude': self.longitude
        }
        return hash

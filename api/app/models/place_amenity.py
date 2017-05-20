"""Import all models"""
from base import *
from peewee import Model
from playhouse.fields import ManyToManyField
from place import Place
from amenity import Amenity

class PlaceAmenities(Model):
    """Model to create a joint table between Places and Amenities
    PlaceAmenities & BaseModel are the only 2 classes inherited from peewee
    """
    place = ManyToManyField(Place)
    amenity = ManyToManyField(Amenity)

    class Meta:
        """Connect the model to the DB"""
        database = database

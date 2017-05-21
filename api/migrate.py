'''Import peewee models from their respective folders and create the tables in
the database. The import of base is required, in addition for access to
BaseModel class, for base.py to access the variables set up in config.py.
'''
import peewee
from peewee import *
from app.models.amenity import Amenity
from app.models.city import City
from app.models.place_amenity import PlaceAmenities
from app.models.place_book import PlaceBook
from app.models.state import State
from app.models.user import User
from app.models.place import Place
from app.models.base import *

def create_database():
    db.connect()
    db.create_tables([Amenity,
                      City,
                      PlaceAmenities,
                      PlaceBook,
                      State,
                      User,
                      Place])

if __name__ == '__main__':
    create_database()

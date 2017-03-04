from base import *

class Amenity(BaseModel):
    """Define accomodation's Amenity model"""
    name = peewee.CharField(128, null=False)

    def to_hash(self):
        """Return a hash with info on accomodation's amenity"""
        hash = {
            'id': self.id,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'name': self.name
        }
        return hash

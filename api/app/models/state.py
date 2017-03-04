"""Import base model"""
from base import *

class State(BaseModel):
    """Define State model"""
    name = peewee.CharField(128, null=False, unique=True)

    def to_hash(self):
        """Return a hash with all state's info"""
        hash = {
            'id': self.id,
            'created_at': self.created_at.strftime("%Y/%m/%d %H:%M:%S"),
            'updated_at': self.updated_at.strftime("%Y/%m/%d %H:%M:%S"),
            'name': self.name
        }
        return hash

from base import *
from state import State

class City(BaseModel):
    """Parent table is State"""
    name = peewee.CharField(128, null=False, unique=True)
    state = peewee.ForeignKeyField(State, related_name="cities", on_delete='cascade')

    def to_hash(self):
        """Return a hash with all city's info"""
        hash = {
            'id': self.id,
            'created_at': self.created_at.strftime("%Y/%m/%d %H:%M:%S"),
            'updated_at': self.updated_at.strftime("%Y/%m/%d %H:%M:%S"),
            'name': self.name,
            'state_id': self.state_id
        }
        return hash

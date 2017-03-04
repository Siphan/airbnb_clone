"""
This base module defines the model that will be the base
of all our classes. It is itself inherited from a Model
from peewee, a Python object relational mapper (ORM).
"""

import peewee
from config import *
from datetime import datetime

database = peewee.MySQLDatabase( DATABASE['database'],
                          user=DATABASE['user'],
                          charset=DATABASE['charset'],
                          host=DATABASE['host'],
                          port=DATABASE['port'],
                          passwd=DATABASE['password'] )

class BaseModel(peewee.Model):
    """Define base model"""
    id = peewee.PrimaryKeyField(unique=True)
    created_at = peewee.DateTimeField(default=datetime.now, formats='%Y/%m/%d %H:%M:%S')
    updated_at = peewee.DateTimeField(default=datetime.now, formats='%Y/%m/%d %H:%M:%S')

    def save(self, *args, **kwargs):
        """Save the Model to the database"""
        self.updated_at = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        peewee.Model.save(self)

    class Meta:
        """Connect to the database"""
        database = database
        order_by = ("id", )

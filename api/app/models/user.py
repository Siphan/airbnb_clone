"""Import base model and hashlib for password encryption"""
from base import *
import hashlib

class User(BaseModel):
    """Define all info needed for each user"""
    email = peewee.CharField(128, null=False, unique=True)
    password = peewee.CharField(128, null=False)
    first_name = peewee.CharField(128, null=False)
    last_name = peewee.CharField(128, null=False)
    is_admin = peewee.BooleanField(default=False)

    def set_password(self, clear_password):
        """Convert user password to MD5 encryption"""
        passwd = hashlib.md5()
        passwd.update(self.clear_password)
        self.password = passwd.digest()

    def to_hash(self):
        """Return a hash with all user's info"""
        hash = {
            'id': self.id,
            'created_at': self.created_at.strftime("%Y/%m/%d %H:%M:%S"),
            'updated_at': self.updated_at.strftime("%Y/%m/%d %H:%M:%S"),
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'is_admin': self.is_admin
        }
        return hash

from base import *
import hashlib

class User(BaseModel):
    email = peewee.CharField(128, null=False, unique=True)
    password = peewee.CharField(128, null=False)
    first_name = peewee.CharField(128, null=False)
    last_name = peewee.CharField(128, null=False)
    is_admin = peewee.BooleanField(default=False)

    def set_password(self, clear_password):
        """Set user password in MD5 encryption"""
        m = hashlib.md5()
        m.update(self.clear_password)
        self.password = m.digest()

    def to_hash(self)

#!/usr/bin/python3
""" BaseModel class that defines all
    common attributes/methods for other classes """

import uuid
from datetime import datetime

class BaseModel:
    """ """

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.updated_at = datetime.now()
        self.created_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        return {
            'my_number': self.my_number,
            'name' : self.name,
            '__class__': self.__class__.__name__,
            'created_at': self.created_at.isoformat(),
            'id' : self.id,
            'updated_at': self.updated_at.isoformat()
            }

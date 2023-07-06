#!/usr/bin/python3
""" BaseModel class that defines all
    common attributes/methods for other classes """

import uuid
from datetime import datetime


class BaseModel:
    """ BaseModel class that defines all """

    def __init__(self):
        """ initializes the class instance """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """ returns a string representation of the class
            instance attributes """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """ updates the public instance attribute
            updated_at with the current datetime """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary of the class
            instance attributes  """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict

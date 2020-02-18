#!/usr/bin/env python3

"""
BaseModel class that defines all common attributes/methods
for other classes

"""

from datetime import datetime
from models import storage
from uuid import uuid4


class BaseModel:

    """ BaseModel Class definition """

    def __init__(self, *args, **kwargs):
        """ Constructor """

        for key, value in kwargs.items():
            if key == "__class__":
                continue

            if (key == "created_at" or key == "updated_at"):
                value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")

            setattr(self, key, value)

        if "id" not in kwargs.keys():
            self.id = str(uuid4())

        if "created_at" not in kwargs.keys():
            self.created_at = datetime.now()

        if "updated_at" not in kwargs.keys():
            self.updated_at = datetime.now()

        if len(kwargs) == 0:
            storage.new(self)

    def __str__(self):
        """ Defines what should be printed for each instance of the class """
        st = "[{:s}] ({:s}) {:s}"
        st = st.format(self.__class__.__name__, self.id, str(self.__dict__))
        return st

    def save(self):
        """
        Update the Public Instance Attr updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__
        of the instance
        """
        dcopy = self.__dict__.copy()
        dcopy["__class__"] = self.__class__.__name__
        dcopy["created_at"] = self.created_at.isoformat()
        dcopy["updated_at"] = self.updated_at.isoformat()
        return dcopy

#!/usr/bin/python3
"""Module containing BaseMode class that defines common attributes/methods for\
other classes"""
import uuid
from datetime import datetime

import models

models.storage.reload()


class BaseModel:
    """model that defines common attributes and methods for other classes"""

    def __init__(self, *args, **kwargs):
        """initialization of the BaseModel"""
        if len(kwargs) != 0:
            for key in kwargs:
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        date_str = kwargs[key]
                        setattr(self, key, datetime.fromisoformat(date_str))
                    else:
                        setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """string representation of the BaseModel class"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     self.__dict__)

    def save(self):
        """updates the object by updating the updated_at value"""
        setattr(self, "updated_at", datetime.now())

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = type(self).__name__
        obj_dict["created_at"] = obj_dict["created_at"].strftime(
            "%Y-%m-%dT%H:%M:%S.%f")
        obj_dict["updated_at"] = obj_dict["updated_at"].strftime(
            "%Y-%m-%dT%H:%M:%S.%f")

        return obj_dict

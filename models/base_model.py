#!/usr/bin/python3
"""base module for all our modules"""
import uuid
from datetime import datetime
import models

class BaseModel:
    """base model class for all our models"""

    def __init__(self, *args, **kwargs):
        """initialize instance of this class

        Args:
            arg: variable argument, can be a list or tuple
            kwargs: key-value argument, can be a dictionary
        """
        if kwargs:
            for key in kwargs:
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        self.__setattr__(
                                  key,
                                  datetime.fromisoformat(kwargs[key])
                                )
                    else:
                        self.__setattr__(key, kwargs[key])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            models.storage.new(self)

    def __str__(self):
        """get string representation of instance of this class"""
        return '[{}] ({}) {}'.format(
                  self.__class__.__name__,
                  self.id,
                  self.__dict__
                )

    def save(self):
        """update/modify date/time of instance of this class"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """get dictionary representation of instance of this class"""
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict

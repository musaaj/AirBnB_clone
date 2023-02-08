#!/usr/bin/python3
"""base module for all our modules"""
import uuid
from datetime import datetime


class BaseModel:
    """base model class for all our models"""

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def __str__(self):
        """get string representation of this"""
        return '[{}] ({}) {}'.format(
                  self.__class__,
                  self.id,
                  self.__dict__
                )

    def save(self):
         """update modification date/time of this"""
         self.updated_at = datetime.today()

    def to_dict(self):
        """get dictionary representation of this"""
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict

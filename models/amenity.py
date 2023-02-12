#!/usr/bin/python3
"""amenity module"""
from models.base_model import BaseModel
"""Authors henok934 musaaj"""


class Amenity(BaseModel):
    """amenity model"""
    name = ''

    def __init__(self, *args, **kwargs):
        """create instance of amenity"""
        if kwargs:
            super().__init__(**kwargs)
        else:
            super().__init__()

#!/usr/bin/python3
"""amenity module"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """amenity model"""
    name = ''

    def __init__(self):
        """create instance of amenity"""
        super().__init__()

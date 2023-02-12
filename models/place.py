#!/usr/bin/python3
"""place module"""
from models.base_model import BaseModel
"""Authors henok934 & musaaj"""


class Place(BaseModel):
    """place model"""
    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """create instance of Place"""
        if kwargs:
            super().__init__(**kwargs)
        else:
            super().__init__()

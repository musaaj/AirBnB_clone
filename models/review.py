#!/usr/bin/python3
"""review module"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review model"""
    place_id = ''
    user_id = ''
    text = ''

    def __init__(self, *args, **kwargs):
        """create instance of Review"""
        if kwargs:
            super().__init__(**kwargs)
        else:
            super().__init__()

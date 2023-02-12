#!/usr/bin/python3
"""state module"""
from models.base_model import BaseModel
"""Authors henok934 & musaaj"""


class State(BaseModel):
    """state model"""
    name = ''

    def __init__(self, *args, **kwargs):
        """create instance of State"""
        if kwargs:
            super().__init__(**kwargs)
        else:
            super().__init__()

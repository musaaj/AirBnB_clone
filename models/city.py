#!/usr/bin/python3
"""city module"""
from models.base_model import BaseModel
"""Authors henok934 & mussag"""


class City(BaseModel):
    """city model"""
    name = ''
    state_id = ''

    def __init__(self, *args, **kwargs):
        """create instance of City"""
        if kwargs:
            super().__init__(**kwargs)
        else:
            super().__init__()

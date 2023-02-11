#!/usr/bin/python3
"""city module"""
from models.base_model import BaseModel


class City(BaseModel):
    """city model"""
    name = ''
    state_id = ''

    def __init__(self):
        """create instance of City"""
        super().__init__()

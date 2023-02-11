#!/usr/bin/python3
"""state module"""
from models.base_model import BaseModel


class State(BaseModel):
    """state model"""
    name = ''

    def __init__(self):
        """create instance of State"""
        super().__init__()


#!/usr/bin/python3
"""user module"""
from models.base_model import BaseModel


class User(BaseModel):
    """user model"""
    email = ''
    passward = ''
    first_name = ''
    last_name = ''

    def __init__(self):
        """create an instance of user"""
        super().__init__()
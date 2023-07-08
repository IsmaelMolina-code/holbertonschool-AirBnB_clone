#!/usr/bin/python3
"""Defines user class"""

from models.base_model import BaseModel

class User(BaseModel):
    """Creates a new empty data user"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

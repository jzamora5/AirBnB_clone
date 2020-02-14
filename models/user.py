#!/usr/bin/python3

"""
User class that inherits from BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """ Class that defines attributes for an user """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

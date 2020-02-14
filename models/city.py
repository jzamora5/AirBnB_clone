#!/usr/bin/python3

"""
City class that inherits from BaseModel
"""

from models.base_model import BaseModel


class City(BaseModel):
    """ Class that defines attributes for a city """

    state_id = ""
    name = ""

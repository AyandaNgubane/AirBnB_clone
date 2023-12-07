#!/usr/bin/python3
"""
City Module
A module that inherits from BaseModel,
and it contains the attributes to be assigned
to the cities.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    City Class

    Attributes:
        state_id (str): The UUID of the State the City belongs to
        name (str): The City name
    """

    state_id = ""
    name = ""

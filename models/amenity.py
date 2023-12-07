#!/usr/bin/python3
"""Amenity Module

A module that inherits from BaseModel,
and it contains the attributes to be assigned
to the Amenities of the places.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity Class

    Attributes:
        name (str): The Amenity name
    """

    name = ""

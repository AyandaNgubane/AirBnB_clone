#!/usr/bin/python3
"""
State Module

A module that inherits from BaseModel,
and it contains the attributes to be assigned
to the States.
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    State Class

    Attributes:
        name (str): The State name
    """
    name = ""

#!/usr/bin/python3
"""module that contains the User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class for user abstraction"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

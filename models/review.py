#!/usr/bin/python3
"""module for review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """review class for handlling review data"""
    place_id = ""
    user_id = ""
    text = ""

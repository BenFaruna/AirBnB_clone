#!/usr/bin/python3
"""Module containing BaseMode class that defines common attributes/methods for\
other classes"""
import uuid
from datetime import datetime


class BaseModel:
    """model that defines common attributes and methods for other classes"""

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

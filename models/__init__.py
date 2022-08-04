#!/usr/bin/python3
"""module serving instance for FileStorage"""
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

classes = {
    "BaseModel": BaseModel,
}

storage = FileStorage()
storage.reload()

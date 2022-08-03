#!/usr/bin/python3
"""module serving instance for FileStorage"""
from engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

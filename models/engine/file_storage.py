#!/usr/bin/python3
"""module for file storage handling serialization and deserialization of
model into json and deserializing from json into object instance"""
import json


class FileStorage:
    """class that holds method for file storage"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the __objects value"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = type(obj).__name__ + ".id"
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        """serializes __objects to the JSON file path"""

        with open(FileStorage.__file_path, "w") as f:
            json.dump(FileStorage.all(), f, encoding="utf-8", indent=2)

    def reload(self):
        """deserializes the JSON file to __objects if JSON file exists"""
        with open(FileStorage.__file_path) as f:
            if f is None:
                pass
            else:
                return json.load(f)

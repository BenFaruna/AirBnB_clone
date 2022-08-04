#!/usr/bin/python3
"""module for file storage handling serialization and deserialization of
model into json and deserializing from json into object instance"""
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """class that holds method for file storage"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the __objects value"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file path"""

        with open(FileStorage.__file_path, "w") as f:
            file_dict = FileStorage.__objects
            obj_json = {
                obj: file_dict[obj].to_dict() for obj in file_dict.keys()
                }
            json.dump(obj_json, f, indent=2)

    def reload(self):
        """deserializes the JSON file to __objects if JSON file exists"""
        try:
            with open(self.__file_path, "r") as f:
                file_json = json.loads(f.read())
                for key, value in file_json.items():
                    model = key.split(".")[0]
                    self.__objects[key] = eval(model)(**value)
        except (FileNotFoundError):
            pass

#!/usr/bin/python3
"""Module containing test case for BaseModel class"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """TestCase for BaseModel"""

    def setUp(self):
        """Set up test methods"""
        pass

    def tearDown(self):
        """Tear Down test methods"""
        pass

    def test_file_storage_instance(self):
        """test instance of file storage can be created"""
        file_storage = FileStorage()
        self.assertIsInstance(file_storage, FileStorage)

    def test_private_class_attribute_cannot_be_accessed_externally(self):
        """test private attributes cannot be accessed from instance of
        object"""
        file_storage = FileStorage()

        with self.assertRaises(AttributeError):
            file_storage.__filepath
        with self.assertRaises(AttributeError):
            file_storage.__objects

    def test_data_structure_of_file_storage_objects_attributes(self):
        """test the data structure for FileStorage private class attribute
        objects is a dict to ensure data is transferred in the right format"""
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)

    def test_file_path_of_file_storage_is_correct(self):
        """test the file_path private class attribute points to the right
        storage file"""
        self.assertEqual(FileStorage._FileStorage__file_path, "file.json")

    def test_all_method_is_present(self):
        """test the all method of the FileStorage class is an attribute of
        the class FileStorage"""
        self.assertIsNotNone(getattr(FileStorage(), "all"))

    def test_all_method_return_dict_object(self):
        """test the return value of the all method"""
        file_storage = FileStorage()
        self.assertIsInstance(file_storage.all(), dict)

    def test_all_method_return_the_value_of_the_objects_attribute(self):
        """test the all mmethod returns the samr value as the private class
        attribute __objects"""
        file_storage = FileStorage()
        self.assertEqual(file_storage.all(),
                         FileStorage._FileStorage__objects)

    def test_new_method_is_present(self):
        """test the new method of the FileStorage class is an attribute of
        the class FileStorage"""
        self.assertIsNotNone(getattr(FileStorage(), "new"))

    def test_new_key_follows_the_right_convention(self):
        """test that the naming convention of objects added to the objects
        follows the right naming convention of <class name>.id"""
        file_storage = FileStorage()
        model = BaseModel()
        file_storage.new(model)

        for key in file_storage.all():
            class_name, model_id = key.split(".")
        self.assertEqual(class_name, type(model).__name__)
        self.assertEqual(model.id, model_id)

    def test_new_value_updates_to_an_object(self):
        """test the new value update to ensure it is the right dictionary
        representation of the model"""
        file_storage = FileStorage()
        model = BaseModel()

        file_storage.new(model)
        storage = file_storage.all()

        for key in storage:
            value = storage[key]

        self.assertIsInstance(value, type(model))

    def test_save_method_is_present(self):
        """test the save method of the FileStorage class is an attribute of
        the class FileStorage"""
        self.assertIsNotNone(getattr(FileStorage(), "save"))


if __name__ == "__main__":
    unittest.main()

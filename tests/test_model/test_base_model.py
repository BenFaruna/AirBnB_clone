#!/usr/bin/python3
"""Module containing test case for BaseModel class"""
import io
import time
import unittest
import uuid
from unittest.mock import patch
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """TestCase for BaseModel"""

    @patch("sys.stdout", new_callable=io.StringIO)
    def assert_print_stdout(self, ins, expected_output, mock_stdout):
        """used to test output to stdout"""
        print(ins)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_base_model_instance_have_id_attribute(self):
        """test to ensure that BaseModel contains id attribute"""
        model = BaseModel()
        self.assertIn("id", model.__dict__)

    def test_base_model_id_attribute_is_not_none(self):
        """test to ensure the id attribute is given a value"""
        model = BaseModel()
        self.assertIsNotNone(model.id)

    def test_base_id_attribute_is_a_string(self):
        """test to check the data type of the id attribute of the model"""
        model = BaseModel()
        self.assertIsInstance(model.id, str)

    def test_id_is_unique_for_different_instance(self):
        """test that BaseModel id attribute is unique for every instance"""
        model_1 = BaseModel()
        model_2 = BaseModel()
        model_3 = BaseModel()
        self.assertNotEqual(model_1.id, model_2.id)
        self.assertNotEqual(model_2.id, model_3.id)
        self.assertNotEqual(model_1.id, model_3.id)

    def test_base_model_have_created_at_attribute(self):
        """test for the presence of the created_at attribute"""
        model = BaseModel()
        self.assertIn("created_at", model.__dict__)  # (model.created_at)

    def test_base_model_created_at_attribute_is_not_none(self):
        """test to ensure the created_at attribute is given a value"""
        model = BaseModel()
        self.assertIsNotNone(model.created_at)

    def test_base_model_have_updated_at_attribute(self):
        """test for the presence of the updated_at attribute"""
        model = BaseModel()
        self.assertIn("updated_at", model.__dict__)

    def test_base_model_updated_at_attribute_is_not_none(self):
        """test to ensure the updated_at attribute is given a value"""
        model = BaseModel()
        self.assertIsNotNone(model.updated_at)

    def test_created_at_and_updated_are_equal_on_initialization(self):
        """test on object initialization created_at and updated_at
        have the same value"""
        model = BaseModel()
        self.assertEqual(model.created_at, model.updated_at)

    # def test_string_representation_using_str_magic_method(self):
    #     """test the __str__ method returns [<class name>]
# (<self.id>) <self.__dict__>"""
    #     model = BaseModel()
    #     expected_str = f"[BaseModel] ({...}) {...}"
    #     self.assert_print_stdout(model, expected_str)

    def test_save_method_updates_the_updated_at_attribute(self):
        """test save method updates updated_at attribute using time
        difference"""
        model = BaseModel()
        # time.sleep is to allow a difference in time before update
        time.sleep(1)
        model.save()
        self.assertNotEqual(model.created_at, model.updated_at)
        self.assertGreater(model.updated_at, model.created_at)

    def test_to_dict_return_a_dictionary(self):
        """test the return value data type of the to_dict method"""
        model = BaseModel()
        obj_dict = model.to_dict()
        self.assertIsInstance(obj_dict, dict)

    def test_to_dict_result_contain_class_key(self):
        """test for the presence of the __class__ key in the result of
        to_dict method"""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIn("__class__", model_dict)

    def test_created_at_and_updated_at_in_iso_format_after_to_dict(self):
        """test datetime object for created_at and updated_at changed to iso
        format"""
        model = BaseModel()
        model_dict = model.to_dict()
        created_at = model_dict["created_at"]
        updated_at = model_dict["updated_at"]

        self.assertEqual(created_at, datetime.isoformat(model.created_at))
        self.assertEqual(updated_at, datetime.isoformat(model.updated_at))

    def test_instance_creation_when_kwargs_is_empty(self):
        """test instance is created with id, created_at and updated_at when
        kwargs is empty"""
        model = BaseModel()
        attr_no = len(model.__dict__)
        self.assertEqual(attr_no, 3)
        self.assertIn("id", model.__dict__)
        self.assertIn("created_at", model.__dict__)
        self.assertIn("updated_at", model.__dict__)

    def test_instance_creation_when_kwargs_is_not_empty(self):
        """test to ensure instance is created properly when kwargs values are given"""
        model = BaseModel()
        model_json = model.to_dict()
        model_2 = BaseModel(model_json)
        self.assertIsInstance(model_2, BaseModel)

    def test_instance_contain_right_values_from_kwargs(self):
        """test instance is created with the right values from kwargs"""
        model = BaseModel()
        model_json = model.to_dict()
        model_2 = BaseModel(**model_json)
        self.assertEqual(model_2.id, model_json["id"])
        self.assertEqual(datetime.isoformat(model_2.created_at),
                         model_json["created_at"])
        self.assertEqual(datetime.isoformat(model_2.updated_at),
                         model_json["updated_at"])

    def test_kwargs_instance_created_at_and_updated_at_in_datetime_format(self):
        """test to ensure created_at and updated_at are convereted into
        datetime format while instance is created using kwargs"""
        model = BaseModel()
        model_json = model.to_dict()
        model_2 = BaseModel(**model_json)
        self.assertIsInstance(model_2.created_at, datetime)
        self.assertIsInstance(model_2.updated_at, datetime)

    def test_kwargs_instance_does_not_have_class_attribute(self):
        """test to verify the __class__ key is not an attribute of instance
        created with kwargs"""
        model = BaseModel()
        model_json = model.to_dict()
        model_2 = BaseModel(**model_json)
        self.assertNotIn("__class__", model_2.__dict__)

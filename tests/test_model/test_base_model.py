#!/usr/bin/python3
"""Module containing test case for BaseModel class"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """TestCase for BaseModel"""

    def test_base_model_instance_have_id_attribute(self):
        """test to ensure that BaseModel contains id attribute"""
        model = BaseModel()
        self.assertIn("id", model.__dict__)

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

    def test_base_model_have_updated_at_attribute(self):
        """test for the presence of the updated_at attribute"""
        model = BaseModel()
        self.assertIn("updated_at", model.__dict__)

    def test_created_at_and_updated_at_have_the_same_value_on_object_initialization(self):
        """test on object initialization created_at and updated_at have the same value"""
        model = BaseModel()
        self.assertEqual(model.created_at, model.updated_at)

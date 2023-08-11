#!/usr/bin/python3
"""
Module containing tests for BaseModel class
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import os

class TestBaseModel(unittest.TestCase):
    """
    Test cases for BaseModel class
    """

    def test_init(self):
        """
        Test BaseModel instance creation and initialization
        """
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertTrue(hasattr(my_model, "id"))
        self.assertTrue(hasattr(my_model, "created_at"))
        self.assertTrue(hasattr(my_model, "updated_at"))

    def test_init_with_kwargs(self):
        """
        Test BaseModel instance creation with keyword arguments
        """
        data = {
            "id": "123",
            "created_at": "2023-08-09T12:00:00.000000",
            "updated_at": "2023-08-09T14:00:00.000000",
            "custom_attr": "test_value"
        }
        my_model = BaseModel(**data)
        self.assertEqual(my_model.id, "123")
        self.assertEqual(my_model.created_at, datetime(2023, 8, 9, 12, 0, 0))
        self.assertEqual(my_model.updated_at, datetime(2023, 8, 9, 14, 0, 0))
        self.assertEqual(my_model.custom_attr, "test_value")

    def test_str(self):
        """
        Test __str__ method
        """
        my_model = BaseModel()
        str_rep = str(my_model)
        self.assertIn("[BaseModel]", str_rep)
        self.assertIn("id", str_rep)
        self.assertIn("created_at", str_rep)
        self.assertIn("updated_at", str_rep)

    def test_save(self):
        """
        Test save method
        """
        my_model = BaseModel()
        prev_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(prev_updated_at, my_model.updated_at)

    def test_to_dict(self):
        """
        Test to_dict method
        """
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
        self.assertIsInstance(my_model_dict, dict)
        self.assertEqual(my_model_dict['__class__'], "BaseModel")
        self.assertEqual(my_model_dict['id'], my_model.id)
        self.assertIn('created_at', my_model_dict)
        self.assertIn('updated_at', my_model_dict)

    def test_to_dict_format(self):
        """
        Test the correct format of to_dict output
        """
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
        created_at = datetime.strptime(my_model_dict['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
        updated_at = datetime.strptime(my_model_dict['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
        self.assertIsInstance(created_at, datetime)
        self.assertIsInstance(updated_at, datetime)

if __name__ == "__main__":
    unittest.main()

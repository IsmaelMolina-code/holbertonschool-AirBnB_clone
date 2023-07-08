#!/usr/bin/python3

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_id_and_intances(self):
        model1 = BaseModel()
        model2 = BaseModel()

        self.assertIsInstance(model1, BaseModel)
        self.assertIsInstance(model2, BaseModel)

        self.assertIsNotNone(model1.id)
        self.assertIsNotNone(model2.id)

        self.assertIsInstance(model1.id, str)
        self.assertIsInstance(model2.id, str)

        self.assertNotEqual(model1.id, model2.id)

    def test_dict(self):
        obj = BaseModel()

        self.assertIn("id", obj.__dict__)
        self.assertIn("created_at", obj.__dict__)
        self.assertIn("updated_at", obj.__dict__)

    def test_created_at(self):
        model = BaseModel()

        self.assertIsNotNone(model.created_at)

        self.assertIsInstance(model.created_at, datetime)

    def test_updated_at(self):
        model = BaseModel()

        self.assertIsNotNone(model.updated_at)

        self.assertIsInstance(model.updated_at, datetime)

        self.assertEqual(model.updated_at, model.created_at)

    def test_save_updated_at(self):
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()

        self.assertNotEqual(old_updated_at, model.updated_at)
        self.assertIsInstance(model.updated_at, datetime)

    def test_to_dict_contains_attributes(self):
        model = BaseModel()
        model.name = "Test Model"
        model.number = 123
        model_dict = model.to_dict()

        self.assertIsInstance(model_dict, dict)
        self.assertIn("id", model_dict)
        self.assertIn("created_at", model_dict)
        self.assertIn("updated_at", model_dict)
        self.assertIn("name", model_dict)
        self.assertIn("number", model_dict)

    def test_to_dict_class_name(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict["__class__"], "BaseModel")

    def test_to_dict_datetime_format(self):
        model = BaseModel()
        model_dict = model.to_dict()
        created_at_str = datetime.strptime(
            model_dict["created_at"], "%Y-%m-%dT%H:%M:%S.%f"
        )
        updated_at_str = datetime.strptime(
            model_dict["updated_at"], "%Y-%m-%dT%H:%M:%S.%f"
        )

        self.assertIsInstance(created_at_str, datetime)
        self.assertIsInstance(updated_at_str, datetime)

    """Otros casos de prueba"""

    # def test_load_from_dict(self):
    #     model_dict = {'id': '123', 'created_at': '2022-01-01T00:00:00.000000', ...}
    #     model = BaseModel()
    #     model.load_from_dict(model_dict)
    #     self.assertEqual(model.id, '123')
    #     self.assertEqual(model.created_at, datetime(2022, 1, 1, 0, 0, 0))


if __name__ == "__main__":
    unittest.main()
    
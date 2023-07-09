#!/usr/bin/python3

import unittest
from models.city import City
from models.base_model import BaseModel


class TestCityClass(unittest.TestCase):
    """Tests for City class"""

    def test_class(self):
        obj = City()

        self.assertIsInstance(obj, City)
        self.assertIsInstance(obj, BaseModel)

        self.assertIn("id", obj.__dict__)
        self.assertIn("created_at", obj.__dict__)
        self.assertIn("updated_at", obj.__dict__)
        self.assertIn("state_id", City.__dict__)
        self.assertIn("name", City.__dict__)

        self.assertEqual(City.state_id, "")
        self.assertEqual(City.name, "")

    def test_attributes_assignment(self):
        city = City()
        city.state_id = "12345"
        city.name = "New York"

        self.assertEqual(city.state_id, "12345")
        self.assertEqual(city.name, "New York")

    def test_to_dict(self):
        """Test the to_dict() method of City class"""
        city = City()
        city.state_id = "12345"
        city.name = "New York"

        city_dict = city.to_dict()

        self.assertEqual(city_dict["state_id"], "12345")
        self.assertEqual(city_dict["name"], "New York")
        self.assertEqual(city_dict["__class__"], "City")
        self.assertIn("id", city_dict)
        self.assertIn("created_at", city_dict)
        self.assertIn("updated_at", city_dict)


if __name__ == '__main__':
    unittest.main()

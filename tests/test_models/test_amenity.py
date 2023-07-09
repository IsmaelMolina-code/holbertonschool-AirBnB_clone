#!/usr/bin/python3

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenityClass(unittest.TestCase):
    """ Tests amenity class """

    def test_class(self):

        obj = Amenity()

        self.assertIsInstance(obj, Amenity)
        self.assertIsInstance(obj, BaseModel)

        self.assertIn("id", obj.__dict__)
        self.assertIn("created_at", obj.__dict__)
        self.assertIn("updated_at", obj.__dict__)
        self.assertIn("name", Amenity.__dict__)

    def test_attributes_assignment(self):

        amenity = Amenity()
        amenity.name = "Pet allowed"

        self.assertEqual(amenity.name, "Pet allowed")

    def test_to_dict(self):

        amenity = Amenity()
        amenity.name = "Pet allowed"

        amenity_dict = amenity.to_dict()

        self.assertEqual(amenity_dict["name"], "Pet allowed")
        self.assertIn("id", amenity_dict)
        self.assertIn("created_at", amenity_dict)
        self.assertIn("updated_at", amenity_dict)


if __name__ == '__main__':
    unittest.main()

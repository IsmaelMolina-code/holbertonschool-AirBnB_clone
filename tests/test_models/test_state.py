#!/usr/bin/python3

import unittest
from models.state import State
from models.base_model import BaseModel


class TestStateClass(unittest.TestCase):
    """Tests for State class"""

    def test_class(self):
        state = State()

        self.assertIsInstance(state, State)
        self.assertIsInstance(state, BaseModel)

        self.assertIn("id", state.__dict__)
        self.assertIn("created_at", state.__dict__)
        self.assertIn("updated_at", state.__dict__)
        self.assertIn("name", State.__dict__)

        self.assertEqual(State.name, "")

    def test_attributes_assignment(self):
        state = State()
        state.name = "California"

        self.assertEqual(state.name, "California")

    def test_to_dict(self):
        """Test the to_dict() method of State class"""
        state = State()
        state.name = "California"

        state_dict = state.to_dict()

        self.assertEqual(state_dict["name"], "California")
        self.assertEqual(state_dict["__class__"], "State")
        self.assertIn("id", state_dict)
        self.assertIn("created_at", state_dict)
        self.assertIn("updated_at", state_dict)


if __name__ == '__main__':
    unittest.main()

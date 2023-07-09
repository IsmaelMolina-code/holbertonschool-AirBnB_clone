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
        self.assertIsInstance(state.name, str)

        state.name = "Montevideo"
        self.assertEqual(state.name, "Montevideo")

    def test_to_dict(self):

        state = State()
        state.name = "Montevideo"

        state_dict = state.to_dict()

        self.assertEqual(state_dict["name"], "Montevideo")
        self.assertEqual(state_dict["__class__"], "State")
        self.assertIn("id", state_dict)
        self.assertIn("created_at", state_dict)
        self.assertIn("updated_at", state_dict)

    def test_str_representation(self):

        state = State()
        state.name = "Montevideo"

        expected_str = "[State] ({}) {}".format(state.id, state.__dict__)
        self.assertEqual(str(state), expected_str)


if __name__ == '__main__':
    unittest.main()

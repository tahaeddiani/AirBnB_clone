#!/usr/bin/python3
"""
Test for base model
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid


class TestBaseModel(unittest.TestCase):
    """
    Test cases
    """
    def test_string(self):
        """
        checks the string
        """
        base = BaseModel()
        self.assertEqual(base.__str__(),
                         f"[{type(base).__name__}] \
({base.id}) {base.__dict__}")

    def test_to_diction(self):
        """
        checks the to_dict()
        """
        base = BaseModel()
        prvs_time = base.updated_at
        self.assertDictEqual(base.to_dict(),
                             {'__class__': type(base).__name__,
                              'updated_at': base.updated_at.isoformat(),
                              'id': base.id,
                              'created_at': base.created_at.isoformat()})
        base.save()
        self.assertNotEqual(prvs_time, base.updated_at)

    def test_attrb(self):
        """
        checks if the right classes
        """
        base = BaseModel()
        base2 = BaseModel()
        self.assertIsInstance(base.id, str)
        self.assertIsInstance(base.created_at, datetime)
        self.assertIsInstance(base.updated_at, datetime)
        self.assertNotEqual(base.id, base2.id)

    def test_save(self):
        """
        tests the save method
        """
        base = BaseModel()
        prvstime = base.updated_at
        base.save()
        newtime = base.updated_at
        self.assertNotEqual(prvstime, newtime)

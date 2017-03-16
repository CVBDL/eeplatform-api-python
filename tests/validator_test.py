#!/usr/bin/env python

"""Tests for eeplatform_api.validator module."""

import unittest

from eeplatform_api.validator import Validator


class ValidatorTest(unittest.TestCase):

    def test_is_valid_endpoint(self):
        root_endpoint = 'http://localhost:3000/api/v1'
        self.assertEqual(Validator.is_valid_endpoint(None), False)
        self.assertEqual(Validator.is_valid_endpoint(root_endpoint), True)

    def test_is_valid_id(self):
        id = '58b12147a1e9b417886d3c01'
        self.assertEqual(Validator.is_valid_id(None), False)
        self.assertEqual(Validator.is_valid_id(''), False)
        self.assertEqual(Validator.is_valid_id(id), True)

    def test_is_valid_payload(self):
        payload = {'description': 'sample text'}
        self.assertEqual(Validator.is_valid_payload(None), False)
        self.assertEqual(Validator.is_valid_payload(''), False)
        self.assertEqual(Validator.is_valid_payload(payload), True)

    def test_is_valid_task_state(self):
        self.assertEqual(Validator.is_valid_task_state('running'), True)
        self.assertEqual(Validator.is_valid_task_state('success'), True)
        self.assertEqual(Validator.is_valid_task_state('failure'), True)
        self.assertEqual(Validator.is_valid_task_state(''), False)
        self.assertEqual(Validator.is_valid_task_state(None), False)


if __name__ == '__main__':
    unittest.main()

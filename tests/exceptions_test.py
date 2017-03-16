#!/usr/bin/env python

"""Tests for eeplatform_api.exceptions module."""

import unittest

from eeplatform_api.exceptions import InvalidArgumentError


class InvalidArgumentErrorTest(unittest.TestCase):

    def test_main(self):
        self.assertEqual(issubclass(InvalidArgumentError, Exception), True)
        
        def make_exception():
            raise InvalidArgumentError()

        self.assertRaises(InvalidArgumentError, make_exception)


if __name__ == '__main__':
    unittest.main()

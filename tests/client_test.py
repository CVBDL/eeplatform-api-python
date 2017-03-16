#!/usr/bin/env python

"""Tests for eeplatform_api.client module."""

import unittest

from eeplatform_api.chart import Chart
from eeplatform_api.client import EagleEyePlatformClient
from eeplatform_api.exceptions import InvalidArgumentError
from eeplatform_api.task import Task


class EagleEyePlatformClientTest(unittest.TestCase):

    root_endpoint = 'http://localhost:3000/api/v1'

    def test_init(self):
        client = EagleEyePlatformClient(self.root_endpoint)

        self.assertEqual(client.root_endpoint, self.root_endpoint)
        self.assertTrue(isinstance(client.chart, Chart))
        self.assertTrue(isinstance(client.task, Task))

        def use_invalid_root_endpoint():
            EagleEyePlatformClient('')

        self.assertRaises(InvalidArgumentError, use_invalid_root_endpoint)


if __name__ == '__main__':
    unittest.main()

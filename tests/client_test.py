#!/usr/bin/env python

"""Tests for the eeplatform_api module."""

import unittest

from eeplatform_api.chart import Chart
from eeplatform_api.client import EagleEyePlatformClient
from eeplatform_api.exceptions import InvalidArgumentError


root_endpoint = 'http://localhost:3000/api/v1'


class EagleEyePlatformClientTest(unittest.TestCase):

    def test_init(self):
        client = EagleEyePlatformClient(root_endpoint)
        self.assertEqual(client.root_endpoint, root_endpoint)
        self.assertTrue(isinstance(client.chart, Chart))

    def test_invalid_root_endpoint(self):
        def create_client():
            EagleEyePlatformClient('')

        self.assertRaises(InvalidArgumentError, create_client)


if __name__ == '__main__':
    unittest.main()

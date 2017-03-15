#!/usr/bin/env python

"""Tests for the eeplatform_api module."""

import unittest

from eeplatform_api.chart import Chart
from eeplatform_api.client import EagleEyePlatformClient


root_endpoint = 'http://localhost:3000/api/v1'


class EagleEyePlatformClientTest(unittest.TestCase):

    def test_init(self):
        self.assertRaises(Exception, EagleEyePlatformClient)
        client = EagleEyePlatformClient(root_endpoint)
        self.assertEqual(client.root_endpoint, root_endpoint)
        self.assertTrue(isinstance(client.chart, Chart))


if __name__ == '__main__':
    unittest.main()

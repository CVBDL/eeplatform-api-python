#!/usr/bin/env python

"""Tests for eeplatform_api.chart module."""

import unittest
from unittest import mock

from eeplatform_api.chart import Chart
from eeplatform_api.client import EagleEyePlatformClient
from eeplatform_api.exceptions import InvalidArgumentError

import tests.requests_mock as requests_mock


class ChartTest(unittest.TestCase):

    root_endpoint = 'http://localhost:3000/api/v1'
    chart_id = '58b12147a1e9b417886d3c01'

    @mock.patch('requests.get', side_effect=requests_mock.mocked_requests_get)
    def test_list(self, mocked_requests_get):
        client = EagleEyePlatformClient(self.root_endpoint)
        client.chart.list()
        mocked_requests_get.assert_called_with(
            '{0}/charts'.format(self.root_endpoint))


    @mock.patch('requests.post',
                side_effect=requests_mock.mocked_requests_post)
    def test_update(self, mocked_requests_post):
        client = EagleEyePlatformClient(self.root_endpoint)

        def pass_invalid_id():
            client.chart.update('', {})
        
        self.assertRaises(InvalidArgumentError, pass_invalid_id)

        def pass_invalid_data():
            client.chart.update(self.chart_id, '')

        self.assertRaises(InvalidArgumentError, pass_invalid_data)

        # It should post update data to server
        client.chart.update(self.chart_id, {})
        mocked_requests_post.assert_called_with(
            '{0}/charts/{1}'.format(self.root_endpoint, self.chart_id),
            json={})


if __name__ == '__main__':
    unittest.main()

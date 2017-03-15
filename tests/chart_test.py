#!/usr/bin/env python

"""Tests for the chart module."""

import unittest
from unittest import mock

from eeplatform_api.chart import Chart
from eeplatform_api.client import EagleEyePlatformClient
from eeplatform_api.exceptions import MissingFieldError


root_endpoint = 'http://localhost:3000/api/v1'
chart_id = '58b12147a1e9b417886d3c01'
headers = {'content-type': 'application/json'}


def mocked_requests_post(url, data=None, json=None, **kwargs):
    class MockResponse:
        text = 'response text'

        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    return MockResponse({'_id': chart_id, 'datatable': {}}, 200)


class ChartTest(unittest.TestCase):

    @mock.patch('requests.post', side_effect=mocked_requests_post)
    def test_update(self, mocked_requests_post):
        client = EagleEyePlatformClient(root_endpoint)

        # It should raise 'MissingFieldError' exception if no id provided
        self.assertRaises(MissingFieldError, client.chart.update)

        # It should raise 'MissingFieldError' exception if no data provided
        self.assertRaises(MissingFieldError, client.chart.update, chart_id)

        # It should post update data to server
        client.chart.update(chart_id, {})
        mocked_requests_post.assert_called_with(
            root_endpoint + '/charts/' + chart_id,
            json={})


if __name__ == '__main__':
    unittest.main()

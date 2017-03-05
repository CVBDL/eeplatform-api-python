#!/usr/bin/env python

"""Tests for the eeplatform_api module."""

from eeplatform_api import EagleEyePlatformClient
from eeplatform_api import MissingFieldError
from unittest import mock
import unittest

__author__ = "Patrick Zhong"


chart_id = '58b12147a1e9b417886d3c01'
headers = {'content-type': 'application/json'}


def mocked_requests_post(url, data=None, json=None, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    return MockResponse({'_id': chart_id, 'datatable': {}}, 200)


class EagleEyePlatformClientTest(unittest.TestCase):

    @mock.patch('requests.post', side_effect=mocked_requests_post)
    def test_update_chart(self, mocked_requests_post):
        client = EagleEyePlatformClient()

        # It should raise 'MissingFieldError' exception if no id provided
        self.assertRaises(MissingFieldError,
                          client.update_chart)

        # It should raise 'MissingFieldError' exception if no data provided
        self.assertRaises(MissingFieldError,
                          client.update_chart,
                          chart_id)

        # It should post update data to server
        client.update_chart(chart_id, {})
        mocked_requests_post.assert_called_with(
            'http://localhost:3000/api/v1/charts/' + chart_id,
            headers=headers,
            data={})


if __name__ == '__main__':
    unittest.main()

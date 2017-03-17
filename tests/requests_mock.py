"""Mock requests library."""

import json as lib_json


chart_id = '58b12147a1e9b417886d3c01'
chart = {
    '_id': chart_id,
    'description': 'sample desc'
}


class MockResponse:
    """Mock the response"""

    def __init__(self, status_code, json_data):
        self.status_code = status_code
        self.json_data = json_data

        if json_data is None:
            self.text = None
        else:
            self.text = lib_json.dumps(json_data)

    def json(self):
        return self.json_data


def mocked_requests_get(url):
    return MockResponse(200, [chart])


def mocked_requests_post(url, json=None, **kwargs):
    return MockResponse(200, json)

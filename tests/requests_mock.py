"""Mock requests library."""

import json as lib_json


chart = {
    '_id': '58b12147a1e9b417886d3c01',
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


def mocked_requests_get_many(url):
    return MockResponse(200, [chart])


def mocked_requests_get_one(url):
    return MockResponse(200, chart)


def mocked_requests_post(url, json=None, **kwargs):
    return MockResponse(200, json)


def mocked_requests_put(url, json=None, **kwargs):
    return MockResponse(200, json)


def mocked_requests_delete(url):
    return MockResponse(204, None)

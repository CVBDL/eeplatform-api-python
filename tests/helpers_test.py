import unittest
import json as lib_json

from eeplatform_api.helpers import RequestHelper


class HelpersTest(unittest.TestCase, RequestHelper):

    def test_respond(self):

        class MockReq:

            def __init__(self, status_code, text):
                self.status_code = status_code
                self.text = text

            def json(self):
                return lib_json.loads(self.text)

        response = {'description': 'sample'}
        req = MockReq(200, lib_json.dumps(response))
        result = super().respond(req)
        self.assertEqual(result, (200, response))

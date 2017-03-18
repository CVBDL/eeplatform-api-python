import unittest
from unittest import mock

from eeplatform_api.client import EagleEyePlatformClient
from eeplatform_api.exceptions import InvalidArgumentError

import tests.requests_mock as requests_mock


class TaskTest(unittest.TestCase):

    root_endpoint = 'http://localhost:3000/api/v1'
    task_id = '58b12147a1e9b417886d3c12'
    state = 'success'

    @mock.patch('requests.put',
                side_effect=requests_mock.mocked_requests_put)
    def test_update_state(self, mocked_requests_put):
        client = EagleEyePlatformClient(self.root_endpoint)

        def pass_invalid_id():
            client.task.update_state(None, self.state)

        self.assertRaises(InvalidArgumentError, pass_invalid_id)

        def pass_invalid_state():
            client.task.update_state(self.task_id, None)

        self.assertRaises(InvalidArgumentError, pass_invalid_state)

        client.task.update_state(self.task_id, self.state)
        mocked_requests_put.assert_called_with(
            '{0}/tasks/{1}'.format(self.root_endpoint, self.task_id),
            json={'state': self.state})


if __name__ == '__main__':
    unittest.main()

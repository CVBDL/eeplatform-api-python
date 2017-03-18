"""EagleEye Platform task resource.

See https://github.com/CVBDL/EagleEye-Docs/blob/master/rest-api/rest-api.md#tasks
"""

import requests

from eeplatform_api.exceptions import InvalidArgumentError
from eeplatform_api.helpers import RequestHelper
from eeplatform_api.validator import Validator


class Task(RequestHelper):
    """The task APIs.

    Args:
        root_endpoint (str): The EagleEye Platform API root endpoint.

    Attributes:
        root_endpoint (str): The EagleEye Platform API root endpoint.
    """

    _arg_error_msg = 'Invalid required positional argument: "{0}"'

    def __init__(self, root_endpoint):
        self.root_endpoint = root_endpoint

    def update_state(self, id, state):
        """Edit task state.

        Args:
            id (str): The "_id" field of a chart.
            state (str): The task state.  One of 'running', 'success'
                         or 'failure'

        Returns:
            A tuple contains status code and JSON chart data.

        Raises:
            InvalidArgumentError: Either chart id or task state
                                  is invalid.
        """
        if not Validator.is_valid_id(id):
            raise InvalidArgumentError(self._arg_error_msg.format('id'))
        if not Validator.is_valid_task_state(state):
            raise InvalidArgumentError(self._arg_error_msg.format('state'))

        req = requests.put('{0}/tasks/{1}'.format(self.root_endpoint, id),
                           json={'state': state})
        return super().respond(req)

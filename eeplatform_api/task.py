"""EagleEye Platform task API.
See https://github.com/CVBDL/EagleEye-Docs/blob/master/rest-api/rest-api.md#tasks
"""

import requests

from eeplatform_api.exceptions import InvalidArgumentError
from eeplatform_api.helpers import RequestHelper
from eeplatform_api.validator import Validator


class Task(RequestHelper):
    """The task resource class for internal use."""

    arg_error_msg = 'Invalid required positional argument: "{0}"'

    def __init__(self, root_endpoint):
        self.root_endpoint = root_endpoint

    def updateState(self, id, state):
        """Edit a task."""

        if not Validator.is_valid_id(id):
            raise InvalidArgumentError(self.arg_error_msg.format('id'))
        if not Validator.is_valid_task_state(state):
            raise InvalidArgumentError(self.arg_error_msg.format('state'))

        req = requests.put('{0}/tasks/{1}'.format(self.root_endpoint, id),
                           json={'state': state})
        return super().respond(req)

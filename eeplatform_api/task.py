# -*- coding: utf-8 -*-
"""A Python client of EagleEye platform APIs.
Resource: task
See https://github.com/CVBDL/EagleEye-Docs/blob/master/rest-api/rest-api.md#tasks
"""

import requests

from eeplatform_api.exceptions import MissingFieldError
from eeplatform_api.helper import RequestHelper


class Task(RequestHelper):

    def __init__(self, root_endpoint=None):
        if root_endpoint is None:
            raise Exception('Missing the required "root_endpoint" parameter')
        else:
            self.root_endpoint = root_endpoint

    def updateState(self, id=None, state=None):
        """Edit a task."""
        if id is None:
            raise MissingFieldError('Missing the required "id" field.')
        if state is None:
            raise MissingFieldError('Missing the required "state" field.')

        req = requests.put('{0}/tasks/{1}'.format(self.root_endpoint, id),
                           json={'state': state})
        return super().respond(req)

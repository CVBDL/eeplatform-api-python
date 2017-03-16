"""A Python client of EagleEye platform APIs.

See https://github.com/CVBDL/EagleEye-Docs/blob/master/rest-api/rest-api.md
"""

from eeplatform_api.chart import Chart
from eeplatform_api.exceptions import InvalidArgumentError
from eeplatform_api.task import Task
from eeplatform_api.validator import Validator


class EagleEyePlatformClient:
    """EagleEye Platform API Client"""

    def __init__(self, root_endpoint):
        if not Validator.is_valid_endpoint(root_endpoint):
            raise InvalidArgumentError(
                'Invalid required positional argument: "root_endpoint"')
        else:
            self.root_endpoint = root_endpoint

        self.chart = Chart(root_endpoint)
        self.task = Task(root_endpoint)

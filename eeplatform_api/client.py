"""EagleEye Platform API Client.

See https://github.com/CVBDL/EagleEye-Docs/blob/master/rest-api/rest-api.md
"""

from eeplatform_api.chart import Chart
from eeplatform_api.exceptions import InvalidArgumentError
from eeplatform_api.task import Task
from eeplatform_api.validator import Validator


class EagleEyePlatformClient:
    """API Client class.

    Args:
        root_endpoint (str): The EagleEye Platform API root endpoint.

    Attributes:
        root_endpoint (str): The EagleEye Platform API root endpoint.
        chart: An object provides EagleEye Platform chart APIs.
        task:  An object provides EagleEye Platform task APIs.

    Examples:
        client = EagleEyePlatformClient(root_endpoint)

        # List all charts
        client.chart.list()

        # Update task state
        client.task.updateState(id, state)

    Raises:
        InvalidArgumentError: The API root endpoint is invalid.
    """

    _arg_error_msg = 'Invalid required positional argument: "{0}"'

    def __init__(self, root_endpoint):
        if not Validator.is_valid_endpoint(root_endpoint):
            raise InvalidArgumentError(
                self._arg_error_msg.format('root_endpoint'))
        else:
            self.root_endpoint = root_endpoint

        self.chart = Chart(root_endpoint)
        self.task = Task(root_endpoint)

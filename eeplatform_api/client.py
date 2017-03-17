"""EagleEye Platform API Client.

See https://github.com/CVBDL/EagleEye-Docs/blob/master/rest-api/rest-api.md
"""

from eeplatform_api.chart import Chart
from eeplatform_api.exceptions import InvalidArgumentError
from eeplatform_api.task import Task
from eeplatform_api.validator import Validator


class EagleEyePlatformClient:
    """API Client class.

    Attributes:
      chart: An object provides EagleEye Platform chart APIs.
      task:  An object provides EagleEye Platform task APIs.
    """

    _arg_error_msg = 'Invalid required positional argument: "{0}"'

    def __init__(self, root_endpoint):
        """Create an API client.
        
        Args:
          root_endpoint: The EagleEye Platform API root endpoint.

        Returns:
          An EagleEye Platform client instance.
          Then, you're able to call APIs via this object.
          Examples:
            client = EagleEyePlatformClient(root_endpoint)
            # List all charts
            client.chart.list()
            # Update task state
            client.task.updateState(id, state)

        Raises:
          InvalidArgumentError: The API root endpoint is invalid.
        """
        if not Validator.is_valid_endpoint(root_endpoint):
            raise InvalidArgumentError(
                self._arg_error_msg.format('root_endpoint'))
        else:
            self.root_endpoint = root_endpoint

        self.chart = Chart(root_endpoint)
        self.task = Task(root_endpoint)

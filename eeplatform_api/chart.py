"""EagleEye Platform chart resource.

See https://github.com/CVBDL/EagleEye-Docs/blob/master/rest-api/rest-api.md#charts
"""

import requests

from eeplatform_api.exceptions import InvalidArgumentError
from eeplatform_api.helpers import RequestHelper
from eeplatform_api.validator import Validator


class Chart(RequestHelper):
    """The chart APIs.

    Args:
        root_endpoint (str): The EagleEye Platform API root endpoint.

    Attributes:
        root_endpoint (str): The EagleEye Platform API root endpoint.
    """

    _arg_error_msg = 'Invalid required positional argument: "{0}"'

    def __init__(self, root_endpoint):
        self.root_endpoint = root_endpoint

    def list(self):
        """List charts.

        Returns:
            A tuple contains status code and JSON chart list.
        """
        req = requests.get('{0}/charts'.format(self.root_endpoint))
        return super().respond(req)

    def get(self, id):
        """Get one chart.
        
        Args:
            id (str): The "_id" field of a chart.

        Returns:
            A tuple contains status code and JSON chart data.

        Raises:
            InvalidArgumentError: The chart id is invalid.
        """
        if not Validator.is_valid_id(id):
            raise InvalidArgumentError(self._arg_error_msg.format('id'))

        req = requests.get('{0}/charts/{1}'.format(self.root_endpoint, id))
        return super().respond(req)

    def create(self, data):
        """Create a chart.
        
        Args:
            data (dict): The new chart's data.

        Returns:
            A tuple contains status code and JSON chart data.

        Raises:
            InvalidArgumentError: The chart data dict is invalid.
        """
        if not Validator.is_valid_payload(data):
            raise InvalidArgumentError(self._arg_error_msg.format('data'))

        req = requests.post('{0}/charts'.format(self.root_endpoint), json=data)
        return super().respond(req)

    def update(self, id, data):
        """Edit a chart.
        
        Args:
            id (str): The "_id" field of a chart.
            data (dict): The update data of a chart.

        Returns:
            A tuple contains status code and JSON chart data.

        Raises:
            InvalidArgumentError: Either chart id or data is invalid.
        """
        if not Validator.is_valid_id(id):
            raise InvalidArgumentError(self._arg_error_msg.format('id'))
        if not Validator.is_valid_payload(data):
            raise InvalidArgumentError(self._arg_error_msg.format('data'))

        req = requests.post('{0}/charts/{1}'.format(self.root_endpoint, id),
                            json=data)
        return super().respond(req)

    def delete(self, id):
        """Delete a chart.
        
        Args:
            id (str): The "_id" field of a chart.

        Returns:
            A tuple contains status code and JSON response.

        Raises:
            InvalidArgumentError: The chart id is invalid.
        """
        if not Validator.is_valid_id(id):
            raise InvalidArgumentError(self._arg_error_msg.format('id'))

        req = requests.delete('{0}/charts/{1}'.format(self.root_endpoint, id))
        return super().respond(req)

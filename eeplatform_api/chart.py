# -*- coding: utf-8 -*-
"""A Python client of EagleEye platform APIs.
Resource: chart
See https://github.com/CVBDL/EagleEye-Docs/blob/master/rest-api/rest-api.md#charts
"""

import requests


class Chart:

    def __init__(self, root_endpoint=None):
        if root_endpoint is None:
            raise Exception('Missing the required "root_endpoint" parameter')
        else:
            self.root_endpoint = root_endpoint

    def _respond(self, req):
        req.encoding = 'utf-8'
        if len(req.text) > 0:
            return (req.status_code, req.json())
        else:
            return (req.status_code, None)

    def list(self):
        """List charts."""
        req = requests.get('{0}/charts'.format(self.root_endpoint))
        return self._respond(req)

    def get(self, id=None):
        """Get one chart."""
        if id is None:
            raise MissingFieldError('Missing the required "id" field.')

        req = requests.get('{0}/charts/{1}'.format(self.root_endpoint, id))
        return self._respond(req)

    def create(self, data=None):
        """Create a chart."""
        if data is None:
            raise MissingFieldError('Missing chart data.')

        req = requests.post('{0}/charts'.format(self.root_endpoint),
                            json=data)
        return self._respond(req)

    def update(self, id=None, data=None):
        """Edit a chart."""
        if id is None:
            raise MissingFieldError('Missing the required "id" field.')
        if data is None:
            raise MissingFieldError('Missing update chart data.')

        req = requests.post('{0}/charts/{1}'.format(self.root_endpoint, id),
                            json=data)
        return self._respond(req)

    def delete(self, id=None):
        """Delete a chart."""
        if id is None:
            raise MissingFieldError('Missing the required "id" field.')
        req = requests.delete('{0}/charts/{1}'.format(self.root_endpoint, id))
        return self._respond(req)


class MissingFieldError(Exception):
    """This means a required field on a resource has not been set."""
    pass

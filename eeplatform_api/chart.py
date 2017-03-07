#!/usr/bin/env python

"""A Python client of EagleEye platform APIs.
Resource: chart
See https://github.com/CVBDL/EagleEye-Docs/blob/master/rest-api/rest-api.md#charts
"""

import json
import logging
import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('chart')


class Chart:

    headers = {'content-type': 'application/json'}

    def __init__(self, root_endpoint=None):
        if root_endpoint is None:
            raise Exception('Missing the required "root_endpoint" parameter')
        else:
            self.root_endpoint = root_endpoint
    
    def update(self, id=None, data=None):
        if id is None:
            raise MissingFieldError('Missing the required "id" field.')
        if data is None:
            raise MissingFieldError('Missing the required "datatable" field.')

        req = requests.post('{0}/charts/{1}'.format(self.root_endpoint, id),
                            headers=self.headers,
                            data=data)
        return req.json()


class MissingFieldError(Exception):
    """This means a required field on a resource has not been set."""
    pass

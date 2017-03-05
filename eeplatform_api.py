#!/usr/bin/env python

"""A Python client of EagleEye platform APIs.

See https://github.com/CVBDL/EagleEye-Docs/blob/master/rest-api/rest-api.md
"""

import json
import requests


__author__ = "Patrick Zhong"


# Reading EagleEye Platform API configurations.
config_file = 'eeplatform_api.config.json'
try:
    with open(config_file) as file:
        config = json.load(file)
        if config['root_endpoint']:
            ROOT_ENDPOINT = config['root_endpoint']
except Exception as e:
    ROOT_ENDPOINT = 'http://localhost:3000/api/v1'
    print(e)


class EagleEyePlatformClient:
    """EagleEye Platform API Client"""

    def __init__(self):
        self.headers = {'content-type': 'application/json'}

    def update_chart(self, id=None, data=None):
        if id is None:
            raise MissingFieldError('Missing the required id field.')
        if data is None:
            raise MissingFieldError('Missing the required datatable field.')

        req = requests.post('{0}/charts/{1}'.format(ROOT_ENDPOINT, id),
                            headers=self.headers,
                            data=data)
        return req.json()


class MissingFieldError(Exception):
    """This means a required field on a resource has not been set."""
    pass

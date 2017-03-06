#!/usr/bin/env python

"""A Python client of EagleEye platform APIs.

See https://github.com/CVBDL/EagleEye-Docs/blob/master/rest-api/rest-api.md
"""

import json
import logging
import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('eeplatform_api')

default_root_endpoint = r'http://localhost:3000/api/v1'

# Reading EagleEye Platform API configurations.
config_filename = 'eeplatform_api.configa.json'
try:
    with open(config_filename) as config_file:
        config = json.load(config_file)
        if config['root_endpoint']:
            ROOT_ENDPOINT = config['root_endpoint']
        else:
            ROOT_ENDPOINT = default_root_endpoint
except Exception as e:
    ROOT_ENDPOINT = default_root_endpoint
    logger.error('Failed to read configuration file: %s', e)
finally:
    logger.info('EagleEye Platform API root endpoint is set to: "%s"',
                ROOT_ENDPOINT)


class EagleEyePlatformClient:
    """EagleEye Platform API Client"""

    headers = {'content-type': 'application/json'}

    def update_chart(self, id=None, data=None):
        if id is None:
            raise MissingFieldError('Missing the required "id" field.')
        if data is None:
            raise MissingFieldError('Missing the required "datatable" field.')

        req = requests.post('{0}/charts/{1}'.format(ROOT_ENDPOINT, id),
                            headers=self.headers,
                            data=data)
        return req.json()


class MissingFieldError(Exception):
    """This means a required field on a resource has not been set."""
    pass

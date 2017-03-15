# -*- coding: utf-8 -*-
"""A Python client of EagleEye platform APIs.

See https://github.com/CVBDL/EagleEye-Docs/blob/master/rest-api/rest-api.md
"""

from eeplatform_api.chart import Chart
from eeplatform_api.task import Task


class EagleEyePlatformClient:
    """EagleEye Platform API Client"""

    def __init__(self, root_endpoint=None):
        if root_endpoint is None:
            raise Exception('Missing the required "root_endpoint" parameter')
        else:
            self.root_endpoint = root_endpoint

        self.chart = Chart(root_endpoint)
        self.task = Task(root_endpoint)

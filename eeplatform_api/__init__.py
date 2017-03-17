"""EagleEye Platform API Client.

A tool for using EagleEye Platform APIs easily.

Usage:

from eeplatform_api.client import EagleEyePlatformClient

client = EagleEyePlatformClient(root_endpoint)

# List all charts
client.chart.list()
    => (status_code, response_data)

# Get one chart by id
client.chart.get(chart_id)
    => (status_code, response_data)

# Create a new chart
client.chart.create(chart_data)
    => (status_code, response_data)

# Update a chart
client.chart.update(chart_id, chart_data)
    => (status_code, response_data)

# Delete a chart
client.chart.delete(chart_id)
    => (status_code, response_data)

# Update task state
client.task.updateState(task_id, state)
    => (status_code, response_data)
"""

__version__ = '0.1'

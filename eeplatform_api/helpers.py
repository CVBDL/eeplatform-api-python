"""EagleEye Platform API helper calsses."""

__all__ = ('RequestHelper')


class RequestHelper:
    """HTTP request helper class"""

    def respond(self, req):
        req.encoding = 'utf-8'
        if len(req.text) > 0:
            return req.status_code, req.json()
        else:
            return req.status_code, None

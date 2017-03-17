"""EagleEye Platform API helper calsses."""

__all__ = ('RequestHelper')


class RequestHelper:
    """HTTP request helper class"""

    def respond(self, req):
        """Wrap response data.

        Args:
            req: A requests object.

        Returns:
            A tuple contains status code and response JSON data.
        """
        req.encoding = 'utf-8'
        if req.text is not None and len(req.text) > 0:
            return req.status_code, req.json()
        else:
            return req.status_code, None

"""Global exception classes."""


class MissingFieldError(Exception):
    """This means a required field on a resource has not been set."""
    pass

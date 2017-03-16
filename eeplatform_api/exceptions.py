"""Global exception classes."""

__all__ = ('InvalidArgumentError')


class InvalidArgumentError(Exception):
    """This means a required argument has a wrong type or value."""
    pass

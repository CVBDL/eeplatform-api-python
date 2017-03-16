"""Provide some static validator methods."""

__all__ = ('Validator')


class Validator:
    """Validator class."""

    @staticmethod
    def is_valid_endpoint(endpoint):
        """Should be a valid URL."""
        return isinstance(endpoint, str) and endpoint.startswith('http')

    @staticmethod
    def is_valid_id(id):
        """MongoDB ObjectID id is a 24 byte hex string."""
        return isinstance(id, str) and len(id)==24

    @staticmethod
    def is_valid_payload(payload):
        """Payload should be a dict type."""
        return isinstance(payload, dict)

    @staticmethod
    def is_valid_task_state(state):
        """Valid task states are: running, success and failure."""
        valid_states = ('running', 'success', 'failure')
        return state in valid_states

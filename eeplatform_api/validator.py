"""Validator module."""

__all__ = ('Validator')


class Validator:
    """Provide some static validators."""

    @staticmethod
    def is_valid_endpoint(endpoint):
        """Validate API endpoint."""
        return isinstance(endpoint, str) and endpoint.startswith('http')

    @staticmethod
    def is_valid_id(id):
        """Validate MongoDB ObjectId."""
        return isinstance(id, str) and len(id)==24

    @staticmethod
    def is_valid_payload(payload):
        """Validate request payload."""
        return isinstance(payload, dict)

    @staticmethod
    def is_valid_task_state(state):
        """Validate task state."""
        valid_states = ('running', 'success', 'failure')
        return state in valid_states

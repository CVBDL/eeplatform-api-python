"""Validator module."""

__all__ = ('Validator')


class Validator:
    """Provide some static validators."""

    @staticmethod
    def is_valid_endpoint(endpoint):
        """Validate API endpoint.

        Args:
            endpoint (str): API endpoint.

        Returns:
            bool: The return value. True for valid, False for invalid.
        """
        return isinstance(endpoint, str) and endpoint.startswith('http')

    @staticmethod
    def is_valid_id(id):
        """Validate MongoDB ObjectId.

        Args:
            id (str): Resource id in EagleEye Platform.

        Returns:
            bool: The return value. True for valid, False for invalid.
        """
        return isinstance(id, str) and len(id) == 24

    @staticmethod
    def is_valid_payload(payload):
        """Validate request payload.

        Args:
            payload (dict): Request payload data.

        Returns:
            bool: The return value. True for valid, False for invalid.
        """
        return isinstance(payload, dict)

    @staticmethod
    def is_valid_task_state(state):
        """Validate task state.

        Args:
            state (str): Task state in EagleEye Platform.
                         One of 'running', 'success' or 'failure'.

        Returns:
            bool: The return value. True for valid, False for invalid.
        """
        valid_states = ('running', 'success', 'failure')
        return state in valid_states

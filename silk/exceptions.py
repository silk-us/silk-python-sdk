class ApiError(Exception):
    """Exception raised for errors in the API."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class ValidationError(Exception):
    """Exception raised for validation errors."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
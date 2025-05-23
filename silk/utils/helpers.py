def format_response(response):
    """Format the API response for easier consumption."""
    if response.status_code == 200:
        return response.json()
    else:
        handle_error(response)

def handle_error(response):
    """Handle errors returned by the API."""
    error_message = f"Error {response.status_code}: {response.text}"
    raise Exception(error_message)
from silk.api.clients import ApiClient
from silk.api.hosts import create_host

def main():
    # Initialize the API client
    client = ApiClient()

    # Define the host details
    host_details = {
        "name": "New Host",
        "description": "This is a new host created for demonstration purposes.",
        "ip_address": "192.168.1.10",
        "other_config": {
            "cpu": "4 cores",
            "memory": "16GB"
        }
    }

    try:
        # Create a new host using the SDK
        response = create_host(client, host_details)
        print("Host created successfully:", response)
    except Exception as e:
        print("An error occurred while creating the host:", str(e))

if __name__ == "__main__":
    main()
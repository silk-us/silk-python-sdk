# Example of a workflow using the Silk Python SDK

from silk.api.clients import ApiClient
from silk.api.hosts import create_host, modify_host
from silk.workflows.example_workflow import run_example_workflow

def main():
    # Initialize the API client
    client = ApiClient(api_key='your_api_key_here')

    # Example: Create a new host
    host_data = {
        'name': 'New Host',
        'ip_address': '192.168.1.1',
        'description': 'This is a new host created for demonstration purposes.'
    }
    
    new_host = create_host(client, host_data)
    print(f'Created Host: {new_host}')

    # Example: Modify the created host
    modified_data = {
        'description': 'Updated description for the new host.'
    }
    
    updated_host = modify_host(client, new_host['id'], modified_data)
    print(f'Updated Host: {updated_host}')

    # Run an example workflow
    run_example_workflow(client)

if __name__ == '__main__':
    main()
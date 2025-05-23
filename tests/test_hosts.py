import unittest
from silk.api.hosts import create_host, modify_host
from silk.exceptions import ApiError

class TestHosts(unittest.TestCase):

    def test_create_host_success(self):
        # Assuming create_host returns a host object on success
        host_data = {
            "name": "Test Host",
            "ip_address": "192.168.1.1"
        }
        host = create_host(host_data)
        self.assertIsNotNone(host)
        self.assertEqual(host.name, host_data["name"])
        self.assertEqual(host.ip_address, host_data["ip_address"])

    def test_create_host_failure(self):
        # Test for failure when invalid data is provided
        invalid_host_data = {
            "name": "",  # Invalid name
            "ip_address": "192.168.1.1"
        }
        with self.assertRaises(ApiError):
            create_host(invalid_host_data)

    def test_modify_host_success(self):
        # Assuming modify_host returns a modified host object
        host_id = "12345"
        updated_data = {
            "name": "Updated Host"
        }
        modified_host = modify_host(host_id, updated_data)
        self.assertIsNotNone(modified_host)
        self.assertEqual(modified_host.name, updated_data["name"])

    def test_modify_host_failure(self):
        # Test for failure when trying to modify a non-existent host
        invalid_host_id = "invalid_id"
        updated_data = {
            "name": "Updated Host"
        }
        with self.assertRaises(ApiError):
            modify_host(invalid_host_id, updated_data)

if __name__ == '__main__':
    unittest.main()
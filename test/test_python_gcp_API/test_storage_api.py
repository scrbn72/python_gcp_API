import unittest
from unittest.mock import patch, MagicMock
from src.python_gcp_API.libraries.storage_api import StorageAPI

class TestStorageAPI(unittest.TestCase):

    @patch('libraries.storage_api.storage.Client')
    def test_bucket_exists_true(self, mock_client):
        # Mock the Storage client
        mock_instance = MagicMock()
        mock_client.return_value = mock_instance
        mock_instance.get_bucket.return_value = True

        storage_api = StorageAPI()
        self.assertTrue(storage_api.bucket_exists('bucket_name'))
        mock_instance.get_bucket.assert_called_once()

    @patch('libraries.storage_api.storage.Client')
    def test_bucket_exists_false(self, mock_client):
        # Mock the Storage client to raise an exception
        mock_instance = MagicMock()
        mock_client.return_value = mock_instance
        mock_instance.get_bucket.side_effect = Exception("Bucket not found")

        storage_api = StorageAPI()
        self.assertFalse(storage_api.bucket_exists('bucket_name'))
        mock_instance.get_bucket.assert_called_once()

if __name__ == '__main__':
    unittest.main()
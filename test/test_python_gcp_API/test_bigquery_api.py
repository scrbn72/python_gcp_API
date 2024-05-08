import unittest
from unittest.mock import patch, MagicMock
from src.python_gcp_API.libraries.bigquery_api import BigQueryAPI

class TestBigQueryAPI(unittest.TestCase):

    @patch('libraries.bigquery_api.bigquery.Client')
    def test_table_exists_true(self, mock_client):

        mock_instance = MagicMock()
        mock_client.return_value = mock_instance
        mock_instance.get_table.return_value = True

        bigquery_api = BigQueryAPI()
        self.assertTrue(bigquery_api.table_exists('dataset_id', 'table_id'))
        mock_instance.get_table.assert_called_once()

    @patch('libraries.bigquery_api.bigquery.Client')
    def test_table_exists_false(self, mock_client):

        mock_instance = MagicMock()
        mock_client.return_value = mock_instance
        mock_instance.get_table.side_effect = Exception("Table not found")

        bigquery_api = BigQueryAPI()
        self.assertFalse(bigquery_api.table_exists('dataset_id', 'table_id'))
        mock_instance.get_table.assert_called_once()

if __name__ == '__main__':
    unittest.main()
from google.cloud import bigquery

class BigQueryAPI:
    def __init__(self, project_id: str):
        self.project_id = project_id
        self.client = bigquery.Client()

    def table_exists(self, dataset_id, table_id):
        """Check if a BigQuery table exists."""
        try:
            self.client.get_table(f"{self.project_id}.{dataset_id}.{table_id}")
            print(f"Table {dataset_id}.{table_id} exists.")
            return True
        except Exception as e:
            print(f"Table {dataset_id}.{table_id} does not exist: {e}")
            return False
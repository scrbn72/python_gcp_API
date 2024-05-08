from google.cloud import storage

class StorageAPI:
    def __init__(self, project_id: str):
        self.project_id = project_id
        self.client = storage.Client()

    def bucket_exists(self, bucket_name):
        """Check if a Cloud Storage bucket exists."""
        try:
            bucket = self.client.get_bucket(bucket_name)
            print(f"Bucket {bucket_name} exists.")
            return True
        except Exception as e:
            print(f"Bucket {bucket_name} does not exist: {e}")
            return False
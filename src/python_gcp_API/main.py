from libraries.bigquery_api import BigQueryAPI
from libraries.storage_api import StorageAPI
from utils.credentials import use_default_credentials

def main():

    use_default_credentials()


    bigquery_api = BigQueryAPI()
    storage_api = StorageAPI()


    dataset_id = ""
    table_id = ""
    bucket_name = ""

    bigquery_api.table_exists(dataset_id, table_id)
    storage_api.bucket_exists(bucket_name)

if __name__ == "__main__":
    main()
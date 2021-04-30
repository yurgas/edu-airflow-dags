import os

from airflow import models
from airflow.models import Variable
from airflow.providers.google.cloud.transfers.gcs_to_local import GCSToLocalFilesystemOperator
from airflow.utils.dates import days_ago

PROJECT_ID = Variable.get("gcp-project-id")
BUCKET = os.environ.get("GCP_GCS_BUCKET", "my-test-airflow-gcs-bucket")

PATH_TO_REMOTE_FILE = os.environ.get("GCP_GCS_PATH_TO_UPLOAD_FILE", "test-gcs-example-remote.txt")
PATH_TO_LOCAL_FILE = os.environ.get("GCP_GCS_PATH_TO_SAVED_FILE", "test-gcs-example-local.txt")

with models.DAG(
    "example_gcs_to_local2",
    start_date=days_ago(1),
    schedule_interval=None,
    tags=['example'],
) as dag:
    # [START howto_operator_gcs_download_file_task]
    download_file = GCSToLocalFilesystemOperator(
        task_id="download_file",
        object_name=PATH_TO_REMOTE_FILE,
        bucket=BUCKET,
        filename=PATH_TO_LOCAL_FILE,
    )
    # [END howto_operator_gcs_download_file_task]

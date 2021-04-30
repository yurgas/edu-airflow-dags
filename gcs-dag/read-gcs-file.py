import os

from airflow import models
from airflow.models import Variable
from airflow.providers.google.cloud.transfers.gcs_to_local import GCSToLocalFilesystemOperator
from airflow.utils.dates import days_ago

PROJECT_ID = Variable.get("gcp-project-id")

with models.DAG(
    "example_gcs_to_local2",
    start_date=days_ago(1),
    schedule_interval=None,
    tags=['example'],
) as dag:
    download_file = GCSToLocalFilesystemOperator(task_id="download_file",object_name="test-gcs-example-local.txt",bucket="my-test-airflow-gcs-bucket",filename="test-gcs-example-local.txt",)

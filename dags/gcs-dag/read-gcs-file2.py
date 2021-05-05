from airflow import DAG
from airflow.models import Variable
from airflow.providers.google.cloud.transfers.gcs_to_local import GCSToLocalFilesystemOperator
from airflow.utils.dates import days_ago
from datetime import timedelta

args = {
    'owner': 'airflow',
}

PROJECT_ID = Variable.get("gcp-project-id")

dag = DAG(
    dag_id='example_gcs_to_local7',
    default_args=args,
    schedule_interval='0 0 * * *',
    start_date=days_ago(1),
    dagrun_timeout=timedelta(minutes=60),
)

download_file = GCSToLocalFilesystemOperator(
    task_id='download_file2',
    object_name="abcdef",
    gcp_conn_id='my_gcp',
    bucket='my-test-airflow-gcs-bucket',
    filename='test-gcs-example-local.txt',
    dag=dag,
)

if __name__ == "__main__":
    dag.cli()

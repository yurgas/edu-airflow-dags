"""Python test import."""

from datetime import timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

from test_module.test_module import TestClass

args = {
    'owner': 'airflow',
}

dag = DAG(
    dag_id='test_import_dag',
    default_args=args,
    schedule_interval='0 0 * * *',
    start_date=days_ago(2),
    dagrun_timeout=timedelta(minutes=60),
)

run_this = BashOperator(
    task_id='echo_hello',
    bash_command='echo "Hello there"',
    dag=dag,
)

if __name__ == "__main__":
    dag.cli()

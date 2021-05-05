"""Python version validation."""

from datetime import timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

args = {
    'owner': 'airflow',
}

dag = DAG(
    dag_id='python_version_dag',
    default_args=args,
    schedule_interval='0 0 * * *',
    start_date=days_ago(2),
    dagrun_timeout=timedelta(minutes=60),
)

run_this = BashOperator(
    task_id='get_python_version',
    bash_command='python --version',
    dag=dag,
)

if __name__ == "__main__":
    dag.cli()

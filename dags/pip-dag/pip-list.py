"""Python version validation."""

from datetime import timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

args = {
    'owner': 'airflow',
}

dag = DAG(
    dag_id='pip_list_dag',
    default_args=args,
    schedule_interval='0 0 * * *',
    start_date=days_ago(2),
    dagrun_timeout=timedelta(minutes=60),
)

pip_version = BashOperator(
    task_id='get_pip_version',
    bash_command='pip --version',
    dag=dag,
)

pip_list = BashOperator(
    task_id='get_pip_list',
    bash_command='pip list',
    dag=dag,
)

pip_version >> pip_list

if __name__ == "__main__":
    dag.cli()

"""Python version validation."""

from datetime import timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

args = {
    'owner': 'airflow',
}

dag = DAG(
    dag_id='pip_list_dag_kubernetes_queue',
    default_args=args,
    schedule_interval='0 0 * * *',
    start_date=days_ago(2),
    dagrun_timeout=timedelta(minutes=60),
)

pip_list = BashOperator(
    task_id='get_pip_list',
    bash_command='pip version; pip list',
    dag=dag,
    queue="kubernetes"
)

if __name__ == "__main__":
    dag.cli()

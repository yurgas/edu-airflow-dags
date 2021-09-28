"""Python version validation."""

from datetime import timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

args = {
    'owner': 'airflow',
}

dag = DAG(
    dag_id='sleep_dag_kubernetes_queue',
    default_args=args,
    schedule_interval='0 0 * * *',
    start_date=days_ago(2),
    dagrun_timeout=timedelta(minutes=60),
)

run_this = BashOperator(
    task_id='sleep_5m',
    bash_command='sleep 300',
    dag=dag,
    queue="kubernetes"
)

if __name__ == "__main__":
    dag.cli()

"""Python version validation."""

from datetime import timedelta
import time

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

args = {
    'owner': 'airflow',
}

dag = DAG(
    dag_id='long_running_kubernetes_queue',
    default_args=args,
    schedule_interval='0 0 * * *',
    start_date=days_ago(1),
    dagrun_timeout=timedelta(minutes=60),
)

def work_in_cycle():
    """This function prints on output during long cycle"""
    for i in range(60):
        print("Iteration {}".format(i))
        time.sleep(5)
    print("Task done")

run_this = PythonOperator(
    task_id='long_running_task',
    python_callable=work_in_cycle,
    dag=dag,
    queue="kubernetes",
    executor_config={
        "KubernetesExecutor": {
            "request_memory": "128Mi",
            "request_cpu": "100m",
            "limit_memory": "256Mi",
            "limit_cpu": "100m"
        }
    }
)

if __name__ == "__main__":
    dag.cli()

"""
Пример пайплайна для ДЗ по теме 23 (п.8*–11*).
Варианты: пустой DAG (п.8*), одна задача (п.9*), зависимые задачи (п.10*).
Сейчас включены зависимые задачи; для п.8* можно оставить только dag, для п.9* — только task_start.
"""
from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="example_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
    tags=["example", "hw23"],
) as dag:
    task_start = BashOperator(
        task_id="start",
        bash_command="echo 'Pipeline started'",
    )
    task_step_a = BashOperator(
        task_id="step_a",
        bash_command="echo 'Step A done'",
    )
    task_step_b = BashOperator(
        task_id="step_b",
        bash_command="echo 'Step B done'",
    )
    task_end = BashOperator(
        task_id="end",
        bash_command="echo 'Pipeline finished'",
    )

    task_start >> task_step_a >> task_end
    task_start >> task_step_b >> task_end

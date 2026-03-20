#ML pipeline DAG для Airflow

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'mlops-team',
    'depends_on_past': False,
    'start_date': datetime(2026, 3, 15),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'example_ml_pipeline',
    default_args=default_args,
    description='Пример ML pipeline',
    schedule_interval=timedelta(days=1),
    catchup=False,
    tags=['ml', 'example'],
)

def load_data(**context):
    #Загрузка данных
    data_size = 1000
    print(f"Загружено {data_size} записей")
    context['ti'].xcom_push(key='data_size', value=data_size)

def train_model(**context):
    # Обучение модели
    data_size = context['ti'].xcom_pull(key='data_size', task_ids='load_data')
    print(f"Обучение на {data_size} записях")
    accuracy = 0.95
    print(f"Модель обучена. Accuracy: {accuracy}")
    context['ti'].xcom_push(key='accuracy', value=accuracy)

def evaluate_model(**context):
    # Оценка модели
    accuracy = context['ti'].xcom_pull(key='accuracy', task_ids='train_model')
    print(f"Accuracy: {accuracy}")

    if accuracy < 0.9:
        print("Модель не прошла критерии качества")
        raise ValueError("Model accuracy too low")

def publish_to_mlflow(**context):
    # Публикация модели в MLflow
    accuracy = context['ti'].xcom_pull(key='accuracy', task_ids='train_model')

# Определение задач
t1 = PythonOperator(
    task_id='load_data',
    python_callable=load_data,
    provide_context=True,
    dag=dag,
)

t2 = PythonOperator(
    task_id='train_model',
    python_callable=train_model,
    provide_context=True,
    dag=dag,
)

t3 = PythonOperator(
    task_id='evaluate_model',
    python_callable=evaluate_model,
    provide_context=True,
    dag=dag,
)

t4 = PythonOperator(
    task_id='publish_to_mlflow',
    python_callable=publish_to_mlflow,
    provide_context=True,
    dag=dag,
)

# Bash-задача для примера
t5 = BashOperator(
    task_id='send_notification',
    bash_command='echo "Pipeline completed successfully!"',
    dag=dag,
)

# Определение порядка выполнения
t1 >> t2 >> t3 >> t4 >> t5

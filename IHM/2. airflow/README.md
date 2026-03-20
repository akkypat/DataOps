# Этап 2: Airflow

Airflow для оркестрации ML-пайплайнов и автоматизации задач.

- Airflow Webserver - веб-интерфейс для управления
- Airflow Scheduler - планировщик задач
- Airflow Triggerer - выполнение deferred/sensor-задач
- Airflow Init -  инициализация бд 
- PostgreSQL - хранение метаданных

## Запуск

```bash
# http://localhost:8080
# Логин/пароль- admin/admin

# Запуск Airflow
make up-airflow

# Логи
make logs-airflow
```

## DAG

- [example_ml_pipeline.py](dags/example_ml_pipeline.py) - пример ML pipeline

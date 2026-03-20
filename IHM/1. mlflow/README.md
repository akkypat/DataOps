# Этап 1: MLflow

MLflow Tracking Server для отслеживания экспериментов и хранения артефактов ML-моделей.

- MLflow Server - веб-интерфейс и API для логирования экспериментов
- PostgreSQL - хранение метаданных экспериментов
- Volume - локальное хранилище артефактов

## Запуск

```bash
#  http://localhost:5000
# $PostgreSQL на порту 5432

# Запуск MLflow и PostgreSQL
make up-mlflow

# Просмотр логов
make logs-mlflow

# Остановка
make down-mlflow
```

## Базовый пример:

```python
import mlflow

# Подключение к tracking server
mlflow.set_tracking_uri("http://localhost:5000")

# Создание эксперимента
mlflow.create_experiment("test-experiment")

# Логирование параметров и метрик
with mlflow.start_run():
    mlflow.log_param("param1", 5)
    mlflow.log_metric("accuracy", 0.95)
    mlflow.log_artifact("model.pkl")

#Расширенный пример см. в файле 
[example_experiment.py](example_experiment.py):
```
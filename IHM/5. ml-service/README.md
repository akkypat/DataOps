# Этап 5: ML-сервис

FastAPI-сервис для ML-предсказаний с логированием запросов в JSON и сохранением истории в PostgreSQL.

- FastAPI приложение - REST API с endpoint /api/v1/predict
- PostgreSQL - хранение логов предсказаний (вход, выход, время, версия модели)

## Запуск

```bash

# http://localhost:8888
# POST /api/v1/predict
# GET /health
# GET /api/v1/logs

# Запуск ML-сервиса и PostgreSQL
make up-ml-service

# Просмотр логов
make logs-ml-service

# Остановка
make down-ml-service

#Выполнение предсказания модели.
# Запрос:
json
{
  "features": [1.5, 2.3, 3.7]
}
```

### База данных

Таблица `prediction_logs` хранит:
- `id` - уникальный идентификатор
- `timestamp` - время предсказания
- `input_features` - входные признаки (JSON)
- `output_prediction` - результат предсказания
- `model_version` - версия модели
- `inference_time_ms` - время выполнения
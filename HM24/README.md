# ДЗ по теме 24: Полноценный ML-сервис

Реализация ML-сервиса с FastAPI, MLflow и sklearn diabetes dataset по итоговому заданию курса DataOps.

## Структура

```
hw_topic24/
├── research/
│   ├── train.ipynb          # Обучение, регистрация в MLflow, сохранение модели
│   └── train_standalone.py  # Обучение без MLflow (для Docker build)
├── mlapp/
│   ├── server.py            # FastAPI приложение
│   └── __main__.py          # Точка входа
├── models/                  # Сохранённая модель (создаётся при обучении)
├── results/
│   └── curl-output.txt     # Примеры вызовов API
├── Dockerfile
├── docker-compose.yaml
└── requirements.txt
```

## Быстрый старт

### 1. Запуск через Docker Compose

```bash
cd hw_topic24
docker compose up --build
```

Сервис: http://localhost:8899  
Swagger: http://localhost:8899/docs

### 2. Полный цикл с MLflow и JupyterLab

1. Запустить MLflow и JupyterHub из основного проекта:
   ```bash
   make up-mlflow
   make up-jupyterhub
   ```

2. Открыть JupyterLab (http://localhost:8000), загрузить `research/train.ipynb`
3. Выполнить notebook — модель обучится и сохранится в `models/diabets`
4. Собрать и запустить ML-сервис (модель будет создана при сборке, если не существует)

## API

**POST /api/v1/predict**

Вход (10 параметров diabetes): `age`, `sex`, `bmi`, `bp`, `s1`, `s2`, `s3`, `s4`, `s5`, `s6`

Выход: `{"predict": float}`

Пример curl (Windows):
```bash
curl -X POST "http://localhost:8899/api/v1/predict" -H "Content-Type: application/json" -d "{\"age\": 0.04, \"sex\": -0.05, \"bmi\": 0.06, \"bp\": -0.04, \"s1\": -0.03, \"s2\": -0.01, \"s3\": 0.02, \"s4\": -0.01, \"s5\": 0.01, \"s6\": -0.04}"
```

## Результаты

- [Примеры curl](results/curl-output.txt) — вызовы predict с разными входными параметрами

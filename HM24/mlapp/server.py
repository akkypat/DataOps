"""
ML-сервис для предсказаний Diabetes (sklearn dataset).
ДЗ по теме 24: Полноценный ML-сервис.
ДЗ по теме 25: мониторинг — PrometheusMiddleware и /metrics (starlette-exporter).
"""
import os
from typing import List

import mlflow.sklearn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from starlette_exporter import PrometheusMiddleware, handle_metrics

# Путь к модели (в Docker: /app/models/diabets)
MODEL_PATH = os.environ.get("MODEL_PATH", "models/diabets")

# Загрузка модели при старте
try:
    model = mlflow.sklearn.load_model(MODEL_PATH)
except Exception as e:
    model = None
    print(f"Warning: Model not loaded: {e}. Use mock predictions.")


app = FastAPI(
    title="Diabetes Predict API",
    description="API для предсказаний на основе sklearn diabetes dataset",
    version="1.0.0"
)

# ДЗ 25: экспорт метрик для Prometheus
app.add_middleware(PrometheusMiddleware)
app.add_route("/metrics", handle_metrics)


# 10 признаков из sklearn.datasets.load_diabetes: age, sex, bmi, bp, s1, s2, s3, s4, s5, s6
class PredictRequest(BaseModel):
    age: float
    sex: float
    bmi: float
    bp: float
    s1: float
    s2: float
    s3: float
    s4: float
    s5: float
    s6: float


class PredictResponse(BaseModel):
    predict: float


def _features_from_request(req: PredictRequest) -> List[float]:
    """Преобразование запроса в список из 10 признаков в правильном порядке."""
    return [
        req.age, req.sex, req.bmi, req.bp,
        req.s1, req.s2, req.s3, req.s4, req.s5, req.s6
    ]


@app.get("/")
async def root():
    return {"service": "Diabetes Predict API", "status": "running"}


@app.get("/health")
async def health():
    return {"status": "healthy"}


@app.post("/api/v1/predict", response_model=PredictResponse)
async def predict(request: PredictRequest):
    """
    Предсказание по 10 параметрам пациента (sklearn diabetes).
    Возвращает {"predict": float}.
    """
    features = _features_from_request(request)
    if len(features) != 10:
        raise HTTPException(status_code=400, detail="Expected 10 features")

    if model is not None:
        import numpy as np
        X = np.array([features])
        prediction = float(model.predict(X)[0])
    else:
        # Заглушка, если модель не загружена
        prediction = sum(features) / 10 * 50

    return PredictResponse(predict=round(prediction, 2))

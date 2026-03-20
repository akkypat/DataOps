import json
import logging
import os
import time
from datetime import datetime
from typing import List

import numpy as np
from fastapi import FastAPI, HTTPException, Response
from prometheus_client import CONTENT_TYPE_LATEST, Counter, Gauge, Histogram, generate_latest
from pydantic import BaseModel
from sqlalchemy import Column, DateTime, Float, Integer, String, Text, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Настройка структурированного логирования в JSON
class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_data = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": record.levelname,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
        }
        if hasattr(record, 'extra_data'):
            log_data.update(record.extra_data)
        return json.dumps(log_data)

# Настройка логгера
logger = logging.getLogger("ml-service")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(JsonFormatter())
logger.addHandler(handler)

# Инициализация FastAPI
app = FastAPI(
    title="ML Service API",
    description="ML сервис для предсказаний с логированием и мониторингом",
    version="1.0.0"
)

# Модели данных
class PredictRequest(BaseModel):
    features: List[float]

class PredictResponse(BaseModel):
    prediction: float
    model_version: str
    timestamp: str

# Настройка базы данных для логирования
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./predictions.db")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class PredictionLog(Base):
    __tablename__ = "prediction_logs"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    input_features = Column(Text)
    output_prediction = Column(Float)
    model_version = Column(String)
    inference_time_ms = Column(Float)

# Создание таблиц
Base.metadata.create_all(bind=engine)

# Простая модель (заглушка) - среднее значение входных признаков
class SimpleModel:
    def __init__(self, version: str = "1.0.0"):
        self.version = version

    def predict(self, features: List[float]) -> float:
        """Простая модель: возвращает взвешенное среднее"""
        weights = np.array([0.3, 0.5, 0.2])
        features_array = np.array(features[:3])
        if len(features_array) < 3:
            features_array = np.pad(features_array, (0, 3 - len(features_array)))
        return float(np.dot(weights, features_array))

# Инициализация модели
MODEL_VERSION = os.getenv("MODEL_VERSION", "1.0.0")
model = SimpleModel(version=MODEL_VERSION)

# Prometheus метрики
prediction_counter = Counter('ml_predictions_total', 'Total number of predictions')
prediction_errors = Counter('ml_prediction_errors_total', 'Total number of prediction errors')
prediction_duration = Histogram('ml_prediction_duration_seconds', 'Prediction duration in seconds')
active_requests = Gauge('ml_active_requests', 'Number of active prediction requests')

# Middleware для логирования всех запросов
@app.middleware("http")
async def log_requests(request, call_next):
    start_time = time.time()

    # Логируем входящий запрос
    log_data = {
        "event": "request_received",
        "method": request.method,
        "url": str(request.url),
        "client": request.client.host if request.client else None,
    }
    logger.info("Request received", extra={"extra_data": log_data})

    # Обработка запроса
    response = await call_next(request)

    # Логируем ответ
    duration_ms = (time.time() - start_time) * 1000
    log_data = {
        "event": "request_completed",
        "method": request.method,
        "url": str(request.url),
        "status_code": response.status_code,
        "duration_ms": round(duration_ms, 2),
    }
    logger.info("Request completed", extra={"extra_data": log_data})

    return response

@app.get("/")
async def root():
    """Корневой endpoint"""
    return {
        "service": "ML Service",
        "version": MODEL_VERSION,
        "status": "running"
    }

@app.get("/health")
async def health():
    """Health check endpoint для Kubernetes probes"""
    return {"status": "healthy"}

@app.get("/metrics")
async def metrics():
    """Prometheus metrics endpoint"""
    return Response(content=generate_latest(), media_type=CONTENT_TYPE_LATEST)

@app.post("/api/v1/predict", response_model=PredictResponse)
async def predict(request: PredictRequest):
    """
    Endpoint для предсказаний ML-модели

    Принимает список признаков и возвращает предсказание.
    Логирует все запросы в БД и в JSON-формат.
    """
    active_requests.inc()
    try:
        start_time = time.time()

        # Валидация входных данных
        if len(request.features) == 0:
            prediction_errors.inc()
            raise HTTPException(status_code=400, detail="Features list cannot be empty")

        # Предсказание
        with prediction_duration.time():
            prediction = model.predict(request.features)

        inference_time_ms = (time.time() - start_time) * 1000
        prediction_counter.inc()

        # Результат
        result = PredictResponse(
            prediction=prediction,
            model_version=MODEL_VERSION,
            timestamp=datetime.utcnow().isoformat()
        )

        # Логирование в JSON
        log_data = {
            "event": "prediction_made",
            "input_features": request.features,
            "output_prediction": prediction,
            "model_version": MODEL_VERSION,
            "inference_time_ms": round(inference_time_ms, 2),
        }
        logger.info("Prediction completed", extra={"extra_data": log_data})

        # Логирование в БД
        try:
            db = SessionLocal()
            log_entry = PredictionLog(
                input_features=json.dumps(request.features),
                output_prediction=prediction,
                model_version=MODEL_VERSION,
                inference_time_ms=inference_time_ms
            )
            db.add(log_entry)
            db.commit()
            db.close()
        except Exception as e:
            logger.error(f"Failed to log to database: {str(e)}")

        return result

    except HTTPException:
        raise
    except Exception as e:
        prediction_errors.inc()
        logger.error(f"Prediction failed: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")
    finally:
        active_requests.dec()

@app.get("/api/v1/logs")
async def get_logs(limit: int = 10):
    """Получение последних логов предсказаний из БД"""
    try:
        db = SessionLocal()
        logs = db.query(PredictionLog).order_by(PredictionLog.timestamp.desc()).limit(limit).all()
        db.close()

        return {
            "count": len(logs),
            "logs": [
                {
                    "id": log.id,
                    "timestamp": log.timestamp.isoformat(),
                    "input_features": json.loads(log.input_features),
                    "output_prediction": log.output_prediction,
                    "model_version": log.model_version,
                    "inference_time_ms": log.inference_time_ms
                }
                for log in logs
            ]
        }
    except Exception as e:
        logger.error(f"Failed to retrieve logs: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to retrieve logs: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8888)

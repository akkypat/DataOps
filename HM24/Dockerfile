# ДЗ по теме 24: ML-сервис Diabetes
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем модель (если есть) и исходники
COPY models/ ./models/
COPY research/ ./research/
COPY mlapp/ ./mlapp/

EXPOSE 8888

ENV MODEL_PATH=/app/models/diabets

CMD ["python", "-m", "mlapp"]

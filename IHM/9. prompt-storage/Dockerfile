FROM python:3.11-slim

WORKDIR /mlflow

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev && \
    rm -rf /var/lib/apt/lists/*

RUN python -m pip install --no-cache-dir --upgrade \
    pip \
    setuptools \
    wheel \
    packaging

RUN pip install --no-cache-dir \
    mlflow==2.22.4 \
    psycopg2-binary==2.9.9 \
    boto3==1.34.44

RUN mkdir -p /mlflow/artifacts

EXPOSE 5000

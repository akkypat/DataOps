 Явная загрузка .env (решает проблему, когда переменные не подтягиваются)
COMPOSE := docker compose --env-file .env

.PHONY: help setup-env up-all down status logs
.PHONY: up-mlflow down-mlflow logs-mlflow
.PHONY: up-airflow down-airflow logs-airflow
.PHONY: up-lakefs down-lakefs logs-lakefs
.PHONY: up-jupyterhub down-jupyterhub logs-jupyterhub
.PHONY: up-ml-service down-ml-service logs-ml-service
.PHONY: up-monitoring down-monitoring logs-monitoring
.PHONY: up-prompt-storage down-prompt-storage logs-prompt-storage

help:
	@echo "=== MLops Final Project - Makefile ==="
	@echo ""
	@echo "Запуск всех сервисов:"
	@echo "  make up-all          - Поднять все профили"
	@echo "  make down            - Остановить все сервисы"
	@echo "  make status          - Показать статус контейнеров"
	@echo "  make logs            - Показать логи всех контейнеров"
	@echo ""
	@echo "Этап 1: MLflow"
	@echo "  make up-mlflow       - Запустить MLflow + PostgreSQL"
	@echo "  make down-mlflow     - Остановить MLflow"
	@echo "  make logs-mlflow     - Логи MLflow"
	@echo ""
	@echo "Этап 2: Airflow"
	@echo "  make up-airflow      - Запустить Airflow + PostgreSQL"
	@echo "  make down-airflow    - Остановить Airflow"
	@echo "  make logs-airflow    - Логи Airflow"
	@echo ""
	@echo "Этап 3: LakeFS"
	@echo "  make up-lakefs       - Запустить LakeFS + PostgreSQL + MinIO"
	@echo "  make down-lakefs     - Остановить LakeFS"
	@echo "  make logs-lakefs     - Логи LakeFS"
	@echo ""
	@echo "Этап 4: JupyterHub"
	@echo "  make up-jupyterhub   - Запустить JupyterHub"
	@echo "  make down-jupyterhub - Остановить JupyterHub"
	@echo "  make logs-jupyterhub - Логи JupyterHub"
	@echo ""
	@echo "Этап 5: ML-сервис"
	@echo "  make up-ml-service   - Запустить ML-сервис + PostgreSQL"
	@echo "  make down-ml-service - Остановить ML-сервис"
	@echo "  make logs-ml-service - Логи ML-сервиса"
	@echo ""
	@echo "Этап 6: Мониторинг"
	@echo "  make up-monitoring   - Запустить Prometheus + Grafana"
	@echo "  make down-monitoring - Остановить мониторинг"
	@echo "  make logs-monitoring - Логи мониторинга"
	@echo ""
	@echo "Этап 9: Prompt Storage"
	@echo "  make up-prompt-storage   - Запустить отдельный MLflow для Prompt Storage"
	@echo "  make down-prompt-storage - Остановить Prompt Storage"
	@echo "  make logs-prompt-storage - Логи Prompt Storage"
	@echo ""
	@echo ""

# Создать .env из шаблона (если не существует)
setup-env:
	@if [ ! -f .env ]; then cp .env.example .env && echo "Создан .env из .env.example"; else echo ".env уже существует"; fi

# Запуск всех профилей
up-all: setup-env
	$(COMPOSE) --profile mlflow --profile airflow --profile lakefs --profile jupyterhub --profile ml-service --profile monitoring --profile prompt-storage up -d

# Остановка всех сервисов
down: setup-env
	$(COMPOSE) down

# Статус контейнеров
status: setup-env
	$(COMPOSE) ps

# Логи всех контейнеров
logs: setup-env
	$(COMPOSE) logs -f

# Этап 1: MLflow
up-mlflow: setup-env
	$(COMPOSE) --profile mlflow up -d

down-mlflow:
	$(COMPOSE) --profile mlflow down

logs-mlflow:
	$(COMPOSE) --profile mlflow logs -f

# Этап 2: Airflow
up-airflow: setup-env
	$(COMPOSE) --profile airflow up -d

down-airflow:
	$(COMPOSE) --profile airflow down

logs-airflow:
	$(COMPOSE) --profile airflow logs -f

# Этап 3: LakeFS
up-lakefs: setup-env
	$(COMPOSE) --profile lakefs up -d

down-lakefs:
	$(COMPOSE) --profile lakefs down

logs-lakefs:
	$(COMPOSE) --profile lakefs logs -f

# Этап 4: JupyterHub
up-jupyterhub: setup-env
	$(COMPOSE) --profile jupyterhub up -d

down-jupyterhub:
	$(COMPOSE) --profile jupyterhub down

logs-jupyterhub:
	$(COMPOSE) --profile jupyterhub logs -f

# Этап 5: ML-сервис
up-ml-service: setup-env
	$(COMPOSE) --profile ml-service up -d

down-ml-service:
	$(COMPOSE) --profile ml-service down

logs-ml-service:
	$(COMPOSE) --profile ml-service logs -f

# Этап 6: Мониторинг
up-monitoring: setup-env
	$(COMPOSE) --profile monitoring up -d

down-monitoring:
	$(COMPOSE) --profile monitoring down

logs-monitoring:
	$(COMPOSE) --profile monitoring logs -f

# Этап 9: Prompt Storage
up-prompt-storage: setup-env
	$(COMPOSE) --profile prompt-storage up -d

down-prompt-storage:
	$(COMPOSE) --profile prompt-storage down

logs-prompt-storage:
	$(COMPOSE) --profile prompt-storage logs -f
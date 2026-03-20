#### Румянцев Иван МИНДА241

# Итоговая работа по DataOps
- 9 этапов развертывания ML-инфраструктуры
- Единый docker-compose.yaml с профилями для каждого этапа
- Makefile для удобного управления сервисами
- Детальная документация в каждой папке этапа

## Краткое описание этапов
```bash
1. Tracking server для логирования экспериментов и хранения артефактов моделей.

2. Оркестрация ML-пайплайнов и автоматизация задач.

3. Версионирование данных с Git-подобным подходом.

4. Многопользовательская среда для работы с Jupyter notebooks.

5. FastAPI REST API с endpoint.

6. Prometheus для сбора метрик ML-сервиса и Grafana для визуализации.

7. Deployment, Service, Ingress с настроенными startup/readiness/liveness проверками.

8. Упаковка ML-сервиса в Helm с настраиваемыми параметрами.

9. Создание версий промптов в отдельном MLflow для LLM-приложений.
```

### Запуск

```bash
# Скопируйте и настройте переменные окружения
cp .env.example .env

# Отредактируйте .env, установите пароли и секретные ключи

# Запустить все этапы сразу
make up-all

# Или запускать по отдельности
make up-mlflow
make up-airflow
make up-lakefs
make up-jupyterhub
make up-ml-service
make up-monitoring

# Статус всех контейнеров
make status

# Логи конкретного этапа
make logs-mlflow
make logs-ml-service
```

## Ссылки на сервисы

- **MLflow**: http://localhost:5000
- **MLflow Prompt Storage**: http://localhost:5001
- **Airflow**: http://localhost:8080
- **LakeFS**: http://localhost:8001
- **MinIO Console**: http://localhost:9001
- **JupyterHub**: http://localhost:8000
- **ML-сервис**: http://localhost:8888
  - API Docs: http://localhost:8888/docs
  - Metrics: http://localhost:8888/metrics
- **Prometheus**: http://localhost:9090
- **Grafana**: http://localhost:3000 
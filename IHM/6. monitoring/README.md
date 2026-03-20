# Этап 6: Мониторинг (Prometheus + Grafana)

Система мониторинга ML-сервиса с использованием Prometheus для сбора метрик и Grafana для визуализации.

- Prometheus - сбор и хранение метрик
- Grafana - визуализация метрик через дашборды
- ML-сервис - endpoint /metrics для экспорта метрик

## Запуск

```bash
# Prometheus UI: http://localhost:9090
# Grafana UI: http://localhost:3000
# Логин/пароль: admin/admin

# Запуск Prometheus и Grafana
make up-monitoring

# Также нужен запущенный ML-сервис
make up-ml-service

# Просмотр логов
make logs-monitoring

# Остановка
make down-monitoring
```
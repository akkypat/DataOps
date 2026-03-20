# Этап 6: Мониторинг

## Скриншоты

1. [`prometheus-targets.png`](./prometheus-targets.png) - Status → Targets, `ml-service` в состоянии `UP`
2. [`grafana-datasource.png`](./grafana-datasource.png) - Настроенный Data Source (Prometheus)
3. [`grafana-dashboard.png`](./grafana-dashboard.png) - Дашборд с метриками ML-сервиса

## Как посмотреть

1. Запустить `make up-ml-service` и `make up-monitoring`
2. Сгенерировать трафик 
3. Prometheus: [http://localhost:9090](http://localhost:9090) - Status - Targets
4. Grafana: [http://localhost:3000](http://localhost:3000)
  - Добавить Data Source: Prometheus ([http://prometheus:9090](http://prometheus:9090))
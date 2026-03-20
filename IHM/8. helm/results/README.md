# Результаты Этап 8: Helm

## Скриншоты

1. [`helm-list.png`](./helm-list.png) - Вывод `helm list`
2. [`helm-status.png`](./helm-status.png) - Вывод `helm status ml-service-release`
3. [`helm-pods.png`](./helm-pods.png) - Поды, развернутые через Helm
4. [`helm-status-after-upgrades.png`](./helm-status-after-upgrades.png) - Скриншот итогового статуса релиза после обновлений

### Как посмотреть
1. K8s кластер запущен
2. chart:
   ```bash
   helm install ml-service-release ./helm/ml-service
   ```
3. Выполнить команды:
   ```bash
   helm list
   helm status ml-service-release
   kubectl get pods
   ```
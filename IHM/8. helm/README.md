# Этап 8: Helm Chart

Helm chart для развертывания ML-сервиса в Kubernetes с настраиваемыми параметрами.

## Запуск

```bash
# Установка chart 
helm install ml-service-release ./helm/ml-service

# Установка с переопределением значений
helm install ml-service-release ./helm/ml-service \
  --set image.tag=2.0.0 \
  --set replicaCount=3

# Обновление релиза
helm upgrade ml-service-release ./helm/ml-service

# Обновление с новой версией образа
helm upgrade ml-service-release ./helm/ml-service \
  --set image.tag=2.0.0

# Обновление ресурсов
helm upgrade ml-service-release ./helm/ml-service \
  --set resources.requests.cpu=200m \
  --set resources.requests.memory=512Mi

# Удаление релиза
helm uninstall ml-service-release
```
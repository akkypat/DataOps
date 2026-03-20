# Этап 7: Kubernetes

Kubernetes манифесты для развертывания ML-сервиса в кластере с настроенными probes и Ingress.

- Deployment - конфигурация подов ML-сервиса с пробами
- Service - внутренний сервис для доступа к подам
- Ingress - внешний доступ к сервису через HTTP
- Secret - хранение чувствительных данных 

## Запуск

1. Запустить Kubernetes кластер (minikube, kind, Docker Desktop, etc.)
2. Собрать Docker образ ML-сервиса:
   ```bash
   docker build -t ml-service:1.0.0 ./ml-service

   # Для minikube:
   minikube image load ml-service:1.0.0

   # Для kind:
   kind load docker-image ml-service:1.0.0

   # Создание namespace
   kubectl create namespace ml-service

   # Применение манифестов
   kubectl apply -f k8s/secret.yaml
   kubectl apply -f k8s/deployment.yaml
   kubectl apply -f k8s/service.yaml
   kubectl apply -f k8s/ingress.yaml

   # Проверка статуса
   kubectl get pods
   kubectl get services
   kubectl get ingress
   ```
### Доступы

```bash
# Port-forward для локального доступа
kubectl port-forward service/ml-service 8888:80

# Тестовый запрос
curl -X POST "http://localhost:8888/api/v1/predict" \
     -H "Content-Type: application/json" \
     -d '{"features": [1.5, 2.3, 3.7]}'

### Доступ через Ingress
# Для minikube
minikube addons enable ingress
<MINIKUBE_IP> ml-service.local

# Доступ к сервису
curl http://ml-service.local/
```
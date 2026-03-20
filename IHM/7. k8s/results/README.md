# Этап 7: Kubernetes

## Скриншоты

1. [`k8s-pods.png`](./k8s-pods.png) - Вывод `kubectl get pods -l app=ml-service`
2. [`k8s-services.png`](./k8s-services.png) - Вывод `kubectl get services`
3. [`k8s-ingress.png`](./k8s-ingress.png) - Вывод `kubectl get ingress`
4. [`k8s-pod-describe.png`](./k8s-pod-describe.png) - Вывод `kubectl describe pod` с секциями probes


## Как посмотреть

1. Запустить K8s кластер (minikube/kind/Docker Desktop)
2. Собрать и загрузить образ:
   ```bash
   docker build -t ml-service:1.0.0 ./ml-service
   minikube image load ml-service:1.0.0
   kubectl apply -f k8s/
   ```
3. Выполнить команды:
   ```bash
   kubectl get pods -l app=ml-service
   kubectl get services
   kubectl get ingress
   kubectl describe pod -l app=ml-service
   ```
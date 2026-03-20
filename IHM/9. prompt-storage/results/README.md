# Этап 9: Prompt Storage в MLflow

## Скриншоты

1. [`mlflow-prompts-ui.png`](./mlflow-prompts-ui.png) - Интерфейс Prompt Engineering в MLflow
2. [`mlflow-prompts-list.png`](./mlflow-prompts-list.png) - Список созданных промптов
3. [`mlflow-prompt-versions.png`](./mlflow-prompt-versions.png) - Версии одного из промптов

## Как посмотреть

1. Запустить сервис Prompt Storage: `make up-prompt-storage`
2. Открыть http://localhost:5001
3. Найти раздел "Prompts"
4. Создать несколько версий промптов:
   - system_prompt (v1, v2, v3)
   - user_query_template (v1, v2)
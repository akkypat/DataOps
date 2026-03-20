# Этап 9: Prompt Storage в MLflow

Использование MLflow Prompt Engineering для версионирования промптов в LLM-приложениях.

## Запуск

- Запустить отдельный MLflow Prompt Storage (Этап 9): `make up-prompt-storage`
- MLflow версии с поддержкой Prompt Engineering
- Этап 1 (MLflow на `http://localhost:5000`) остается без изменений
- Открыть MLflow UI: http://localhost:5001
- В боковом меню найдите раздел "Prompts"

## Создание версий промптов

1. В разделе Prompt Engineering нажать "Create Prompt"
2. Отправить имя промпта (например, "system_prompt")
3. Отправить текст промпта
4. Сохранить как версию 1
5. Создать новую версию с измененным текстом
6. Повторить для других промптов
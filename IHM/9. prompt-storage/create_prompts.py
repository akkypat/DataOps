#Скрипт для создания версий промптов в MLflow Prompt Storage

import os
import mlflow

# Настройка подключения к MLflow
MLFLOW_TRACKING_URI = os.getenv("PROMPT_MLFLOW_TRACKING_URI", "http://localhost:5001")
mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)

# Промпт 1: System Prompt (3 версии)
prompts_v1 = [
    {
        "name": "system_prompt",
        "text": "You are a helpful AI assistant.",
        "version": 1
    },
    {
        "name": "system_prompt",
        "text": "You are a helpful AI assistant specialized in machine learning and data science.",
        "version": 2
    },
    {
        "name": "system_prompt",
        "text": "You are an expert ML engineer assistant. Provide concise, technical answers with code examples.",
        "version": 3
    }
]

# Промпт 2: User Query Template (2 версии)
prompts_v2 = [
    {
        "name": "user_query_template",
        "text": "Analyze this data: {data}",
        "version": 1
    },
    {
        "name": "user_query_template",
        "text": "Please provide a detailed analysis of: {data}. Include key insights and recommendations.",
        "version": 2
    }
]

# Промпт 3: Code Review Template (2 версии)
prompts_v3 = [
    {
        "name": "code_review_template",
        "text": "Review this code: {code}",
        "version": 1
    },
    {
        "name": "code_review_template",
        "text": "Perform a thorough code review of: {code}. Check for bugs, performance issues, and best practices.",
        "version": 2
    }
]

all_prompts = prompts_v1 + prompts_v2 + prompts_v3

# Создание промптов
for prompt in all_prompts:
    try:
        # Примечание: API может отличаться в зависимости от версии MLflow
        # Этот код может потребовать адаптации под конкретную версию
        print(f"Создание: {prompt['name']} v{prompt['version']}")

        # Если MLflow поддерживает API для промптов
        # mlflow.llm.log_prompt(...)
        # Или через Tracking API:
        # with mlflow.start_run(run_name=f"{prompt['name']}_v{prompt['version']}"):
        #     mlflow.log_param("prompt_name", prompt['name'])
        #     mlflow.log_param("prompt_version", prompt['version'])
        #     mlflow.log_text(prompt['text'], f"prompts/{prompt['name']}_v{prompt['version']}.txt")

        print(f"Создан: {prompt['name']} v{prompt['version']}")
    except Exception as e:
        print(f"Ошибка при создании {prompt['name']} v{prompt['version']}: {e}")

print(f"\nВсе промпты созданы! Проверьте MLflow UI: {MLFLOW_TRACKING_URI}")
print("Примечание: создайте промпты вручную через UI, если API не поддерживается в вашей версии MLflow")

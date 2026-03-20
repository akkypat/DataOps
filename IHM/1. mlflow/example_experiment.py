import os
import numpy as np
import mlflow
import mlflow.sklearn
from sklearn.linear_model import LinearRegression

# Настройка подключения к MLflow
MLFLOW_TRACKING_URI = "http://localhost:5000"
mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)

# Создание или получение эксперимента
EXPERIMENT_NAME = "demo-linear-regression"
try:
    experiment_id = mlflow.create_experiment(EXPERIMENT_NAME)
    print(f"Создан новый эксперимент: {EXPERIMENT_NAME} (ID: {experiment_id})")
except Exception:
    experiment = mlflow.get_experiment_by_name(EXPERIMENT_NAME)
    experiment_id = experiment.experiment_id
    print(f"Используется существующий эксперимент: {EXPERIMENT_NAME} (ID: {experiment_id})")

mlflow.set_experiment(EXPERIMENT_NAME)

# Создание простых тренировочных данных
np.random.seed(42)
X = np.random.rand(100, 3)
y = X[:, 0] * 2 + X[:, 1] * 3 + X[:, 2] * 1.5 + np.random.randn(100) * 0.1

# Запуск run и логирование
with mlflow.start_run(run_name="linear-model-v1") as run:
    print(f"\nЗапущен run: {run.info.run_id}")

    # Обучение модели
    model = LinearRegression()
    model.fit(X, y)

    # Предсказание и оценка
    predictions = model.predict(X)
    mse = np.mean((predictions - y) ** 2)
    r2_score = model.score(X, y)

    # Логирование параметров
    mlflow.log_param("model_type", "LinearRegression")
    mlflow.log_param("n_features", X.shape[1])
    mlflow.log_param("n_samples", X.shape[0])
    mlflow.log_param("random_seed", 42)

    # Логирование метрик
    mlflow.log_metric("mse", mse)
    mlflow.log_metric("r2_score", r2_score)
    mlflow.log_metric("coefficients_sum", np.sum(model.coef_))

    print(f"Метрики: MSE={mse:.4f}, R^2={r2_score:.4f}")

    # Логирование модели через sklearn
    mlflow.sklearn.log_model(
        model,
        "model",
        registered_model_name="LinearRegressionModel"
    )

    # Сохранение дополнительных артефактов
    # 1. Коэффициенты модели
    with open("coefficients.txt", "w") as f:
        f.write(f"Intercept: {model.intercept_}\n")
        f.write(f"Coefficients: {model.coef_}\n")
    mlflow.log_artifact("coefficients.txt")
    os.remove("coefficients.txt")

    # 2. Пример предсказаний
    with open("predictions_sample.txt", "w") as f:
        for i in range(5):
            f.write(f"Sample {i+1}: X={X[i]}, y_true={y[i]:.4f}, y_pred={predictions[i]:.4f}\n")
    mlflow.log_artifact("predictions_sample.txt")
    os.remove("predictions_sample.txt")

    # 3. Тэги
    mlflow.set_tag("model_version", "1.0.0")
    mlflow.set_tag("environment", "development")
    mlflow.set_tag("author", "mlops-team")

    print(f"Просмотр: {MLFLOW_TRACKING_URI}/#/experiments/{experiment_id}/runs/{run.info.run_id}")

# Создание второго run для сравнения
with mlflow.start_run(run_name="linear-model-v2") as run:
    print(f"\nЗапущен run: {run.info.run_id}")

    # Другие данные
    X2 = np.random.rand(150, 3)
    y2 = X2[:, 0] * 1.5 + X2[:, 1] * 2.5 + X2[:, 2] * 2 + np.random.randn(150) * 0.15

    model2 = LinearRegression()
    model2.fit(X2, y2)

    predictions2 = model2.predict(X2)
    mse2 = np.mean((predictions2 - y2) ** 2)
    r2_score2 = model2.score(X2, y2)

    # Логирование
    mlflow.log_param("model_type", "LinearRegression")
    mlflow.log_param("n_features", X2.shape[1])
    mlflow.log_param("n_samples", X2.shape[0])
    mlflow.log_param("random_seed", 42)

    mlflow.log_metric("mse", mse2)
    mlflow.log_metric("r2_score", r2_score2)

    mlflow.sklearn.log_model(model2, "model")

    mlflow.set_tag("model_version", "2.0.0")
    mlflow.set_tag("environment", "development")
    print(f"Метрики: MSE={mse2:.4f}, R²={r2_score2:.4f}")

print(f"\nПросмотр экспериментов: {MLFLOW_TRACKING_URI}")
print(f"Эксперимент: {EXPERIMENT_NAME}")
print("\nСоздано 2 run'а для сравнения моделей.")

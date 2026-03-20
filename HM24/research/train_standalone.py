"""
Скрипт для обучения и сохранения модели без MLflow.
Используйте для быстрого получения модели при сборке Docker,
если MLflow не запущен. Основной сценарий — notebook research/train.ipynb.
"""
import os
import sys

from sklearn.datasets import load_diabetes
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

try:
    import mlflow.sklearn
except ImportError:
    sys.exit("Требуется mlflow. Выполните: pip install mlflow scikit-learn")

# Путь к папке models (от research/)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR)
MODEL_SAVE_PATH = os.path.join(ROOT_DIR, "models", "diabets")


def main():
    print("Загрузка датасета diabetes...")
    data = load_diabetes(return_X_y=False)
    X, y = data.data, data.target

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    print("Обучение пайплайна (StandardScaler + RandomForestRegressor)...")
    pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("model", RandomForestRegressor(n_estimators=100, random_state=42)),
    ])
    pipeline.fit(X_train, y_train)

    from sklearn.metrics import mean_squared_error, r2_score
    y_pred = pipeline.predict(X_test)
    print(f"MSE: {mean_squared_error(y_test, y_pred):.2f}")
    print(f"R²: {r2_score(y_test, y_pred):.4f}")

    os.makedirs(os.path.dirname(MODEL_SAVE_PATH), exist_ok=True)
    mlflow.sklearn.save_model(pipeline, MODEL_SAVE_PATH)
    print(f"Модель сохранена: {MODEL_SAVE_PATH}")


if __name__ == "__main__":
    main()

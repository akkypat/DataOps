"""
Точка входа для запуска ML-сервиса.
"""
import uvicorn

from mlapp.server import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8888)

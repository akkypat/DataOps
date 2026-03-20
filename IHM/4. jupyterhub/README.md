# Этап 4: JupyterHub

JupyterHub для организации многопользовательской среды разработки с Jupyter notebooks.

- JupyterHub - многопользовательский сервер Jupyter
- Configurable HTTP Proxy - прокси для маршрутизации запросов к пользовательским серверам
- JupyterLab - современный интерфейс Jupyter

## Запуск

```bash
# http://localhost:8000
# Логин/пароль: admin/password

# Запуск JupyterHub
make up-jupyterhub

# Просмотр логов
make logs-jupyterhub

# Остановка
make down-jupyterhub
```
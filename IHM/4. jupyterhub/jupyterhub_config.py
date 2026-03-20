import os

# Базовая конфигурация JupyterHub
c.JupyterHub.bind_url = 'http://0.0.0.0:8000'
c.JupyterHub.hub_bind_url = 'http://0.0.0.0:8081'
c.JupyterHub.hub_connect_url = 'http://jupyterhub:8081'

# Использование DummyAuthenticator для упрощенной аутентификации
c.JupyterHub.authenticator_class = 'jupyterhub.auth.DummyAuthenticator'

# Разрешить вход с любым паролем (для демо)
c.DummyAuthenticator.password = os.environ.get('JUPYTERHUB_DUMMY_PASSWORD', 'password')

# Список администраторов
c.Authenticator.admin_users = {'admin'}

# Spawner - запуск single-user servers
c.JupyterHub.spawner_class = 'jupyterhub.spawner.SimpleLocalProcessSpawner'

# Директория для single-user серверов
c.Spawner.notebook_dir = '~'

# Стандартный URL для single-user servers
c.Spawner.default_url = '/lab'

# Для текущего демо-образа single-user процесс запускается в том же контейнере
# от root, поэтому явно разрешаем такой запуск.
c.Spawner.args = ['--allow-root']

# Таймауты запуска/доступности single-user сервера
c.Spawner.start_timeout = 120
c.Spawner.http_timeout = 120

# Логирование
c.JupyterHub.log_level = 'INFO'
c.Spawner.debug = True

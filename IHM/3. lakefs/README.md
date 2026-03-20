# Этап 3: LakeFS

LakeFS для версионирования данных с использованием Git-подобного подхода (branches, commits, merges).

- LakeFS - сервер версионирования данных
- PostgreSQL - хранение метаданных LakeFS
- MinIO - S3-совместимое объектное хранилище для данных

## Запуск

```bash
# http://localhost:8001
# http://localhost:9001
# Логин/пароль: minioadmin/ minioadmin123
# http://localhost:9000

# Запуск LakeFS, PostgreSQL и MinIO
make up-lakefs

# Просмотр логов
make logs-lakefs

# Остановка
make down-lakefs
```
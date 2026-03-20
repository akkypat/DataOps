# Результаты Этап 3: LakeFS

## Скриншоты

1. [`minio-console.png`](./minio-console.png) - MinIO Console с созданным bucket
2. [`lakefs-repositories.png`](./lakefs-repositories.png) - Список репозиториев в LakeFS
3. [`lakefs-branches.png`](./lakefs-branches.png) - Ветки репозитория (main, dev)
4. [`lakefs-commits.png`](./lakefs-commits.png) - История коммитов с добавленным файлом


## Как посмотреть

1. Запустить `make up-lakefs`
2. Открыть MinIO: http://localhost:9001 (minioadmin/minioadmin123)
3. Создать bucket: `lakefs-data`
4. Открыть LakeFS: http://localhost:8001
5. Создать репозиторий, ветку, добавьте файл, сделайте commit

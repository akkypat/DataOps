# ML DB Project — Topic 18 (DataOps)

##  Тема
Работа с БД в ML‑проектах.  
Использование yoyo-migrations для управления миграциями PostgreSQL.

---

#  Быстрый старт

## 1️ Клонировать проект и перейти в папку

```bash
cd ml-db-project
```

---

## 2️ Установка зависимостей

Создание виртуального окружения и установка пакетов:

```bash
make dev.install
```

Активировать окружение вручную (если нужно):

```bash
source .venv/bin/activate
```

---

## 3️ Запуск PostgreSQL через Docker

```bash
docker compose up -d
```

Проверить статус:

```bash
docker compose ps
```

Проверить готовность БД:

```bash
docker logs ml_postgres
```

---

#  Работа с миграциями

##  Создание новой миграции

```bash
make db.migration.new name="users: create table"
```

Файл будет создан в папке `migrations/`.

---

##  Применение миграций

```bash
make db.migrate
```

---

##  Откат последней миграции

```bash
make db.rollback
```

---

#  Проверка полного цикла

```bash
make db.migrate
make db.rollback
make db.migrate
```

Таким образом тестируется корректность и миграции, и отката.

---

#  Проверка структуры БД

Подключение через psql:

```bash
psql -h localhost -U ml_user -d ml_db
```

Внутри клиента:

```sql
\dt
\d users
```

Ожидаемая структура таблицы:

- id (SERIAL, PK)
- firstname (VARCHAR)
- lastname (VARCHAR) — после второй миграции
- created_at (TIMESTAMP)

---

#  Структура проекта

```
ml-db-project/
│
├── Makefile
├── requirements.txt
├── docker-compose.yaml
├── .env
│
└── migrations/
    ├── 001_create_users_table.py
    └── 002_add_lastname_column.py
```

---

#  Используемые технологии

- Python 3
- yoyo-migrations
- PostgreSQL 17
- Docker Compose
- Makefile

---


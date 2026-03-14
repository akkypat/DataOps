include .env
export

VENV=.venv/bin/activate
YOYO=.venv/bin/yoyo

dev.install:
	python -m venv .venv
	. .venv/bin/activate && pip install -r requirements.txt

db.migration.new:
	. .venv/bin/activate && yoyo new migrations -m "$(name)"

db.migrate:
	. .venv/bin/activate && yoyo apply --database $(DATABASE_URL) migrations

db.rollback:
	. .venv/bin/activate && yoyo rollback --database $(DATABASE_URL) migrations

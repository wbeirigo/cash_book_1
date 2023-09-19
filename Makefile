dev:
	docker-compose up -d

dev-down:
	docker-compose down

create-alembic:
	alembic revision --autogenerate -m "Added account table"

push-migration:
	alembic upgrade head

	
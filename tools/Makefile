build:
	docker-compose build --no-cache

up:
	docker-compose up -d --force-recreate

rebuild: build up

pull-latest:
	docker-compose pull
	docker-compose up -d --force-recreate

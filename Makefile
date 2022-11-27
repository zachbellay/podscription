build:
	docker compose -f docker-compose.yml --env-file .env build 

up:
	docker compose -f docker-compose.yml --env-file .env up -d

restart:
	docker compose -f docker-compose.yml --env-file .env restart

down:
	docker compose -f docker-compose.yml --env-file .env down
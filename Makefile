
build:
	docker compose -f docker-compose.yml --env-file .env build 
# docker compose -f scrapers/docker-compose.yaml --env-file .env 	build
# docker compose -f django/docker-compose.yaml --env-file .env build

up:
	docker compose -f docker-compose.yml --env-file .env up -d
# docker compose -f django/docker-compose.yaml --env-file .env up -d
# docker compose -f scrapers/docker-compose.yaml --env-file .env up -d

# restart:
# 	docker compose -f scrapers/docker-compose.yaml --env-file .env -f django/docker-compose.yaml --env-file .env restart

down:
# docker compose -f scrapers/docker-compose.yaml --env-file .env down
# docker compose -f django/docker-compose.yaml --env-file .env down
	docker compose -f docker-compose.yml --env-file .env down
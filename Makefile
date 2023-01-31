
# Note: check package.json for APP_ENV=production/development

ifdef PROD
    COMPOSE_FILES += -f docker-compose.yml --env-file .env.production
else
	COMPOSE_FILES += -f docker-compose.dev.yml --env-file .env.development
endif

build:
	DOCKER_BUILDKIT=1 COMPOSE_DOCKER_CLI_BUILD=1 docker compose $(COMPOSE_FILES) build

ifdef PROD
up:
	docker compose $(COMPOSE_FILES) up -d && docker network connect nginx-proxy-manager_default podscription-django
else
up:
	docker compose $(COMPOSE_FILES) up -d
endif

restart:
	docker compose $(COMPOSE_FILES) restart

down:
	docker compose $(COMPOSE_FILES) down



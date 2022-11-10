AIRFLOW_IMAGE_NAME=podscription-airflow-base
AIRFLOW_IMAGE_VERSION=v0.0.1

build:
# docker build -t ${AIRFLOW_IMAGE_NAME}:${AIRFLOW_IMAGE_VERSION} -t ${AIRFLOW_IMAGE_NAME}:latest airflow
	docker-compose -f airflow/docker-compose.airflow.yaml --env-file .env build
	docker-compose -f django/docker-compose.yaml --env-file .env build

up:
	docker-compose -f django/docker-compose.yaml --env-file .env up -d
	docker-compose -f airflow/docker-compose.airflow.yaml --env-file .env up -d

restart:
	docker-compose -f airflow/docker-compose.airflow.yaml --env-file .env -f django/docker-compose.yaml --env-file .env restart

down:
	docker-compose -f airflow/docker-compose.airflow.yaml --env-file .env down
	docker-compose -f django/docker-compose.yaml --env-file .env down



# docker-compose logs django/docker-compose.yaml
# no configuration file provided: not found

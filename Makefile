AIRFLOW_IMAGE_NAME=podscription-airflow-base
AIRFLOW_IMAGE_VERSION=v0.0.1

build:
	bash -c 'source .env'
	docker build -t ${AIRFLOW_IMAGE_NAME}:${AIRFLOW_IMAGE_VERSION} -t ${AIRFLOW_IMAGE_NAME}:latest airflow

up:
	docker-compose -f airflow/docker-compose.airflow.yaml --env-file .env --profile flower up -d

restart:
	docker-compose -f airflow/docker-compose.airflow.yaml --env-file .env restart

down:
	docker-compose -f airflow/docker-compose.airflow.yaml --env-file .env down




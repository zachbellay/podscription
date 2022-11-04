#  run this command from the ./airflow/dags directory
ln -s ../../scrapers scrapers


docker buildx build --platform linux/amd64 --output type=docker -t airflow-base:latest .

docker run --rm -it --platform linux/amd64 airflow-base:latest bash
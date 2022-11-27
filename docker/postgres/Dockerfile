FROM postgres:latest
COPY ./init.sh /docker-entrypoint-initdb.d/init.sh
# CMD ["docker-entrypoint.sh", "postgres"]

# docker run -e POSTGRES_USER=${DJANGO_POSTGRES_DB} -e POSTGRES_PASSWORD=${DJANGO_DATABASE_PASSWORD} -e POSTGRES_DB=${DJANGO_POSTGRES_DB} pg:latest
# docker run -d --name pg -e POSTGRES_USER=${DJANGO_POSTGRES_DB} -e POSTGRES_PASSWORD=${DJANGO_DATABASE_PASSWORD} -e POSTGRES_DB=${DJANGO_POSTGRES_DB} pg:latest
#!/bin/bash
set -e

#bash for loop
for i in {1..10}; do
    echo 'hello'
done

psql -v ON_ERROR_STOP=0 --username $POSTGRES_USER --dbname $POSTGRES_DB <<-EOSQL
    CREATE USER $POSTGRES_USER WITH PASSWORD '$POSTGRES_PASSWORD' LOGIN;
    CREATE DATABASE $POSTGRES_DB;
    GRANT ALL PRIVILEGES ON DATABASE $POSTGRES_DB TO $POSTGRES_USER;

    CREATE USER postgres WITH PASSWORD '$POSTGRES_PASSWORD' LOGIN;
    GRANT ALL PRIVILEGES ON DATABASE $POSTGRES_DB TO postgres;
EOSQL

for i in {1..10}; do
    echo 'hello'
done



# alias psql='PGPASSWORD="$POSTGRES_PASSWORD" psql -v ON_ERROR_STOP=0 --username "$POSTGRES_USER"'

# psql <<-EOSQL
#     CREATE USER $DJANGO_POSTGRES_USER WITH PASSWORD $DJANGO_DATABASE_PASSWORD LOGIN;
#     GRANT ALL PRIVILEGES ON DATABASE $DJANGO_POSTGRES_DB TO $DJANGO_POSTGRES_USER;
# EOSQL

# # create database if not exists
# # apparently needed because psql doesn't support 
# # the IF NOT EXISTS clause, weird
# psql -tc "select 1 from pg_database where datname='$POSTGRES_DB'" \
# | grep -q 1 \
# | echo "Database $POSTGRES_DB already exists, skipping creation." \
# || psql -c "CREATE DATABASE $POSTGRES_DB" \
# | echo "Database $POSTGRES_DB created."

# psql <<-EOSQL
#     GRANT ALL PRIVILEGES ON DATABASE $POSTGRES_DB TO $POSTGRES_USER;
#     GRANT ALL PRIVILEGES ON DATABASE $POSTGRES_DB TO postgres;
# EOSQL
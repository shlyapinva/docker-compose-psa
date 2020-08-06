#!/bin/bash

set -e

POSTGRESQL_URL="postgresql://worker:worker@db/app"

>&2 echo "!!!!!!!! Check conteiner_a for available !!!!!!!!"

until curl $POSTGRESQL_URL; do
  >&2 echo "db is unavailable - sleeping"
  sleep 1
done

>&2 echo "db is up - executing command"

exec $cmd 

#!/usr/bin/env bash
set -eux

# Use absolute paths
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

# Config source .env and extras
source ${REPO_ROOT}/src/.env
CONTAINER_NAME="cont_fc_db"

# Start Postgres container (detached)
docker run --name $CONTAINER_NAME \
  -e POSTGRES_USER=$DB_USER \
  -e POSTGRES_PASSWORD=$DB_PASS \
  -e POSTGRES_DB=$DB_NAME \
  -p $DB_PORT:5432 \
  -d postgres:16

echo "Waiting for Postgres to be ready..."
# Wait for Postgres to accept connections
until docker exec $CONTAINER_NAME pg_isready -U $DB_USER > /dev/null 2>&1; do
  sleep 1
done

echo "Postgres is up!"

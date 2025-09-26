#!/bin/bash
set -eux

# Define the absolute path to the repo root
REPO_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
echo "Repo root: $REPO_ROOT"

echo "Cleaning old lambda package..."
rm -f "$REPO_ROOT/lambda.zip"
rm -rf "$REPO_ROOT/package/"

echo "Installing dependencies in Lambda-compatible Docker..."
docker run --rm -v "$REPO_ROOT":/var/task python:3.11-bullseye bash -c "
    pip install --upgrade pip
    pip install -r /var/task/api/requirements.txt -t /var/task/package
"

echo "Copying application code..."
cp -r "$REPO_ROOT/api/"* "$REPO_ROOT/package/"

echo "Creating lambda.zip..."
cd "$REPO_ROOT/package"
zip -r "$REPO_ROOT/lambda.zip" . > /dev/null
cd "$REPO_ROOT"

echo "Cleaning up..."
rm -rf "$REPO_ROOT/package/"

echo "Lambda package created: $REPO_ROOT/lambda.zip"

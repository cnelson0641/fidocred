#!/bin/bash
set -eux

# Define the absolute path to the repo root
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "Repo root: $REPO_ROOT"

echo "Cleaning old lambda package..."
rm -f "$REPO_ROOT/artifacts/lambda.zip"
rm -rf "$REPO_ROOT/artifacts/package/"

echo "Installing dependencies in Lambda-compatible Docker..."
docker run --rm -v "$REPO_ROOT":/repo python:3.11-bullseye bash -c "
    pip install --upgrade pip
    pip install -r /repo/api/requirements.txt -t /repo/artifacts/package
"

echo "Copying application code..."
cp -r "$REPO_ROOT/api/"* "$REPO_ROOT/artifacts/package/"

echo "Creating lambda.zip..."
cd "$REPO_ROOT/artifacts/package"  # Have to cd because zip doesnt support -C on all platforms
zip -r "$REPO_ROOT/artifacts/lambda.zip" .
cd -  # Cd back

echo "Cleaning up..."
rm -rf "$REPO_ROOT/artifacts/package/"

echo "Lambda package created: $REPO_ROOT/artifacts/lambda.zip"
echo "SUCCESS!!!!!!!"

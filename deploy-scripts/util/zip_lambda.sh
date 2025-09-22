#!/bin/bash
set -eux

# Move to repo root
cd "$(dirname "$0")/../.."

echo "Cleaning old lambda package..."
rm -f lambda.zip
rm -rf package/

echo "Installing dependencies..."
# Install Python dependencies into a temporary folder
pip install -r api/requirements.txt -t package/

echo "Copying application code..."
cp -r api/* package/

echo "Creating lambda.zip..."
cd package
zip -r ../../lambda.zip . > /dev/null
cd ..

echo "Cleaning up..."
rm -rf package/

echo "Lambda package created: lambda.zip"


#!/bin/bash
set -eux

cd "$(dirname "$0")/../src"

python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

uvicorn api.main:app --host 0.0.0.0 --port 8000 --reload

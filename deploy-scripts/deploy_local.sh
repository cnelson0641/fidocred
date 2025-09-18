#!/bin/bash
set -eux

cd "$(dirname "$0")/../api"

python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

uvicorn main:app --host 0.0.0.0 --port 8000 --reload

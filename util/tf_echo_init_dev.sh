#!/bin/bash

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

CI_ENVIRONMENT_NAME='dev' . ${REPO_ROOT}/cicd/ci_env_vars.sh > /dev/null
echo tofu init $TF_BACKEND_CONFIG


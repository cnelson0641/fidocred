#!/bin/bash

# GitLab environment
export GITLAB_ENV=${CI_ENVIRONMENT_NAME}

# Terraform backend
export TF_BACKEND_BUCKET="fidocred-${GITLAB_ENV}-tfstate"
export TF_BACKEND_REGION="us-east-1"
export TF_BACKEND_LOCK_TABLE="fidocred-${GITLAB_ENV}-locks"
export TF_BACKEND_CONFIG="-backend-config=bucket=${TF_BACKEND_BUCKET} \
	-backend-config=region=${TF_BACKEND_REGION} \
	-backend-config=dynamodb_table=${TF_BACKEND_LOCK_TABLE} \
	-backend-config=encrypt=true \
    -backend-config=key=${GITLAB_ENV}-terraform.tfstate"

# Echo for reference
echo GITLAB_ENV - $GITLAB_ENV
echo TF_BACKEND_BUCKET - $TF_BACKEND_BUCKET
echo TF_BACKEND_REGION - $TF_BACKEND_REGION
echo TF_BACKEND_LOCK_TABLE -  $TF_BACKEND_LOCK_TABLE
echo TF_BACKEND_CONFIG - $TF_BACKEND_CONFIG

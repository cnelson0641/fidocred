#!/bin/bash

# GitLab environment
export GITLAB_ENV="$CI_ENVIRONMENT_NAME"

# Terraform backend
export TF_BACKEND_BUCKET="fidocred-${GITLAB_ENV}-tfstate"
export TF_BACKEND_REGION="us-east-1"
export TF_BACKEND_LOCK_TABLE="fidocred-${GITLAB_ENV}-locks"
export TF_BACKEND_CONFIG="-backend-config=bucket=${TF_BACKEND_BUCKET} \
	-backend-config=region=${TF_BACKEND_REGION} \
	-backend-config=dynamodb_table=${TF_BACKEND_LOCK_TABLE} \
	-backend-config=encrypt=true"

# Backend keys
export TF_BACKEND_KEY_NETWORK="-backend-config=key=network/terraform.tfstate"
export TF_BACKEND_KEY_DB="-backend-config=key=db/terraform.tfstate"
export TF_BACKEND_KEY_APP="-backend-config=key=app/terraform.tfstate"

# Terraform var groups
export TF_NETWORK_VARS=""
export TF_DB_VARS="-var=remote_state_bucket=${TF_BACKEND_BUCKET} \
	-var=remote_state_region=${TF_BACKEND_REGION} \
	-var=remote_state_key_network=network/terraform.tfstate \
	-var=remote_state_lock_table=${TF_BACKEND_LOCK_TABLE}"
export TF_APP_VARS="-var=remote_state_bucket=${TF_BACKEND_BUCKET} \
	-var=remote_state_region=${TF_BACKEND_REGION} \
	-var=remote_state_key_network=network/terraform.tfstate \
	-var=remote_state_key_db=db/terraform.tfstate \
	-var=remote_state_lock_table=${TF_BACKEND_LOCK_TABLE}"

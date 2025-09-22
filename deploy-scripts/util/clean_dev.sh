#!/bin/bash
set -eux

export AWS_PROFILE=fc-dev-admin

echo "Cleaning up DEV environment in AWS..."

# -------------------
# 1. Delete Lambda functions
# -------------------
echo "Deleting Lambda functions..."
aws lambda list-functions \
  --query "Functions[?starts_with(FunctionName,'dev-')].FunctionName" \
  --output text | xargs -n 1 -r aws lambda delete-function --function-name

# -------------------
# 2. Delete API Gateway (HTTP API)
# -------------------
echo "Deleting API Gateway HTTP APIs..."
aws apigatewayv2 get-apis \
  --query "Items[?starts_with(Name,'dev-')].ApiId" \
  --output text | xargs -n 1 -r aws apigatewayv2 delete-api --api-id

# -------------------
# 3. Delete IAM roles and policies
# -------------------
echo "Deleting IAM roles..."
aws iam list-roles \
  --query "Roles[?starts_with(RoleName,'dev-')].RoleName" \
  --output text | xargs -n 1 -r aws iam delete-role --role-name

echo "Deleting IAM policies..."
aws iam list-policies --scope Local \
  --query "Policies[?starts_with(PolicyName,'dev-')].Arn" \
  --output text | xargs -n 1 -r aws iam delete-policy --policy-arn

# -------------------
# 4. Delete CloudWatch log groups
# -------------------
echo "Deleting CloudWatch log groups..."
aws logs describe-log-groups \
  --query "logGroups[?starts_with(logGroupName,'/aws/lambda/dev')].logGroupName" \
  --output text | xargs -n 1 -r aws logs delete-log-group --log-group-name

echo "DEV cleanup complete!"


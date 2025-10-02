#!/bin/bash
set -eux

# -------------------
# Configuration
# -------------------
ENV="${1:-dev}"  # pass dev/test/PROD as first argument, default=dev
AWS_PROFILE="fc-${ENV}-admin"
export AWS_PROFILE

PREFIX="fidocred-${ENV}"

echo "Cleaning up ${ENV} environment in AWS..."

# -------------------
# 1. Delete Lambda functions
# -------------------
echo "Deleting Lambda functions..."
aws lambda list-functions \
  --query "Functions[?starts_with(FunctionName,'$PREFIX')].FunctionName" \
  --output text | xargs -n 1 -r aws lambda delete-function --function-name

# -------------------
# 2. Delete API Gateway (HTTP API)
# -------------------
echo "Deleting API Gateway HTTP APIs..."
aws apigatewayv2 get-apis \
  --query "Items[?starts_with(Name,'$PREFIX')].ApiId" \
  --output text | xargs -n 1 -r aws apigatewayv2 delete-api --api-id

# -------------------
# 3. Delete IAM roles and policies
# -------------------
echo "Deleting IAM roles..."
for ROLE in $(aws iam list-roles --query "Roles[?starts_with(RoleName,'$PREFIX')].RoleName" --output text); do
    echo "Cleaning role: $ROLE"

    # Detach managed policies
    aws iam list-attached-role-policies --role-name "$ROLE" \
      --query 'AttachedPolicies[].PolicyArn' --output text | \
      xargs -n 1 -r aws iam detach-role-policy --role-name "$ROLE" --policy-arn

    # Delete inline policies
    aws iam list-role-policies --role-name "$ROLE" \
      --query 'PolicyNames' --output text | \
      xargs -n 1 -r aws iam delete-role-policy --role-name "$ROLE" --policy-name

    # Delete the role itself
    aws iam delete-role --role-name "$ROLE"
done

echo "Deleting IAM policies..."
aws iam list-policies --scope Local \
  --query "Policies[?starts_with(PolicyName,'$PREFIX')].Arn" \
  --output text | xargs -n 1 -r aws iam delete-policy --policy-arn

# -------------------
# 4. Delete CloudWatch log groups
# -------------------
echo "Deleting CloudWatch log groups..."
aws logs describe-log-groups \
  --query "logGroups[?starts_with(logGroupName,'/aws/lambda/$PREFIX')].logGroupName" \
  --output text | xargs -n 1 -r aws logs delete-log-group --log-group-name

echo "${ENV} cleanup complete!"


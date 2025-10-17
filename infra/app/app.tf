##################
# Lambda Function
##################
# Lambda IAM Role
resource "aws_iam_role" "lambda_role" {
  name = "fidocred-lambda-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action    = "sts:AssumeRole"
      Effect    = "Allow"
      Principal = { Service = "lambda.amazonaws.com" }
    }]
  })
}

# Attach Lambda perms to IAM role
resource "aws_iam_role_policy_attachment" "lambda_basic" {
  role       = aws_iam_role.lambda_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

# Security group
resource "aws_security_group" "lambda_sg" {
  name        = "fidocred-lambda-sg"
  description = "Lambda security group"
  vpc_id      = data.terraform_remote_state.network.outputs.network.vpc_id

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# SG rule to allow lambda sg to talk to db sg
resource "aws_security_group_rule" "lambda_to_db" {
  type                        = "egress"
  from_port                   = 5432
  to_port                     = 5432
  protocol                    = "tcp"
  security_group_id            = aws_security_group.lambda_sg.id
  destination_security_group_id = data.terraform_remote_state.db.outputs.db_sg_id
}


# Lambda Function
resource "aws_lambda_function" "fastapi_lambda" {
  function_name    = "fidocred-lambdafunc"
  handler          = "main.handler"
  runtime          = "python3.11"
  role             = aws_iam_role.lambda_role.arn
  filename         = "${path.module}/../../artifacts/lambda.zip"
  source_code_hash = filebase64sha256("${path.module}/../../artifacts/lambda.zip")

  vpc_config {
    subnet_ids         = [data.terraform_remote_state.network.outputs.network.private_subnet_id]
    security_group_ids = [aws_security_group.lambda_sg.id]
  }
}

##################
# API Gateway
##################
# API Gateway
resource "aws_apigatewayv2_api" "http_api" {
  name          = "fidocred-apigateway"
  protocol_type = "HTTP"
}

# Lambda integration
resource "aws_apigatewayv2_integration" "lambda_integration" {
  api_id                 = aws_apigatewayv2_api.http_api.id
  integration_type       = "AWS_PROXY"
  integration_uri        = aws_lambda_function.fastapi_lambda.arn
  payload_format_version = "2.0"
}

# Default route
resource "aws_apigatewayv2_route" "default_route" {
  api_id    = aws_apigatewayv2_api.http_api.id
  route_key = "ANY /{proxy+}"
  target    = "integrations/${aws_apigatewayv2_integration.lambda_integration.id}"
}

# Empty route
resource "aws_apigatewayv2_route" "empty_route" {
  api_id    = aws_apigatewayv2_api.http_api.id
  route_key = "ANY /"
  target    = "integrations/${aws_apigatewayv2_integration.lambda_integration.id}"
}

# Deployment
resource "aws_apigatewayv2_deployment" "deployment" {
  api_id = aws_apigatewayv2_api.http_api.id
  depends_on = [
    aws_apigatewayv2_route.default_route,
    aws_apigatewayv2_route.empty_route
  ]
}

# Default stage (only one)
resource "aws_apigatewayv2_stage" "stage" {
  api_id        = aws_apigatewayv2_api.http_api.id
  name          = "$default"
  deployment_id = aws_apigatewayv2_deployment.deployment.id
}

# Lambda permissions for API Gateway
resource "aws_lambda_permission" "apigw_permission" {
  statement_id  = "AllowAPIGatewayInvoke"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.fastapi_lambda.function_name
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${aws_apigatewayv2_api.http_api.execution_arn}/${aws_apigatewayv2_stage.stage.name}/*/*"
}

###############################################
# DB - Aurora Serverlessv2 PostgreSQL Cluster
###############################################
# Aurora Serverless Security Group
resource "aws_security_group" "db_sg" {
  name        = "fidocred-db-sg"
  description = "Allow Aurora PostgreSQL access only from Lambda"
  vpc_id      = data.terraform_remote_state.network.outputs.network.vpc_id

  ingress {
    from_port       = 5432
    to_port         = 5432
    protocol        = "tcp"
    security_groups = [aws_security_group.lambda_sg.id]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# Aurora Serverless v2 Postgres Cluster
resource "aws_rds_cluster" "aurora_serverless" {
  cluster_identifier      = "fidocred-aurora"
  engine                  = "aurora-postgresql"
  engine_version          = "15.4"
  database_name           = "fidocred"
  master_username         = var.db_user
  master_password         = var.db_pass
  skip_final_snapshot     = true
  storage_encrypted       = true
  backup_retention_period = 2
  vpc_security_group_ids  = [aws_security_group.db_sg.id]

  # Serverless v2 scaling
  engine_mode = "serverless"
  scaling_configuration {
    min_capacity             = 1
    max_capacity             = 1
    auto_pause               = true
    seconds_until_auto_pause = 300
  }
}

# Aurora Serverless Cluster Instance
resource "aws_rds_cluster_instance" "aurora_serverless_instance" {
  cluster_identifier = aws_rds_cluster.aurora_serverless.id
  engine             = aws_rds_cluster.aurora_serverless.engine
  engine_version     = aws_rds_cluster.aurora_serverless.engine_version
  instance_class     = "db.serverless"
}

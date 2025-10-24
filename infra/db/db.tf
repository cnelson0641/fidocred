###############################################
# DB - Aurora Serverlessv2 PostgreSQL Cluster
###############################################
# Aurora Serverless Security Group
resource "aws_security_group" "db_sg" {
  name        = "fidocred-db-sg"
  description = "Allow Aurora PostgreSQL access only from Lambda"
  vpc_id      = var.vpc_id

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# DB Subnet Group
resource "aws_db_subnet_group" "aurora_subnet_group" {
  name        = "fidocred-aurora-subnet-group"
  description = "Aurora subnet group"
  subnet_ids  = [var.private_subnet_id_1,var.private_subnet_id_2]
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
  backup_retention_period = 1
  vpc_security_group_ids  = [aws_security_group.db_sg.id]
  db_subnet_group_name    = aws_db_subnet_group.aurora_subnet_group.name

  # Serverless v2 scaling
  engine_mode = "provisioned"
  serverlessv2_scaling_configuration {
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

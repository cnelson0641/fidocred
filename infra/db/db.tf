###############################################
# DB - RDS PostgreSQL 16.9 db.t3.micro
###############################################
# DB Security Group
resource "aws_security_group" "db_sg" {
  name        = "fidocred-db-sg"
  description = "Allow DB access only from Lambda"
  vpc_id      = var.vpc_id

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# DB Subnet Group
resource "aws_db_subnet_group" "db_subnet_group" {
  name        = "fidocred-db-subnet-group"
  description = "DB subnet group"
  subnet_ids  = [var.private_subnet_id, var.private_subnet_id2]
}

# RDS MySQL DB
resource "aws_db_instance" "postgre-db" {
  identifier              = "fidocred-rds-postgre-db"
  # Networking
  db_subnet_group_name    = aws_db_subnet_group.db_subnet_group.name
  multi_az                = false
  availability_zone       = "us-east-1a"
  # DB Engine
  engine                  = "postgres"
  engine_version          = "16.9"
  # Creds
  username                = var.db_user
  password                = var.db_pass
  # CPU, Storage, Other
  instance_class          = "db.t4g.micro"
  storage_type            = "gp3"
  allocated_storage       = 20
  max_allocated_storage   = 20
  skip_final_snapshot     = true
  publicly_accessible     = false
  backup_retention_period = 0
}

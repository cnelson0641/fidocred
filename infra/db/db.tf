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
  subnet_ids  = [var.private_subnet_id]
}

# RDS MySQL DB
resource "aws_db_instance" "postgre-db" {
	identifier = "fidocred-rds-postgre-db"
    db_subnet_group_name = aws_db_subnet_group.db_subnet_group.name
    engine = "postgres"
    engine_version = "16.9"
    instance_class = "db.t3.micro"
    storage_type = "gp3"
    allocated_storage = 1
    max_allocated_storage = 5
    username = var.db_user
    password = var.db_pass
    skip_final_snapshot = true
    publicly_accessible = false
    backup_retention_period = 0
}

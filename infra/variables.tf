variable "aws_region" {
  description = "AWS region to deploy into"
  type        = string
  default     = "us-east-1"
}

variable "env_name" {
  description = "PROD or test environment."
  type        = string
}

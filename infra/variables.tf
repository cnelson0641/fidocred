variable "aws_region" {
  description = "AWS region to deploy into"
  type        = string
  default     = "us-east-1"
}

variable "env_name" {
  description = "Dev, test, or PROD environment."
  type        = string
}

variable "aws_access_key" {
      type = string
}

variable "aws_secret_key" {
      type = string
}

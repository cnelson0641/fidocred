#############
# General
#############
variable "gitlab_env" {
  description = "Dev, test, or PROD environment."
  type        = string
  validation {
    condition     = contains(["dev", "test", "PROD"], var.gitlab_env)
    error_message = "gitlab_env must be: dev, test, PROD"
  }
}

#############
# AWS
#############
variable "region" {
  type    = string
  default = "us-east-1"
}

variable "availability_zone" {
  type    = string
  default = "us-east-1a"
}

variable "db_user" {
  type    = string
  default = "fc-admin"
}

variable "db_pass" {
  type    = string
  default = "FidoCredDogzRule99%*"
}

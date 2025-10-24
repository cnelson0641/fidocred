variable "vpc_id" {
  type = string
}

variable "private_subnet_id_1" {
  type = string
}

variable "public_subnet_id" {
  type = string
}

variable "db_sg_id" {
  type = string
}

variable "db_user" {
  type    = string
  default = "fc-admin"
}

variable "db_pass" {
  type    = string
  default = "FidoCredDogzRule99%*"
}

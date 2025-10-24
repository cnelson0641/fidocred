variable "vpc_id" {
  type = string
}

variable "private_subnet_id_1" {
  type = string
}

variable "private_subnet_id_2" {
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

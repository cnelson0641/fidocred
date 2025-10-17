variable "remote_state_bucket" {}
variable "remote_state_key" {}
variable "remote_state_region" {}
variable "remote_state_lock_table" {}

variable "db_user" {
    type = string
    default = "fc-admin"
}

variable "db_pass" {
    type = string
    default = "FidoCredDogzRule99%*"
}

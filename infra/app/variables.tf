variable "remote_state_bucket" {}
variable "remote_state_key_network" {}
variable "remote_state_key_db" {}
variable "remote_state_region" {}
variable "remote_state_lock_table" {}

variable "db_user" {
    type = string
    default = "fc-admin"
}

variable "db_pass" {
    type = string
    defualt = "FidoCredDogzRule99%*"
}

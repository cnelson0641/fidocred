terraform {
  backend "gitlab" {
    project     = "FidoCred/fidocred-api"
    environment = var.env_name
  }
}

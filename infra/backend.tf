terraform {
  backend "gitlab" {
    project = "FidoCred/fidocred-api"
    token   = var.gitlab_token
    branch  = var.env_name
  }
}

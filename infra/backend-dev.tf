terraform {
  backend "http" {
    address        = "https://gitlab.com/api/v4/projects/74343031/terraform/state/dev"
    lock_address   = "https://gitlab.com/api/v4/projects/74343031/terraform/state/dev/lock"
    unlock_address = "https://gitlab.com/api/v4/projects/74343031/terraform/state/dev/lock"
    username       = "gitlab-ci-token"
    password       = "CI_JOB_TOKEN"
  }
}


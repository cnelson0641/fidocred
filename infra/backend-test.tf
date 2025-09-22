terraform {
  backend "http" {
    address        = "https://gitlab.com/api/v4/projects/74343031/terraform/state/test"
    lock_address   = "https://gitlab.com/api/v4/projects/74343031/terraform/state/test/lock"
    unlock_address = "https://gitlab.com/api/v4/projects/74343031/terraform/state/test/lock"
    username       = "gitlab-ci-token"
    password       = "CI_JOB_TOKEN"
  }
}


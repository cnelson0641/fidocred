variable "gitlab_env" {
    description = "Dev, test, or PROD environment."
    type        = string
    validation {
        condition = contains(["dev", "test", "PROD", var.gitlab_env)
        error_message = "gitlab_env must be: dev, test, PROD"
    }
}

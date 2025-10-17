data "terraform_remote_state" "network" {
    backend = "s3"
    config = {
        bucket = var.remote_state_bucket
        key = var.remote_state_key_network
        region = var.remote_state_region
        dynamodb_table = var.remote_state_lock_table
        encrypt = true
    }
}

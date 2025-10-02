terraform {
    backend "s3" {
        bucket = "fidocred-dev-tfstate"
        key = "terraform.tfstate"
        region = "us-east-1"
        dynamodb_table = fidocred-dev-locks"
        encrypt = true
    }
}

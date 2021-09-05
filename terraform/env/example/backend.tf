terraform {
  backend "s3" {
    bucket = "BUCKET_NAME_HERE!!!" # I usually use 'terraform-backend-${REPOSITORY_NAME}-${AWS_ACCOUNT_ID}'.
    key    = "terraform.tfstate"   # If you forget to specify key, terraform automatically create a file named 'yes'.
    region = "ap-northeast-1"
  }
}

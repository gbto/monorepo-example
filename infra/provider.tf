provider "aws" {
  region  = var.aws_region
  profile = "gbto-mfa"
}
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "4.3.0"
    }
  }
}

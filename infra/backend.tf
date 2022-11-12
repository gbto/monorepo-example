terraform {
  backend "s3" {
    bucket  = "data-platform-tfstates-dev"
    key     = "pants-monorepo-dev.tfstate"
    region  = "eu-west-1"
    encrypt = true
  }
}

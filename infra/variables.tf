variable "project_name" {
  description = "The name of the project"
  type        = string
  default     = "gbto"
}
variable "env_name" {
  description = "Environment the ressources are instantiated in"
  type        = string
  default     = "dev"
}

variable "aws_region" {
  description = "AWS region in which to instantiate the resources"
  type        = string
  default     = "eu-west-1"
}

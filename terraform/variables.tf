variable "aws_region" {
  description = "AWS region"
  type        = string
}

variable "availability_zones" {
  description = "Availability zones"
  type        = list(string)
}

variable "container_image" {
  description = "Public container image to deploy"
  type        = string
}


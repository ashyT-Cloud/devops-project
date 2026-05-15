variable "aws_region" {
  description = "AWS region to deploy into"
  type        = string
  default     = "us-east-1"
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t2.micro"
}

variable "ami_id" {
  description = "Ubuntu 24.04 LTS AMI ID for us-east-1"
  type        = string
  default     = "ami-05cf1e9f73fbad2e2"
}

variable "key_name" {
  description = "Name of the SSH key pair in aws"
  type        = string
}

variable "project_name" {
  description = "Used to tag and name all resources"
  type        = string
  default     = "devops-project"
}

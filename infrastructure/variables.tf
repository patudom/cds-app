variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "environment" {
  description = "Environment name"
  type        = string
  default     = "production"
}

variable "cds_portal_image" {
  description = "Docker image URI for cds-portal"
  type        = string
  # Example: "123456789012.dkr.ecr.us-east-1.amazonaws.com/cds-portal:latest"
}

variable "cds_hubble_image" {
  description = "Docker image URI for cds-hubble"
  type        = string
  # Example: "123456789012.dkr.ecr.us-east-1.amazonaws.com/cds-hubble:latest"
}

variable "cds_portal_min_capacity" {
  description = "Minimum number of tasks for cds-portal"
  type        = number
  default     = 1
}

variable "cds_portal_max_capacity" {
  description = "Maximum number of tasks for cds-portal"
  type        = number
  default     = 10
}

variable "cds_hubble_min_capacity" {
  description = "Minimum number of tasks for cds-hubble"
  type        = number
  default     = 1
}

variable "cds_hubble_max_capacity" {
  description = "Maximum number of tasks for cds-hubble"
  type        = number
  default     = 10
}

variable "cloudfront_secret" {
  description = "Secret value for CloudFront custom header to prevent direct ALB access"
  type        = string
  sensitive   = true
  default     = "change-me-to-a-secure-random-string"
}
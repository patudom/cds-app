output "alb_dns_name" {
  description = "DNS name of the load balancer"
  value       = aws_lb.main.dns_name
}

output "alb_zone_id" {
  description = "Zone ID of the load balancer"
  value       = aws_lb.main.zone_id
}

output "vpc_id" {
  description = "ID of the VPC"
  value       = aws_vpc.main.id
}

output "private_subnet_ids" {
  description = "IDs of the private subnets"
  value       = aws_subnet.private[*].id
}

output "public_subnet_ids" {
  description = "IDs of the public subnets"
  value       = aws_subnet.public[*].id
}

output "ecs_cluster_name" {
  description = "Name of the ECS cluster"
  value       = aws_ecs_cluster.main.name
}

output "cds_portal_secrets_arn" {
  description = "ARN of the CDS Portal secrets in Secrets Manager"
  value       = aws_secretsmanager_secret.cds_portal_secrets.arn
}

output "cds_hubble_secrets_arn" {
  description = "ARN of the CDS Hubble secrets in Secrets Manager"
  value       = aws_secretsmanager_secret.cds_hubble_secrets.arn
}

output "cloudfront_domain_name" {
  description = "Domain name of the CloudFront distribution"
  value       = aws_cloudfront_distribution.apps.domain_name
}

output "cloudfront_distribution_id" {
  description = "ID of the CloudFront distribution"
  value       = aws_cloudfront_distribution.apps.id
}

output "cloudfront_https_url" {
  description = "HTTPS URL of the CloudFront distribution"
  value       = "https://${aws_cloudfront_distribution.apps.domain_name}"
}

output "cds_portal_url" {
  description = "URL for accessing CDS Portal"
  value       = "https://${aws_cloudfront_distribution.apps.domain_name}"
}

output "cds_hubble_url" {
  description = "URL for accessing CDS Hubble"
  value       = "https://${aws_cloudfront_distribution.apps.domain_name}/hubbles-law"
}

output "ecr_repository_cds_portal_url" {
  description = "URL of the CDS Portal ECR repository"
  value       = aws_ecr_repository.cds_portal.repository_url
}

output "ecr_repository_cds_hubble_url" {
  description = "URL of the CDS Hubble ECR repository"
  value       = aws_ecr_repository.cds_hubble.repository_url
}

output "codepipeline_name" {
  description = "Name of the CodePipeline"
  value       = aws_codepipeline.cds_pipeline.name
}

output "github_connection_arn" {
  description = "ARN of the GitHub connection"
  value       = aws_codestarconnections_connection.github.arn
}
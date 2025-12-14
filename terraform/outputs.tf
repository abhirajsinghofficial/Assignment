output "load_balancer_dns" {
  description = "Public endpoint of the application"
  value       = aws_lb.this.dns_name
}


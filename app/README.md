# SimpleTimeService

SimpleTimeService is a minimal HTTP microservice that returns the current timestamp and the IP address of the client making the request.

---

## Purpose

This service demonstrates:
- Minimal microservice design
- Docker containerization
- Running containers as a non-root user
- Clear documentation for team usage

---

## Service Endpoint

- GET /

### Example Response

{
  "timestamp": "2025-12-14T10:21:43.123456+00:00",
  "ip": "203.0.113.10"
}

## Docker Image (Public Registry)

https://hub.docker.com/r/abhirajsinghofficial/simpletimeservice

## CI/CD Pipeline

This repository includes a GitHub Actions pipeline that:

- Builds the container image
- Pushes it to DockerHub
- Deploys infrastructure using Terraform

Secrets are stored securely in GitHub Actions and are not committed
to the repository.


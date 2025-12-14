# Container Application Infrastructure (Terraform)

This Terraform configuration deploys a containerized application to AWS using ECS Fargate.

---

## Prerequisites

Install the following tools:

- Terraform  
  https://developer.hashicorp.com/terraform/downloads

- AWS CLI  
  https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html

- A public container image (DockerHub or equivalent)

---

## AWS Authentication

No credentials are stored in this repository.

Authenticate using one of the following methods:

### Option1: AWS CLI
```bash
aws configure
```

### Option2: Environment Variables
```bash
export AWS_ACCESS_KEY_ID=xxxx
export AWS_SECRET_ACCESS_KEY=xxxx
export AWS_DEFAULT_REGION=us-east-1
```

## Deploy Infrastructure with terraform lifecycle below
```bash
terraform init
terraform plan
terraform apply
```
Type yes when prompted.

### Access the Application

After apply completes, Terraform outputs:

load_balancer_dns = <DNS_NAME>

Open in browser or curl:

curl http://<DNS_NAME>/

## Clean Up
```bash
terraform destroy
```

## Terraform Remote State

This project uses a remote Terraform backend.

State is stored in:
- S3 (for persistence)
- DynamoDB (for state locking)

These resources must exist before running Terraform.



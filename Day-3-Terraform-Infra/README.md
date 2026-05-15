# Day 3 — Infrastructure as Code with Terraform

## Project Overview

This project demonstrates Infrastructure as Code (IaC) using Terraform on AWS.

Terraform was used to provision an EC2 instance along with networking and security configurations completely through code without manually creating resources from the AWS Console.

---

# Project Structure

```bash
Day-3-Terraform-Infra/
├── main.tf
├── variables.tf
├── terraform.tfvars
├── output.tf
├── terraform.tfstate
└── terraform.tfstate.backup
```

---

# What Was Built

Using Terraform, the following infrastructure was provisioned:

- AWS EC2 Instance
- Security Group
- SSH Access Configuration
- Variable-based configuration
- Output values for public IP

---

# Terraform Workflow

```text
Write Terraform Code
        │
        ▼
terraform init
        │
        ▼
terraform plan
        │
        ▼
terraform apply
        │
        ▼
Infrastructure Created on AWS
```

---

# Files Explanation

## `main.tf`

Contains the main infrastructure configuration:

- AWS provider
- EC2 instance resource
- Security group rules

---

## `variables.tf`

Defines reusable variables such as:

- AWS region
- AMI ID
- Instance type
- Key pair name

---

## `terraform.tfvars`

Stores actual variable values.

Example:

```hcl
region        = "ap-south-1"
instance_type = "t2.micro"
```

---

## `output.tf`

Displays important outputs after deployment.

Example:

```hcl
output "public_ip" {
  value = aws_instance.web.public_ip
}
```

---

## `terraform.tfstate`

Terraform state file that tracks created infrastructure resources.

---

# Steps Performed

## 1. Install Terraform and Configure AWS CLI

Configured AWS credentials using IAM user access keys.

```bash
aws configure
```

---

## 2. Initialize Terraform

```bash
terraform init
```

Downloads required providers and initializes the project.

---

## 3. Validate Terraform Code

```bash
terraform validate
```

Checks configuration syntax and validity.

---

## 4. Preview Infrastructure Changes

```bash
terraform plan
```

Shows resources Terraform will create.

---

## 5. Create Infrastructure

```bash
terraform apply
```

Provisions resources on AWS.

---

## 6. Verify EC2 Instance

SSH into the created EC2 instance using:

```bash
ssh -i key.pem ubuntu@<public-ip>
```

---

# Key Concepts Learned

## Infrastructure as Code (IaC)

Infrastructure can be managed entirely through code instead of manual AWS Console operations.

---

## Terraform State File

```text
terraform.tfstate
```

Tracks infrastructure resources created by Terraform.

---

## Variables

Variables make Terraform code reusable and configurable.

---

## Outputs

Outputs expose important values like public IP addresses.

---

## Idempotency

Running Terraform multiple times only applies required changes without duplicating resources.

---

## terraform destroy

```bash
terraform destroy
```

Deletes all infrastructure managed by Terraform.

---

# Commands Used

## Initialize

```bash
terraform init
```

## Validate

```bash
terraform validate
```

## Plan

```bash
terraform plan
```

## Apply

```bash
terraform apply
```

## Destroy

```bash
terraform destroy
```

---

# Final Outcome

By the end of Day 3:

- Infrastructure was provisioned entirely using code
- AWS EC2 instance was successfully deployed
- Terraform workflow was understood end-to-end
- Infrastructure management became repeatable and automated

---

# Next Step

## Day 4 — Continuous Deployment Pipeline

Upcoming topics:

- Automated deployment
- CI/CD integration
- Deployment automation
- Server provisioning workflows

---

*Part of the DevOps Hands-on Project Series.*

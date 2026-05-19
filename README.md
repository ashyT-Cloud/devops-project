#  DevOps Hands-on Project Series


![CI](https://github.com/ashyT-Cloud/devops-project/actions/workflows/ci.yml/badge.svg)



A complete hands-on DevOps learning journey covering Docker, CI/CD, Terraform, Kubernetes, Monitoring, and Cloud deployment.

---

# Project Roadmap

| Day | Topic | Status |
|------|--------|--------|
| Day 1 | Dockerized Flask Application | ✅ Completed |
| Day 2 | CI Pipeline with GitHub Actions | ✅ Completed |
| Day 3 | Infrastructure as Code with Terraform | ✅ Completed |
| Day 4 | Continuous Deployment Pipeline | ✅ Completed  |
| Day 5 | Monitoring with Prometheus & Grafana | 🔜 Upcoming |

---

# Repository Structure

```bash
DevOps-Projects/
│
├── Day-1-Dockerized-Flask-App/
│   ├── app.py
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── requirements.txt
│   └── README.md
│
├── Day-2-GitHubAction-CI/
│   ├── .github/
│   │   └── workflows/
│   │       └── ci.yml
│   ├── app.py
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── requirements.txt
│   ├── setup.cfg
│   ├── conftest.py
│   ├── tests/
│   │   └── test_app.py
│   └── README.md
│
├── Day-3-Terraform-Infra/
│   ├── main.tf
│   ├── variables.tf
│   ├── terraform.tfvars
│   ├── output.tf
│   ├── terraform.tfstate
│   └── terraform.tfstate.backup
│
├── Day-4-CD-Pipeline/
│   ├── app.py
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── requirements.txt
│   ├── conftest.py
│   ├── setup.cfg
│   ├── deploy.sh
│   ├── tests/
│   │   └── test_app.py
│   └── README.md
│
├── Day-5-Monitoring/
│
└── README.md
```

---

# Tech Stack

- Docker
- GitHub Actions
- Python
- Flask
- Terraform
- AWS
- Kubernetes
- Prometheus
- Grafana

---

# Day 1 — Dockerized Flask Application

### Topics Covered

- Docker basics
- Dockerfile creation
- Docker Compose
- Containerized Flask application

### Features

- Flask app containerization
- Multi-container setup
- Local container testing
- Docker image creation

---

# Day 2 — CI Pipeline with GitHub Actions

### Topics Covered

- GitHub Actions workflows
- CI pipeline automation
- Linting and formatting
- Automated testing
- Docker image automation

### Features

- flake8 lint checks
- black formatting validation
- pytest automation
- Docker image build and push
- GitHub Secrets integration

---

## Day 3 — Infrastructure as Code with Terraform

### Topics Covered

- Terraform basics
- AWS provider configuration
- EC2 provisioning
- Variables and outputs
- Terraform state management
- Infrastructure automation

---

## Day 4 — CD Pipeline: Auto Deploy on Push

### Topics Covered

- Continuous Deployment (CD)
- GitHub Actions workflow automation
- SSH automation to AWS EC2
- Docker deployment automation
- Smoke testing
- Automated production deployment

---

# Upcoming Projects


## Day 5 — Monitoring

- Prometheus setup
- Grafana dashboards
- Metrics monitoring
- Alerting system

---

# Learning Goals

This project series focuses on:

- Real-world DevOps workflow
- CI/CD automation
- Cloud infrastructure management
- Container orchestration
- Monitoring and observability
- Production-ready practices

---

# Author

Ashish Thakur

---

# License

This project is for learning and educational purposes.

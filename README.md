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
| Day 5 | Monitoring with Prometheus & Grafana | ✅ Completed |

──────── Extension: Kubernetes Journey ────────

| Day | Topic | Status |
|------|--------|--------|
| Day 6 | K8s Core Concepts (Pod, Deployment, Service) | ✅ Completed |
| Day 7 | ConfigMaps & Secrets + Probes | ✅ Completed |
| Day 8 | Auto Scaling + Rolling Updates | ✅ Completed |
| Day 9 | Helm | ✅ Completed  |
| Day 10 | AWS EKS Deployment | ✅ Completed |

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
│    ├── docker-compose.yml        # All 3 containers: app + prometheus + grafana
│    ├── prometheus.yml            # Scrape config — what Prometheus monitors
│    └── app/
│        ├── app.py                # Flask app with /metrics endpoint
│        ├── Dockerfile            # Multi-stage build
│        ├── requirements.txt      # Includes prometheus-flask-exporter
│        ├── conftest.py           # Pytest path config
│        ├── setup.cfg             # flake8 config
│        └── tests/
│            └── test_app.py       # Unit tests
│
├── Day-6-K8s-Basics/
├── Day-7-K8s-Config/
│   └── manifests/
│       ├── configmap.yaml
│       ├── secret.yaml
│       ├── deployment.yaml
│       └── service.yaml
└── Day-8-K8s-Scaling/
│    └── manifests/
│        ├── configmap.yaml      # unchanged from Day 7
│        ├── secret.yaml         # unchanged from Day 7
│        ├── deployment.yaml     # updated: rolling update strategy + resources
│        ├── service.yaml        # unchanged from Day 7
│        └── hpa.yaml            # NEW: HorizontalPodAutoscaler
├── Day-9-Helm/
│         └── flask-chart/
│              ├── Chart.yaml                  # chart metadata + version
│              ├── values.yaml                 # default values (all environments)
│              ├── values-staging.yaml         # staging overrides
│              ├── values-prod.yaml            # production overrides
│              └── templates/
│                  ├── _helpers.tpl            # reusable name + label helpers
│                  ├── deployment.yaml         # templated Deployment
│                  ├── service.yaml            # templated Service
│                  ├── configmap.yaml          # templated ConfigMap
│                  ├── secret.yaml             # templated Secret
│                  └── hpa.yaml                # conditional HPA
Day-10-EKS/
├── README.md
├── cluster.yaml
├── helm-values
│   ├── values-prod.yaml
│   └── values-staging.yaml
├── ingress.yaml
└── namespaces.yaml

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
- Python
- Flask
- Linux
- CI/CD
- Infrastructure as Code (IaC)

---

# DevOps Topics Covered

- Docker containerization
- GitHub Actions CI/CD
- Terraform infrastructure automation
- Continuous Deployment
- Monitoring and Observability
- AWS EC2 deployment
---

# Kubernetes Topics Covered

- Pods
- Deployments
- Services
- ConfigMaps
- Secrets
- Liveness Probes
- Readiness Probes
- Self-healing deployments

---

### Kubernetes Extension (Days 6–10)

- Kubernetes
- kubectl
- minikube
- Helm
- AWS EKS

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

## Day 5 — Monitoring with Prometheus & Grafana

Topics covered:

- Metrics collection
- Prometheus monitoring
- Grafana dashboards
- Docker Compose monitoring stack
- Application observability

# Complete CI/CD Workflow

```text
Code Push
   │
   ▼
CI Pipeline
(Lint → Test → Docker Build)
   │
   ▼
CD Pipeline
(Deploy to EC2)
   │
   ▼
Monitoring Stack
(Prometheus + Grafana)
```

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

# Final Outcome

By completing this project series:

- Applications were containerized using Docker
- CI/CD pipelines were automated using GitHub Actions
- Infrastructure was provisioned using Terraform
- Continuous deployment was implemented on AWS EC2
- Monitoring and observability were added using Prometheus and Grafana


# Author

Ashish Thakur

---

# License

This project is for learning and educational purposes.

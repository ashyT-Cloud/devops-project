# Day 4 — CD Pipeline: Auto Deploy on Push

## Project Overview

This project demonstrates a complete Continuous Deployment (CD) pipeline using GitHub Actions, Docker, AWS EC2, and Flask.

After every successful CI pipeline execution, the latest Docker image is automatically deployed to an AWS EC2 instance without any manual intervention.

---

# Project Structure

```bash
devops-project/
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── cd.yml
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
```

---

# What Was Built

The CD pipeline performs the following automatically:

- Waits for CI pipeline success
- Connects to AWS EC2 using SSH
- Copies deployment script to server
- Pulls latest Docker image from Docker Hub
- Stops old container
- Starts updated container
- Runs smoke test after deployment
- Deploys latest commit automatically

---

# Pipeline Flow

```text
Developer Pushes Code
          │
          ▼
CI Pipeline Runs
(lint → test → docker build)
          │
          ▼
CD Pipeline Triggered
          │
          ▼
SSH into EC2
          │
          ▼
Pull Latest Docker Image
          │
          ▼
Restart Container
          │
          ▼
Smoke Test
          │
          ▼
Application Live on EC2
```

---

# GitHub Actions CD Workflow

## `.github/workflows/cd.yml`

```yaml
name: CD Pipeline

on:
  workflow_run:
    workflows: ["CI Pipeline"]
    types:
      - completed
    branches: [main]

jobs:
  deploy:
    name: Deploy to EC2
    runs-on: ubuntu-latest

    if: ${{ github.event.workflow_run.conclusion == 'success' }}

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up SSH key
        run: |
          mkdir -p ~/.ssh
          echo "${{ secrets.EC2_SSH_KEY }}" > ~/.ssh/deploy_key.pem
          chmod 400 ~/.ssh/deploy_key.pem
          ssh-keyscan -H ${{ secrets.EC2_HOST }} >> ~/.ssh/known_hosts

      - name: Copy deploy script to EC2
        run: |
          scp -o StrictHostKeyChecking=no \
            -i ~/.ssh/deploy_key.pem \
            Day-4-CD-Pipeline/deploy.sh \
            ${{ secrets.EC2_USER }}@${{ secrets.EC2_HOST }}:~/deploy.sh

      - name: Run deploy script on EC2
        run: |
          ssh -o StrictHostKeyChecking=no \
            -i ~/.ssh/deploy_key.pem \
            ${{ secrets.EC2_USER }}@${{ secrets.EC2_HOST }} \
            "chmod +x ~/deploy.sh && \
             DOCKERHUB_USERNAME=${{ secrets.DOCKERHUB_USERNAME }} \
             APP_VERSION=${{ github.sha }} \
             ~/deploy.sh"

      - name: Smoke test
        run: |
          sleep 10
          curl -f http://${{ secrets.EC2_HOST }}:5000/health

      - name: Print deployment info
        run: |
          echo "Deployment successful"
          echo "Commit: ${{ github.sha }}"
```

---

# Deploy Script

## `deploy.sh`

```bash
#!/bin/bash

set -e

echo "Starting deployment..."

docker pull $DOCKERHUB_USERNAME/myapp:latest

docker stop myapp || true
docker rm myapp || true

docker run -d \
  --name myapp \
  --restart always \
  -p 5000:5000 \
  -e APP_VERSION=$APP_VERSION \
  $DOCKERHUB_USERNAME/myapp:latest

sleep 5

curl -f http://localhost:5000/health

echo "Deployment successful"
```

---

# Flask Application

## `app.py`

```python
from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify({
        "message": "Hello DevOps!",
        "version": os.getenv("APP_VERSION", "1.0.0")
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "ok",
        "version": os.getenv("APP_VERSION", "1.0.0")
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

---

# GitHub Secrets Required

Navigate to:

```text
GitHub Repository
→ Settings
→ Secrets and variables
→ Actions
```

Add the following secrets:

| Secret Name | Purpose |
|---|---|
| `EC2_HOST` | EC2 public IP |
| `EC2_USER` | EC2 SSH username |
| `EC2_SSH_KEY` | Full private SSH key |
| `DOCKERHUB_USERNAME` | Docker Hub username |
| `DOCKERHUB_TOKEN` | Docker Hub access token |

---

# Commands Used

## Test SSH Access

```bash
ssh -i devops-key.pem ubuntu@EC2_PUBLIC_IP
```

---

## Check Running Containers

```bash
docker ps
```

---

## Check Logs

```bash
docker logs myapp
```

---

## Test Application

```bash
curl http://EC2_PUBLIC_IP:5000/health
```

---

# Key Concepts Learned

## Continuous Deployment (CD)

Automatically deploys application changes after successful CI validation.

---

## workflow_run Trigger

The CD workflow only starts after the CI workflow completes successfully.

---

## SSH Automation

GitHub Actions securely connects to EC2 using SSH keys stored in GitHub Secrets.

---

## Smoke Testing

After deployment, a health endpoint verifies the application is running correctly.

---

## Docker Container Replacement

Old containers are stopped and replaced with updated containers automatically.

---

# Problems Fixed During Setup

| Error | Fix |
|---|---|
| Permission denied (publickey) | Corrected SSH key and EC2 user |
| SSH connection closed | Added correct authorized key |
| curl smoke test failed | Fixed application startup timing |
| Docker permission denied | Added ubuntu user to docker group |

---

# Final Outcome

By the end of Day 4:

- Fully automated CD pipeline was implemented
- Docker deployments became automatic
- EC2 deployment process was automated
- GitHub Actions integrated CI + CD successfully
- Production deployment workflow was completed

---

# Next Step

## Day 5 — Monitoring with Prometheus & Grafana

Upcoming topics:

- Metrics collection
- Monitoring dashboards
- Alerting setup
- Application observability

---

*Part of the DevOps Hands-on Project Series.*

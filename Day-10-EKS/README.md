# Day 10 — Amazon EKS + ALB Ingress + GitHub Actions CD

## Overview

On Day 10, I deployed my Flask application to **Amazon EKS (Elastic Kubernetes Service)** and exposed it publicly using an **AWS Application Load Balancer (ALB)** through Kubernetes Ingress.

I also integrated **GitHub Actions CD** to automate deployments into EKS using **Helm**, creating a production-style Kubernetes deployment workflow.

---

## Architecture

```text
Git Push
    ↓
GitHub Actions (CD)
    ↓
AWS Authentication
    ↓
EKS Cluster
    ↓
Helm Deployment
    ↓
AWS ALB Ingress
    ↓
ClusterIP Service
    ↓
Flask Pods
```

---

## Project Structure

```text
Day-10-EKS/
├── cluster.yaml
├── ingress.yaml
├── namespaces.yaml
├── helm-values/
│   ├── values-prod.yaml
│   └── values-staging.yaml
├── README.md
```

---

## What Was Implemented

### 1. Amazon EKS Cluster

Created an EKS cluster using `eksctl`.

```bash
eksctl create cluster -f cluster.yaml
```

Verified nodes:

```bash
kubectl get nodes
```

---

### 2. Multi-Environment Namespaces

Created isolated namespaces for:

- `production`
- `staging`

Applied namespaces:

```bash
kubectl apply -f namespaces.yaml
```

---

### 3. Helm Deployment to EKS

Reused the Helm chart created in Day 9 and deployed the Flask app into EKS.

Deployment command:

```bash
helm upgrade --install myapp-prod Day-9-Helm/flask-chart \
-f Day-10-EKS/helm-values/values-prod.yaml \
-n production
```

Verified resources:

```bash
kubectl get all -n production
```

---

### 4. AWS Load Balancer Controller

Installed and configured:

- AWS Load Balancer Controller
- IAM policy
- IRSA (IAM Roles for Service Accounts)

Verified:

```bash
kubectl get pods -n kube-system | grep aws
```

---

### 5. ALB Ingress

Configured Kubernetes Ingress to expose the Flask application externally using an internet-facing ALB.

Apply ingress:

```bash
kubectl apply -f ingress.yaml
```

Verify:

```bash
kubectl get ingress -n production
```

Example result:

```text
flask-ingress
k8s-producti-flasking-xxxxx.us-east-1.elb.amazonaws.com
```

---

### 6. GitHub Actions CD Pipeline

Configured a deployment workflow that:

1. Authenticates to AWS
2. Updates kubeconfig for EKS
3. Connects to Kubernetes cluster
4. Deploys using Helm
5. Verifies rollout
6. Performs smoke testing

Deployment workflow:

```text
Push → GitHub Actions → EKS → Helm → Rolling Deployment
```

---

## CI/CD Workflow

```text
Developer Push
      ↓
GitHub Actions
      ↓
AWS Credentials
      ↓
EKS Authentication
      ↓
Helm Upgrade
      ↓
Rolling Deployment
      ↓
Smoke Test
```

---

## Production Architecture

```text
Internet
    ↓
AWS ALB (Ingress)
    ↓
ClusterIP Service
    ↓
Flask Pods (3 replicas)
```

Why `ClusterIP`?

Since traffic is routed through Ingress:

```yaml
service:
  type: ClusterIP
```

is the recommended Kubernetes architecture.

---

## Real-World Issues Debugged

### 1. Wrong Kubernetes Context

Issue:

Resources were accidentally deployed to Minikube instead of EKS.

Fix:

```bash
kubectl config use-context iam-root-account@devops-cluster.us-east-1.eksctl.io
```

Lesson:

Always verify current cluster context.

---

### 2. ALB Controller IAM Permission Issue

Issue:

Ingress remained stuck and ALB was not created.

Error:

```text
AccessDenied:
elasticloadbalancing:DescribeListenerAttributes
```

Fix:

Updated AWS Load Balancer Controller IAM policy.

Lesson:

Cloud-native integrations commonly fail due to IAM permissions.

---

### 3. GitHub Actions EKS Authentication

Issue:

GitHub Actions successfully authenticated to AWS but failed to access Kubernetes.

Error:

```text
Unauthorized
```

Fix:

Configured EKS Access Entry for CI/CD IAM user.

Lesson:

Valid AWS credentials ≠ Kubernetes cluster authorization.

---

### 4. Rolling Deployment Failure

Issue:

Deployment timed out during rollout.

Root Cause:

GitHub Actions deployed a non-existing Docker image tag.

Fix:

Used stable Docker image tag (`1.0.0`) instead of SHA-based image tags.

---

## Key Commands Used

```bash
kubectl get nodes

kubectl get ingress -n production

kubectl get all -n production

kubectl rollout status deployment/myapp-prod-flask-chart -n production

helm upgrade --install myapp-prod Day-9-Helm/flask-chart \
-f Day-10-EKS/helm-values/values-prod.yaml \
-n production
```

---

## Skills Demonstrated

- Amazon EKS
- Kubernetes Ingress
- AWS ALB Integration
- Helm Deployments
- GitHub Actions CD
- IAM + IRSA
- Kubernetes Context Management
- HPA
- Rolling Deployments
- Smoke Testing
- Kubernetes Troubleshooting
- DevOps Debugging

---

## Outcome

Successfully deployed a Flask application to **Amazon EKS** with:

- ALB Ingress
- Helm deployment
- GitHub Actions CD
- Rolling deployments
- Smoke testing
- Production-style Kubernetes architecture

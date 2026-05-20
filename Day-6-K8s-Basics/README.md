# Day 6 — Kubernetes Core Concepts (Pod, Deployment, Service)


---

# 📌 Project Context

This project is part of a **10-Day DevOps + Kubernetes Journey**.

The original DevOps workflow (Days 1–5) included:

- Dockerized Flask application
- CI pipeline using GitHub Actions
- Infrastructure provisioning using Terraform
- CD pipeline deployment to EC2
- Monitoring using Prometheus & Grafana

From **Day 6 onward**, the same application is migrated into Kubernetes to learn production-grade orchestration concepts.

```text
Docker → CI/CD → Monitoring → Kubernetes → EKS
```

---

# 🚀 What Was Built

A fully working local Kubernetes environment running the Flask application using:

- minikube
- kubectl
- Pod manifests
- Deployment manifests
- Service manifests
- Self-healing Kubernetes workloads

---

# 🔄 How Day 6 Connects to Previous Days

```text
Day 1 → Flask app + Dockerfile
Day 2 → CI pipeline pushes image to Docker Hub
Day 3 → Terraform provisions EC2
Day 4 → CD pipeline deploys app to EC2
Day 5 → Monitoring stack added
Day 6 → Same app migrated into Kubernetes
```

The Docker image built in earlier days is now orchestrated using Kubernetes instead of standalone Docker containers.

---

# 📂 Project Structure

```text
Day-6-K8s-Basics/
│
├── manifests/
│   ├── pod.yaml
│   ├── deployment.yaml
│   └── service.yaml
│
└── README.md
```

---

# ☸️ Kubernetes Objects Used

| Object | Purpose |
|--------|---------|
| Pod | Runs the container |
| Deployment | Manages replicas and self-healing |
| Service | Exposes the application |
| ReplicaSet | Maintains desired replica count |

---

# 🧠 Kubernetes Architecture

```text
Cluster
└── Node
    └── Pod
        └── Container
```

```text
Deployment → ReplicaSet → Pods
Service → Exposes Pods
```

---

# 📄 Pod Manifest

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: flask-pod
spec:
  containers:
    - name: flask
      image: ashytcloud/myapp:latest
      ports:
        - containerPort: 5000
```

---

# 📄 Deployment Manifest

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: flask-deployment

spec:
  replicas: 2

  selector:
    matchLabels:
      app: flask

  template:
    metadata:
      labels:
        app: flask

    spec:
      containers:
        - name: flask
          image: ashytcloud/myapp:latest

          ports:
            - containerPort: 5000
```

---

# 📄 Service Manifest

```yaml
apiVersion: v1
kind: Service

metadata:
  name: flask-service

spec:
  type: NodePort

  selector:
    app: flask

  ports:
    - port: 80
      targetPort: 5000
      nodePort: 30080
```

---

# ⚙️ Installation

## Install kubectl

```bash
curl -LO "https://dl.k8s.io/release/$(curl -L -s \
https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"

sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
```

---

## Install minikube

```bash
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64

sudo install minikube-linux-amd64 /usr/local/bin/minikube
```

---

## Start Kubernetes Cluster

```bash
sudo apt-get install -y conntrack

minikube start --driver=docker --force
```

---

# 🚀 Deploy Application

```bash
kubectl apply -f manifests/pod.yaml

kubectl apply -f manifests/deployment.yaml

kubectl apply -f manifests/service.yaml
```

---

# 🔍 Useful kubectl Commands

```bash
kubectl get pods

kubectl get all

kubectl describe pod <pod-name>

kubectl logs <pod-name>

kubectl exec -it <pod-name> -- /bin/bash

kubectl scale deployment flask-deployment --replicas=4
```

---

# 💥 Self-Healing Demo

Delete a Pod manually:

```bash
kubectl delete pod <pod-name>
```

Kubernetes automatically creates a replacement Pod to maintain the desired replica count.

---

# 📊 Key Concepts Learned

- Pods
- Deployments
- Services
- ReplicaSets
- Label selectors
- Self-healing
- Scaling
- Declarative YAML configuration

---

# 🗺️ Kubernetes Roadmap

| Day | Topic | Status |
|------|--------|--------|
| Day 6 | Pod, Deployment, Service | ✅ Completed |
| Day 7 | ConfigMaps & Secrets | ⏳ Upcoming |
| Day 8 | Auto Scaling | ⏳ Upcoming |
| Day 9 | Helm | ⏳ Upcoming |
| Day 10 | AWS EKS | ⏳ Upcoming |

---

# 🎯 Outcome

Successfully migrated the Flask application from standalone Docker containers to a Kubernetes-managed deployment using minikube and kubectl.

This lays the foundation for advanced Kubernetes concepts and cloud-native deployments in upcoming days.

# Day 7 — ConfigMaps, Secrets + Health Checks

## Project Overview

This project demonstrates how to make a Kubernetes Flask deployment production-ready using:

- ConfigMaps
- Secrets
- Liveness Probes
- Readiness Probes

The existing Flask application was enhanced with externalized configuration and automatic health management using Kubernetes native features.

---

# Project Structure

```bash
devops-project/
└── Day-7-K8s-Config/
    └── manifests/
        ├── configmap.yaml
        ├── secret.yaml
        ├── deployment.yaml
        └── service.yaml
```

---

# What Was Built

The Kubernetes deployment now supports:

- External configuration using ConfigMaps
- Sensitive value management using Secrets
- Automatic container health monitoring
- Self-healing application behavior
- Readiness traffic control
- Environment variable injection

---

# Kubernetes Architecture

```text
                ┌──────────────────┐
                │   ConfigMap      │
                │  APP_ENV         │
                │  APP_VERSION     │
                └────────┬─────────┘
                         │
                         ▼
┌─────────────┐    ┌───────────────┐
│   Secret    │──► │ Flask Pod     │
│ SECRET_KEY  │    │ Flask App     │
└─────────────┘    │ LivenessProbe │
                   │ ReadinessProbe│
                   └──────┬────────┘
                          │
                          ▼
                    ┌──────────┐
                    │ Service  │
                    └──────────┘
```

---

# ConfigMap

## `configmap.yaml`

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: flask-config
data:
  APP_VERSION: "day7-k8s"
  APP_ENV: "production"
  LOG_LEVEL: "INFO"
  PORT: "5000"
```

---

# Secret

## `secret.yaml`

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: flask-secret
type: Opaque
data:
  SECRET_KEY: ZGV2b3BzLXNlY3JldC1rZXktMTIz
  DB_PASSWORD: c3VwZXJzZWNyZXRwYXNz
```

---

# Deployment

## `deployment.yaml`

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

          envFrom:
            - configMapRef:
                name: flask-config

            - secretRef:
                name: flask-secret

          livenessProbe:
            httpGet:
              path: /health
              port: 5000
            initialDelaySeconds: 10
            periodSeconds: 10

          readinessProbe:
            httpGet:
              path: /health
              port: 5000
            initialDelaySeconds: 5
            periodSeconds: 5
```

---

# Service

## `service.yaml`

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
    - protocol: TCP
      port: 80
      targetPort: 5000
      nodePort: 30080
```

---

# Apply Kubernetes Resources

## Apply ConfigMap

```bash
kubectl apply -f manifests/configmap.yaml
```

---

## Apply Secret

```bash
kubectl apply -f manifests/secret.yaml
```

---

## Apply Deployment

```bash
kubectl apply -f manifests/deployment.yaml
```

---

## Apply Service

```bash
kubectl apply -f manifests/service.yaml
```

---

# Verify Deployment

## Check Pods

```bash
kubectl get pods
```

---

## Check Service

```bash
kubectl get svc
```

---

## Describe Pod

```bash
kubectl describe pod <pod-name>
```

---

# Verify Environment Variables

```bash
kubectl exec -it <pod-name> -- env | grep APP
```

Expected output:

```text
APP_ENV=production
APP_VERSION=day7-k8s
```

---

# Verify Probes

```bash
kubectl describe pod <pod-name>
```

Expected section:

```text
Liveness:  http-get http://:5000/health
Readiness: http-get http://:5000/health
```

---

# Key Concepts Learned

## ConfigMap

Used for storing non-sensitive configuration values separately from application code.

Examples:

- APP_VERSION
- APP_ENV
- LOG_LEVEL

---

## Secret

Used for storing sensitive information securely.

Examples:

- Passwords
- API keys
- Tokens

---

## Liveness Probe

Checks whether the application is alive.

If the probe fails repeatedly:

- Kubernetes automatically restarts the container

---

## Readiness Probe

Checks whether the application is ready to receive traffic.

If readiness fails:

- Pod is temporarily removed from the Service

---

## Self-Healing

Kubernetes automatically replaces unhealthy containers using probes.

---

# Base64 Encoding

## Encode Secret

```bash
echo -n "mysecret" | base64
```

---

## Decode Secret

```bash
echo "bXlzZWNyZXQ=" | base64 --decode
```

---

# Useful Commands

## Watch Pods

```bash
kubectl get pods -w
```

---

## View Logs

```bash
kubectl logs <pod-name>
```

---

## Restart Deployment

```bash
kubectl rollout restart deployment flask-deployment
```

---

## Check Rollout Status

```bash
kubectl rollout status deployment flask-deployment
```

---

# Common Issues Fixed

| Problem | Fix |
|---|---|
| Wrong base64 secret value | Used `echo -n` |
| Probe failure causing restarts | Increased delay values |
| ConfigMap not loading | Applied ConfigMap before Deployment |
| Pod not receiving traffic | Fixed readiness probe |

---

# Final Outcome

By the end of Day 7:

- Configuration became externalized
- Secrets became securely managed
- Health checks were automated
- Kubernetes self-healing was implemented
- Production-grade deployment practices were achieved

---

# Next Step

## Day 8 — HPA Auto Scaling + Rolling Updates

Upcoming topics:

- Horizontal Pod Autoscaler
- CPU-based scaling
- Rolling deployments
- Zero downtime updates

---

# Author

Ashish Thakur

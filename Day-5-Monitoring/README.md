# Day 5 — Monitoring with Prometheus & Grafana

## Project Overview

This project demonstrates a complete monitoring and observability stack using Prometheus and Grafana for a Flask application running on AWS EC2 with Docker.

The Flask application exposes metrics through a `/metrics` endpoint, Prometheus collects the metrics, and Grafana visualizes them through dashboards.

---

# Project Structure

```bash
devops-project/
└── Day-5-Monitoring/
    ├── docker-compose.yml
    ├── prometheus.yml
    └── app/
        ├── app.py
        ├── Dockerfile
        ├── requirements.txt
        ├── conftest.py
        ├── setup.cfg
        └── tests/
            └── test_app.py
```

---

# What Was Built

The monitoring stack includes:

- Flask application with Prometheus metrics exporter
- Prometheus server for metrics collection
- Grafana dashboards for visualization
- Docker Compose orchestration
- Persistent volumes for Prometheus and Grafana data

---

# Architecture

```text
Flask App
(port 5000)
      │
      ▼
Prometheus
(port 9090)
      │
      ▼
Grafana
(port 3000)
```

---

# Services Running

| Service | Port |
|---|---|
| Flask App | 5000 |
| Prometheus | 9090 |
| Grafana | 3000 |

---

# Flask Application

## `app/app.py`

```python
from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics
import os

app = Flask(__name__)

metrics = PrometheusMetrics(app)

metrics.info(
    "app_info",
    "Application info",
    version=os.getenv("APP_VERSION", "1.0.0")
)

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
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

---

# Docker Compose Configuration

## `docker-compose.yml`

```yaml
version: "3.9"

services:

  app:
    build: ./app
    container_name: myapp
    ports:
      - "5000:5000"
    environment:
      - APP_VERSION=${APP_VERSION:-1.0.0}
    restart: always
    networks:
      - monitoring

  prometheus:
    image: prom/prometheus:v2.51.0
    container_name: prometheus
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
      - prometheus_data:/prometheus
    restart: always
    networks:
      - monitoring

  grafana:
    image: grafana/grafana:10.4.0
    container_name: grafana
    ports:
      - "3000:3000"
    environment:
      - GF_SECURITY_ADMIN_USER=admin
      - GF_SECURITY_ADMIN_PASSWORD=devops123
    volumes:
      - grafana_data:/var/lib/grafana
    restart: always
    depends_on:
      - prometheus
    networks:
      - monitoring

networks:
  monitoring:
    driver: bridge

volumes:
  prometheus_data:
  grafana_data:
```

---

# Prometheus Configuration

## `prometheus.yml`

```yaml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: "flask-app"
    static_configs:
      - targets: ["app:5000"]
    metrics_path: /metrics
```

---

# Start Monitoring Stack

## Build and Run Containers

```bash
docker compose up --build -d
```

---

# Verify Running Containers

```bash
docker ps
```

---

# Test Application

## Flask Health Endpoint

```bash
curl http://localhost:5000/health
```

## Metrics Endpoint

```bash
curl http://localhost:5000/metrics
```

---

# Access URLs

| Service | URL |
|---|---|
| Flask App | `http://EC2_PUBLIC_IP:5000` |
| Prometheus | `http://EC2_PUBLIC_IP:9090` |
| Grafana | `http://EC2_PUBLIC_IP:3000` |

---

# Grafana Login

| Username | Password |
|---|---|
| admin | devops123 |

---

# Key Concepts Learned

## Prometheus

Prometheus collects application metrics at regular intervals.

---

## Grafana

Grafana visualizes metrics using dashboards and graphs.

---

## Metrics Endpoint

The `/metrics` endpoint exposes:

- Request count
- Response latency
- Error rate
- CPU usage
- Memory usage

---

## Docker Networking

All services communicate internally using a shared Docker network.

---

# Useful Docker Commands

## View Logs

```bash
docker compose logs -f
```

## Restart Services

```bash
docker compose restart
```

## Stop Services

```bash
docker compose down
```

---

# Final Outcome

By the end of Day 5:

- Full monitoring stack was deployed
- Application metrics became observable
- Prometheus successfully scraped metrics
- Grafana dashboards visualized live data
- Monitoring workflow was fully operational

---

# Project Completion

This completes the 5-Day DevOps Hands-on Project Series.

Topics covered:

- Docker
- CI/CD
- Terraform
- AWS EC2
- Continuous Deployment
- Monitoring & Observability

---

# Author

Ashish Thakur

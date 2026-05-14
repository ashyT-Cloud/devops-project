# DevOps Flask Application with Docker & Docker Compose 🚀

A lightweight DevOps project demonstrating containerization of a Python Flask application using Docker and Docker Compose with Redis integration.

This project showcases:
- Multi-stage Docker builds
- Containerized Flask application
- Docker Compose orchestration
- Redis service integration
- Environment variable management
- Persistent Docker volumes
- Health endpoint implementation

---

# 📁 Project Structure

```bash
devops-project/
│
├── Dockerfile
├── docker-compose.yml
├── app.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Technologies Used

- Python 3.11
- Flask
- Redis
- Docker
- Docker Compose

---

# 📦 Application Features

✅ Flask REST API  
✅ Dockerized application  
✅ Multi-stage optimized Docker build  
✅ Redis container integration  
✅ Environment variable support  
✅ Health check endpoint  
✅ Persistent Redis storage using Docker volumes  
✅ Lightweight and production-friendly setup  

---

# 🐳 Dockerfile Highlights

The project uses a **multi-stage Docker build** for optimization:

### Stage 1 — Builder
- Installs Python dependencies
- Reduces unnecessary runtime packages

### Stage 2 — Runtime
- Copies only required dependencies
- Keeps image lightweight
- Runs Flask application securely

---

# 🚀 API Endpoints

## Home Endpoint

```bash
GET /
```

### Sample Response

```json
{
  "message": "Hello DevOps!",
  "version": "1.0.0"
}
```

---

## Health Check Endpoint

```bash
GET /health
```

### Sample Response

```json
{
  "status": "ok"
}
```

---

# 🔧 Setup & Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/ashyT-Cloud/devops-project.git
cd devops-project
```

---

# 🐳 Running with Docker

## Build Docker Image

```bash
docker build -t flask-devops-app .
```

## Run Container

```bash
docker run -d -p 5000:5000 flask-devops-app
```

---

# 🧩 Running with Docker Compose

## Start Services

```bash
docker compose up -d
```

## Check Running Containers

```bash
docker ps
```

## Stop Services

```bash
docker compose down
```

---

# 🌐 Access Application

Open in browser:

```bash
http://<server-ip>:5000
```

Health endpoint:

```bash
http://<server-ip>:5000/health
```

---

# 📜 Docker Compose Services

## Flask App Service
- Builds custom Docker image
- Exposes port `5000`
- Uses environment variables
- Depends on Redis service

## Redis Service
- Uses official Redis Alpine image
- Exposes port `6379`
- Stores persistent data using Docker volumes

---

# 📂 Environment Variables

| Variable | Description |
|----------|-------------|
| APP_VERSION | Application version |
| REDIS_URL | Redis connection URL |

---

# 📌 requirements.txt

```txt
flask==3.0.3
redis==5.0.4
```

---

# 🔍 Useful Docker Commands

## View Logs

```bash
docker compose logs -f
```

## Enter Running Container

```bash
docker exec -it <container_id> sh
```

## Remove Containers

```bash
docker compose down -v
```

---

# 🎯 Learning Outcomes

Through this project, I learned:

- Docker image creation
- Multi-stage Docker builds
- Docker Compose orchestration
- Container networking
- Volume management
- Flask container deployment
- Redis integration
- DevOps project structuring

---

# 👨‍💻 Author

## Ashish Thakur

Aspiring Cloud & DevOps Engineer passionate about:
- Docker
- Kubernetes
- AWS
- CI/CD
- Cloud Infrastructure

---

# ⭐ Future Improvements

- Add Nginx reverse proxy
- Implement CI/CD pipeline
- Add Kubernetes deployment manifests
- Add monitoring with Prometheus & Grafana
- Deploy on AWS EC2

---

# 📄 License

This project is open-source and available under the MIT License.


Day 2:
![CI](https://github.com/ashyT-Cloud/devops-project/actions/workflows/ci.yml/badge.svg)

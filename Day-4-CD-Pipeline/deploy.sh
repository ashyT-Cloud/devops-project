#!/bin/bash
set -e   # exit immediately if any command fails

echo "=== Starting deployment ==="

# Pull latest image from DockerHub
echo "Pulling latest image..."
docker pull $DOCKERHUB_USERNAME/myapp:latest

# Stop and remove old container if running
echo "Stopping old container..."
docker stop myapp 2>/dev/null || true
docker remove myapp 2>/dev/null || true

# Run new container
echo "Starting new container..."
docker run -d \
  --name myapp \
  --restart always \
  -p 5000:5000 \
  -e APP_VERSION=$APP_VERSION \
  $DOCKERHUB_USERNAME/myapp:latest

# Wait for app to start
echo "Waiting for app to start..."
sleep 5

# Smoke test - verify app is responding
echo "Running smoke test..."
curl -f htttp://localhost:5000/health || exit 1

echo "=== Deployment successful ==="

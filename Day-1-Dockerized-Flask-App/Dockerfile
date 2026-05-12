# --- Stage 1: build -------------------------------
FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --user -r requirements.txt

# --- Stage 2: runtime -----------------------------
FROM python:3.11-slim

WORKDIR /app

# Copy installed packages from builder, not from internet
COPY --from=builder /root/.local /root/.local

# Copy app code last (changes most often - keeps cache vaid)
COPY app.py .

ENV PATH=/root/.local/bin:$PATH
ENV APP_VERSION=1.0.0

EXPOSE 5000

CMD ["python", "app.py"]

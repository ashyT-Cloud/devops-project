# Day 2 — CI Pipeline with GitHub Actions

> Automated CI pipeline using GitHub Actions for linting, testing, and Docker image build/push.

---

# Project Overview

This project demonstrates a complete CI workflow using GitHub Actions.

Every push to the `main` branch automatically triggers:

- Code linting using **flake8**
- Code formatting validation using **black**
- Unit testing using **pytest**
- Docker image build and push to Docker Hub

The pipeline follows a dependency chain:

```text
Lint → Test → Docker Build
```

If one stage fails, the next stage will not run.

---

# Project Structure

```bash
Day-2-GitHubAction-CI/
├── .github/
│   └── workflows/
│       └── ci.yml
├── app.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── setup.cfg
├── conftest.py
└── tests/
    └── test_app.py
```

---

# CI Pipeline Workflow

```text
Push Code to GitHub
        │
        ▼
┌──────────────────┐
│ Lint Job         │
│ flake8 + black   │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Test Job         │
│ pytest           │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Docker Build Job │
│ Build + Push     │
└──────────────────┘
```

---

# GitHub Actions Workflow

## `.github/workflows/ci.yml`

```yaml
name: CI Pipeline

on:
  push:
    branches: [main]

jobs:

  lint:
    runs-on: ubuntu-latest

    defaults:
      run:
        working-directory: Day-2-GitHubAction-CI

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install lint tools
        run: pip install flake8 black

      - name: Run flake8
        run: flake8 app.py tests/

      - name: Run black check
        run: black --check app.py tests/

  test:
    runs-on: ubuntu-latest
    needs: lint

    defaults:
      run:
        working-directory: Day-2-GitHubAction-CI

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Run tests
        run: pytest tests/ -v

  docker-build:
    runs-on: ubuntu-latest
    needs: test

    steps:
      - uses: actions/checkout@v4

      - uses: docker/login-action@v3
        with:
          username: ${{ secrets.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}

      - uses: docker/build-push-action@v5
        with:
          context: Day-2-GitHubAction-CI
          push: true
          tags: username/myapp:latest
```

---

# Running Locally

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Tests

```bash
pytest tests/ -v
```

## Run flake8

```bash
flake8 app.py tests/
```

## Run black Check

```bash
black --check app.py tests/
```

## Auto Format Code

```bash
black app.py tests/
```

---

# GitHub Secrets Setup

Go to:

```text
GitHub Repository
→ Settings
→ Secrets and Variables
→ Actions
```

Add:

| Secret Name | Description |
|---|---|
| `DOCKERHUB_USERNAME` | Docker Hub username |
| `DOCKERHUB_TOKEN` | Docker Hub access token |

---

# Key Concepts Learned

## GitHub Actions

GitHub Actions automates tasks like testing, building, and deployment whenever code changes are pushed.

---

## `needs:` Dependency

```yaml
needs: lint
```

Ensures jobs run in sequence.

Example:

```text
lint must pass
→ then test runs
→ then docker build runs
```

---

## flake8

Checks coding style issues like:

- Unused imports
- Missing blank lines
- Long lines

---

## black

Automatically formats Python code to maintain consistent style.

---

## pytest

Framework used for automated unit testing.

---

# Problems Fixed During Setup

| Error | Fix |
|---|---|
| `.github` folder not detected | Moved to repository root |
| `test/ not found` | Corrected to `tests/` |
| `actions/chekout` typo | Fixed to `actions/checkout@v4` |
| flake8 line length errors | Added `setup.cfg` |
| `ModuleNotFoundError` | Added `conftest.py` |

---

# Outcome

By the end of Day 2:

- CI pipeline became fully automated
- Code quality checks were enforced
- Docker image builds became automatic
- GitHub Actions workflow was successfully integrated

---

# Next Step

## Day 3 — Terraform Infrastructure Automation

Upcoming topics:

- Terraform basics
- AWS EC2 provisioning
- Variables and outputs
- Infrastructure as Code (IaC)

---

*Part of the DevOps Hands-on Project Series.*

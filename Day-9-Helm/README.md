# DevOps Project — Day 9: Helm — Package and Version Your App

![Helm](https://img.shields.io/badge/Helm-v3.20.2-0F1689?style=flat&logo=helm&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-v1.30-326CE5?style=flat&logo=kubernetes&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0.3-000000?style=flat&logo=flask&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-25.x-2496ED?style=flat&logo=docker&logoColor=white)

> **Kubernetes Project** | Day 9 of 10 — Packaging the entire Flask K8s deployment into a Helm chart. One command to install, upgrade, rollback, or remove everything. Separate values files for staging and production environments.

---

## What Was Built

- **Helm chart** (`flask-chart`) packaging all K8s objects into one deployable unit
- **values.yaml** — default values for all configurable settings
- **values-staging.yaml** — staging overrides (1 replica, no HPA, debug logging)
- **values-prod.yaml** — production overrides (3 replicas, HPA up to 10, pinned image tag)
- **Templated manifests** — Deployment, Service, ConfigMap, Secret, HPA all use Go templates
- **`_helpers.tpl`** — reusable name and label helpers shared across all templates
- Successfully installed, upgraded, and rolled back using Helm commands

---

## How Day 9 Connects to Previous Days

```
Day 6  → Pod, Deployment, Service manifests (manual YAML)
Day 7  → ConfigMap, Secret, Probes added
Day 8  → HPA + Rolling Update Strategy added
Day 9  → ALL of the above packaged into one Helm chart
          helm install  = kubectl apply on all 5 files at once
          helm upgrade  = rolling update with one command
          helm rollback = instant revert with revision history
          helm uninstall = clean removal of everything
```

---

## Project Structure

```
devops-project/
└── Day-9-Helm/
    └── flask-chart/
        ├── Chart.yaml                  # chart metadata + version
        ├── values.yaml                 # default values (all environments)
        ├── values-staging.yaml         # staging overrides
        ├── values-prod.yaml            # production overrides
        └── templates/
            ├── _helpers.tpl            # reusable name + label helpers
            ├── deployment.yaml         # templated Deployment
            ├── service.yaml            # templated Service
            ├── configmap.yaml          # templated ConfigMap
            ├── secret.yaml             # templated Secret
            └── hpa.yaml                # conditional HPA
```

---

## Files — Complete Code

### `Chart.yaml`

```yaml
apiVersion: v2
name: flask-chart
description: A Helm chart for the Flask DevOps app
type: application
version: 1.0.0
appVersion: "1.0.0"
maintainers:
  - name: ashyT-Cloud
```

| Field | Purpose |
|-------|---------|
| `apiVersion: v2` | Helm 3 format (always v2 for new charts) |
| `version` | Chart version — increment when chart structure changes |
| `appVersion` | App version — informational, matches Docker image tag |
| `type: application` | Deploys workloads (vs `library` for shared templates) |

---

### `values.yaml`

```yaml
replicaCount: 2

image:
  repository: ashytcloud/myapp
  tag: latest
  pullPolicy: Always

service:
  type: NodePort
  port: 80
  targetPort: 5000
  nodePort: 30080

resources:
  requests:
    memory: "64Mi"
    cpu: "100m"
  limits:
    memory: "128Mi"
    cpu: "250m"

config:
  APP_VERSION: "1.0.0"
  APP_ENV: "production"
  LOG_LEVEL: "INFO"
  PORT: "5000"

secret:
  SECRET_KEY: ZGV2b3BzLXNlY3JldC1rZXktMTIz
  DB_PASSWORD: c3VwZXJzZWNyZXRwYXNz

autoscaling:
  enabled: true
  minReplicas: 2
  maxReplicas: 5
  targetCPUUtilizationPercentage: 50

livenessProbe:
  initialDelaySeconds: 10
  periodSeconds: 10
  failureThreshold: 3
  timeoutSeconds: 5

readinessProbe:
  initialDelaySeconds: 5
  periodSeconds: 5
  failureThreshold: 3
  timeoutSeconds: 3

strategy:
  maxSurge: 1
  maxUnavailable: 0
```

---

### `values-staging.yaml`

```yaml
replicaCount: 1

config:
  APP_VERSION: "staging"
  APP_ENV: "staging"
  LOG_LEVEL: "DEBUG"

autoscaling:
  enabled: false
  minReplicas: 1
  maxReplicas: 2
  targetCPUUtilizationPercentage: 70

resources:
  requests:
    memory: "32Mi"
    cpu: "50m"
  limits:
    memory: "64Mi"
    cpu: "100m"
```

---

### `values-prod.yaml`

```yaml
replicaCount: 3

image:
  tag: "1.0.0"

config:
  APP_VERSION: "1.0.0"
  APP_ENV: "production"
  LOG_LEVEL: "WARNING"

autoscaling:
  enabled: true
  minReplicas: 3
  maxReplicas: 10
  targetCPUUtilizationPercentage: 50

resources:
  requests:
    memory: "128Mi"
    cpu: "200m"
  limits:
    memory: "256Mi"
    cpu: "500m"
```

**Staging vs Production comparison:**

| Setting | Staging | Production |
|---------|---------|-----------|
| Replicas | 1 | 3 |
| HPA | Disabled | Enabled (max 10) |
| Log level | DEBUG | WARNING |
| Image tag | latest | 1.0.0 (pinned) |
| CPU request | 50m | 200m |
| Memory limit | 64Mi | 256Mi |

---

### `templates/_helpers.tpl`

```yaml
{{- define "flask-chart.name" -}}
{{- .Chart.Name | trunc 63 | trimSuffix "-" }}
{{- end }}

{{- define "flask-chart.fullname" -}}
{{- printf "%s-%s" .Release.Name .Chart.Name | trunc 63 | trimSuffix "-" }}
{{- end }}

{{- define "flask-chart.labels" -}}
helm.sh/chart: {{ .Chart.Name }}-{{ .Chart.Version }}
app.kubernetes.io/name: {{ include "flask-chart.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}

{{- define "flask-chart.selectorLabels" -}}
app.kubernetes.io/name: {{ include "flask-chart.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}
```

**Why `_helpers.tpl`:**
- Files starting with `_` are never rendered as K8s manifests
- Define once, reuse across all templates with `{{ include "flask-chart.fullname" . }}`
- Ensures naming is consistent — change the release name once, all objects update

---

### `templates/deployment.yaml`

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include "flask-chart.fullname" . }}
  labels:
    {{- include "flask-chart.labels" . | nindent 4 }}
spec:
  {{- if not .Values.autoscaling.enabled }}
  replicas: {{ .Values.replicaCount }}
  {{- end }}
  selector:
    matchLabels:
      {{- include "flask-chart.selectorLabels" . | nindent 6 }}
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: {{ .Values.strategy.maxSurge }}
      maxUnavailable: {{ .Values.strategy.maxUnavailable }}
  template:
    metadata:
      labels:
        {{- include "flask-chart.selectorLabels" . | nindent 8 }}
    spec:
      containers:
        - name: {{ .Chart.Name }}
          image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
          imagePullPolicy: {{ .Values.image.pullPolicy }}
          ports:
            - containerPort: {{ .Values.service.targetPort }}
          envFrom:
            - configMapRef:
                name: {{ include "flask-chart.fullname" . }}-config
            - secretRef:
                name: {{ include "flask-chart.fullname" . }}-secret
          resources:
            {{- toYaml .Values.resources | nindent 12 }}
          livenessProbe:
            httpGet:
              path: /health
              port: {{ .Values.service.targetPort }}
            initialDelaySeconds: {{ .Values.livenessProbe.initialDelaySeconds }}
            periodSeconds: {{ .Values.livenessProbe.periodSeconds }}
            failureThreshold: {{ .Values.livenessProbe.failureThreshold }}
            timeoutSeconds: {{ .Values.livenessProbe.timeoutSeconds }}
          readinessProbe:
            httpGet:
              path: /health
              port: {{ .Values.service.targetPort }}
            initialDelaySeconds: {{ .Values.readinessProbe.initialDelaySeconds }}
            periodSeconds: {{ .Values.readinessProbe.periodSeconds }}
            failureThreshold: {{ .Values.readinessProbe.failureThreshold }}
            timeoutSeconds: {{ .Values.readinessProbe.timeoutSeconds }}
```

**Key template syntax:**

| Syntax | What it does |
|--------|-------------|
| `{{ include "flask-chart.fullname" . }}` | Call helper function with current context |
| `{{- include ... \| nindent 4 }}` | Include + indent 4 spaces + trim whitespace |
| `{{- if not .Values.autoscaling.enabled }}` | Conditional block |
| `{{- toYaml .Values.resources \| nindent 12 }}` | Convert map to YAML, indent 12 spaces |
| `.Values.image.repository` | Navigate nested values |
| `.Release.Name` | The helm install name (e.g. `myapp`) |
| `.Chart.Name` | Chart name from Chart.yaml |

---

### `templates/service.yaml`

```yaml
apiVersion: v1
kind: Service
metadata:
  name: {{ include "flask-chart.fullname" . }}
  labels:
    {{- include "flask-chart.labels" . | nindent 4 }}
spec:
  type: {{ .Values.service.type }}
  selector:
    {{- include "flask-chart.selectorLabels" . | nindent 4 }}
  ports:
    - protocol: TCP
      port: {{ .Values.service.port }}
      targetPort: {{ .Values.service.targetPort }}
      nodePort: {{ .Values.service.nodePort }}
```

---

### `templates/configmap.yaml`

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: {{ include "flask-chart.fullname" . }}-config
  labels:
    {{- include "flask-chart.labels" . | nindent 4 }}
data:
  {{- range $key, $val := .Values.config }}
  {{ $key }}: {{ $val | quote }}
  {{- end }}
```

`{{- range $key, $val := .Values.config }}` — loops over every key in `values.yaml config:`. Add a new config key to values.yaml and it automatically appears in the ConfigMap — no template change needed.

---

### `templates/secret.yaml`

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: {{ include "flask-chart.fullname" . }}-secret
  labels:
    {{- include "flask-chart.labels" . | nindent 4 }}
type: Opaque
data:
  {{- range $key, $val := .Values.secret }}
  {{ $key }}: {{ $val | quote }}
  {{- end }}
```

---

### `templates/hpa.yaml`

```yaml
{{- if .Values.autoscaling.enabled }}
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: {{ include "flask-chart.fullname" . }}
  labels:
    {{- include "flask-chart.labels" . | nindent 4 }}
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: {{ include "flask-chart.fullname" . }}
  minReplicas: {{ .Values.autoscaling.minReplicas }}
  maxReplicas: {{ .Values.autoscaling.maxReplicas }}
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: {{ .Values.autoscaling.targetCPUUtilizationPercentage }}
{{- end }}
```

`{{- if .Values.autoscaling.enabled }}` — entire HPA file is conditional. Set `false` in staging = no HPA object created at all. No commented-out YAML, no manual deletion needed.

---

## Helm Commands — Full Reference

```bash
# Validate chart
helm lint ./flask-chart

# Preview rendered YAML (no install)
helm template myapp ./flask-chart
helm template myapp ./flask-chart -f flask-chart/values-prod.yaml

# Dry run
helm install myapp ./flask-chart --dry-run --debug

# Install
helm install myapp ./flask-chart
helm install myapp-staging ./flask-chart -f flask-chart/values-staging.yaml -n staging --create-namespace
helm install myapp-prod ./flask-chart -f flask-chart/values-prod.yaml -n production --create-namespace

# Upgrade
helm upgrade myapp ./flask-chart
helm upgrade myapp ./flask-chart --set image.tag=v2.0.0
helm upgrade myapp ./flask-chart --set config.APP_VERSION=2.0.0

# Upgrade or install (best for CI/CD)
helm upgrade --install myapp ./flask-chart

# Inspect
helm list
helm list -A                    # all namespaces
helm status myapp
helm history myapp
helm get values myapp           # values used in current release

# Rollback
helm rollback myapp 1           # rollback to revision 1
helm history myapp              # verify revision

# Uninstall
helm uninstall myapp
```

---

## Deploy to Multiple Environments

```bash
# Staging namespace
helm install myapp-staging ./flask-chart \
  -f flask-chart/values-staging.yaml \
  --namespace staging \
  --create-namespace

# Production namespace
helm install myapp-prod ./flask-chart \
  -f flask-chart/values-prod.yaml \
  --namespace production \
  --create-namespace

# List all releases
helm list -A
# NAME           NAMESPACE   REVISION  STATUS    CHART
# myapp-staging  staging     1         deployed  flask-chart-1.0.0
# myapp-prod     production  1         deployed  flask-chart-1.0.0
```

---

## Key Concepts

### Why Helm over raw YAML

| Feature | Raw YAML | Helm |
|---------|---------|------|
| Variables | No | Yes — `{{ .Values.x }}` |
| Conditionals | No | Yes — `{{- if .Values.x }}` |
| Loops | No | Yes — `{{- range }}` |
| Install as unit | No — file by file | Yes — one command |
| Upgrade tracking | No | Yes — revision history |
| Rollback | Manual | `helm rollback myapp 1` |
| Remove all objects | Manual | `helm uninstall myapp` |

### values.yaml override chain

```
Chart defaults (values.yaml)
    ↓ overridden by
-f values-staging.yaml
    ↓ overridden by
--set image.tag=v2.0.0   ← highest priority
```

### Release vs Chart

| Term | Meaning | Example |
|------|---------|---------|
| Chart | The package (template + defaults) | `flask-chart` |
| Release | A named instance of a chart | `myapp`, `myapp-staging` |
| Revision | A version of a release | 1, 2, 3... |

Install the same chart twice with different names = two completely independent apps.

### Always pin image tags in production

```yaml
# BAD — values-prod.yaml
image:
  tag: latest        # unpredictable — new push can break production

# GOOD — values-prod.yaml
image:
  tag: "1.0.0"       # predictable — you control when to upgrade
```

---

## Errors Fixed During Setup

| Error | Cause | Fix |
|-------|-------|-----|
| `nil pointer evaluating interface {}.initialDelaySeconds` | `readinessProbe` block missing from values.yaml | Added livenessProbe + readinessProbe + strategy to values.yaml |
| `cannot re-use a name that is still in use` | Previous failed install left release | `helm uninstall myapp` then reinstall |
| `spec.ports[0].port: Invalid value: 0` | `service.port` missing from values.yaml | Added full service block to values.yaml |

---

## 10-Day Kubernetes Roadmap

| Day | Topic | Status |
|-----|-------|--------|
| Day 6 | K8s core concepts – Pod, Deployment, Service | ✅ Done |
| Day 7 | ConfigMaps, Secrets, liveness + readiness probes | ✅ Done |
| Day 8 | HPA auto-scaling + rolling deploys | ✅ Done |
| Day 9 | Helm — package and version your app | ✅ Done |
| Day 10 | Deploy to AWS EKS — real cloud cluster | Upcoming |

---

*Extension of the 5-day DevOps project — packaging Kubernetes deployments with Helm for professional multi-environment management.*

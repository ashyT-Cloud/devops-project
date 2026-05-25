## Real Issue Faced During Implementation

During setup, HPA initially showed:

```bash
cpu: <unknown>/50%
```

### Root Cause

After debugging with:

```bash
kubectl describe hpa flask-hpa
```

the issue was identified as:

```text
missing request for cpu in container flask of Pod flask-pod
```

A standalone pod (`flask-pod`) created during earlier testing did not have CPU resource requests configured.

Since HPA calculates CPU utilization using `requests.cpu`, Kubernetes could not compute utilization.

### Fix

Removed the old pod:

```bash
kubectl delete pod flask-pod
```

After cleanup:

```bash
kubectl get hpa
```

Output:

```bash
cpu: 1%/50%
```

### Lesson Learned

For HPA to work:

- Metrics Server must be installed
- `resources.requests.cpu` must exist in Deployment
- Extra test pods without CPU requests can interfere with scaling metrics

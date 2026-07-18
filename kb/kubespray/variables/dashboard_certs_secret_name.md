---
id: VARIABLE-DASHBOARD_CERTS_SECRET_NAME
type: variable
title: dashboard_certs_secret_name
status: active
kubespray_version: ">=v2.27.0 <=v2.30.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - dashboard_certs_secret_name
tags:
  - kubernetes-apps
  - ansible
  - variable
sources:
  - type: code
    path: roles/kubernetes-apps/ansible/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.30.0/roles/kubernetes-apps/ansible/defaults/main.yml
    note: "default: kubernetes-dashboard-certs"
relations: []
---
<!-- generated: variable-stub -->

# dashboard_certs_secret_name

## Summary

Kubespray variable `dashboard_certs_secret_name` — default `kubernetes-dashboard-certs`. Defined in `roles/kubernetes-apps/ansible/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.30.0` of the indexed range. **Removed after `v2.30.0`** (absent in later tags of the range). (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubernetes-apps/ansible/defaults/main.yml` (Kubespray `v2.30.0`):

```yaml
dashboard_certs_secret_name: kubernetes-dashboard-certs
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.30.0`. **Removed after `v2.30.0`** (absent in later tags of the range). Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubernetes-apps/ansible/defaults/main.yml` (Kubespray `v2.30.0`).

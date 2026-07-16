---
id: VARIABLE-AUTHORIZATION_MODES
type: variable
title: authorization_modes
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - authorization_modes
tags:
  - apiserver
  - authorization
  - rbac
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "API server authorization modes; default ['Node', 'RBAC']"
relations: []
---

# authorization_modes

## Summary
List of authorization modes enabled on the Kubernetes API server (`--authorization-mode`). Default is `['Node', 'RBAC']`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml`:
```yaml
authorization_modes: ['Node', 'RBAC']
```
The default value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (only the line number varies). The hardening docs and test fixtures reference the same `['Node', 'RBAC']` value.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Controls API server authorization configuration.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.

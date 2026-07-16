---
id: VARIABLE-KUBERNETES_AUDIT_WEBHOOK
type: variable
title: kubernetes_audit_webhook
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubernetes_audit_webhook
tags:
  - apiserver
  - audit
  - security
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "Enables apiserver audit webhook support; default false"
relations: []
---

# kubernetes_audit_webhook

## Summary
Boolean toggle that enables kube-apiserver audit webhook support. Default is `false`. When enabled, the associated `audit_webhook_*` variables (config file, server URL, mode, batch settings) configure the webhook backend.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/main.yml`:

```yaml
kubernetes_audit_webhook: false
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line 80 in v2.29.0/v2.29.1, line 83 in v2.30.0/v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related to `audit_webhook_config_file`, `audit_webhook_server_url`, `audit_webhook_mode`, and other `audit_webhook_*` variables.

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.

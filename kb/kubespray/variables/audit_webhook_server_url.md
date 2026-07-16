---
id: VARIABLE-AUDIT_WEBHOOK_SERVER_URL
type: variable
title: audit_webhook_server_url
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - audit_webhook_server_url
tags:
  - audit
  - webhook
  - control-plane
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "URL of the remote audit webhook backend, default https://audit.app"
relations: []
---

# audit_webhook_server_url

## Summary
URL of the remote audit webhook backend that receives Kubernetes audit events. Default: `https://audit.app` (a placeholder value expected to be overridden by the user).

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/main.yml` as:

```yaml
audit_webhook_server_url: "https://audit.app"
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Effective only when audit webhook support is enabled (`kubernetes_audit_webhook: true`). Related variables: `audit_webhook_config_file`, `audit_webhook_server_extra_args`.

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.

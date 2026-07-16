---
id: VARIABLE-AUDIT_WEBHOOK_MODE
type: variable
title: audit_webhook_mode
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - audit_webhook_mode
tags:
  - audit
  - webhook
  - control-plane
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "Audit webhook delivery mode, default batch"
relations: []
---

# audit_webhook_mode

## Summary
Delivery strategy for sending audit events to the webhook backend (maps to the API server `--audit-webhook-mode` flag), e.g. `batch` or `blocking`. Default: `batch`.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/main.yml` as:

```yaml
audit_webhook_mode: batch
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Effective only when audit webhook support is enabled (`kubernetes_audit_webhook: true`). The `audit_webhook_batch_max_size` and `audit_webhook_batch_max_wait` settings apply when mode is `batch`.

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.

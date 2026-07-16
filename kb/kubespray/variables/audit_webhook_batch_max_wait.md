---
id: VARIABLE-AUDIT_WEBHOOK_BATCH_MAX_WAIT
type: variable
title: audit_webhook_batch_max_wait
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - audit_webhook_batch_max_wait
tags:
  - audit
  - webhook
  - control-plane
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "Max wait time before flushing an audit webhook batch, default 1s"
relations: []
---

# audit_webhook_batch_max_wait

## Summary
Maximum time to wait before forcing a flush of the buffered audit events to the webhook backend (maps to the API server `--audit-webhook-batch-max-wait` flag). Default: `1s`.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/main.yml` as:

```yaml
audit_webhook_batch_max_wait: 1s
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Effective only when audit webhook support is enabled (`kubernetes_audit_webhook: true`). Related variables: `audit_webhook_mode`, `audit_webhook_batch_max_size`.

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.

---
id: VARIABLE-AUDIT_WEBHOOK_CONFIG_FILE
type: variable
title: audit_webhook_config_file
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - audit_webhook_config_file
tags:
  - audit
  - webhook
  - control-plane
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "Path to the audit webhook kubeconfig file"
relations: []
---

# audit_webhook_config_file

## Summary
Filesystem path to the audit webhook backend kubeconfig file used by the API server (maps to `--audit-webhook-config-file`). Default: `{{ kube_config_dir }}/audit-policy/apiserver-audit-webhook-config.yaml`.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/main.yml` as:

```yaml
audit_webhook_config_file: "{{ kube_config_dir }}/audit-policy/apiserver-audit-webhook-config.yaml"
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Effective only when audit webhook support is enabled (`kubernetes_audit_webhook: true`). Related variables: `audit_webhook_server_url`, `audit_webhook_mode`.

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.

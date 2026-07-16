---
id: VARIABLE-AUDIT_LOG_MAXBACKUPS
type: variable
title: audit_log_maxbackups
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - audit_log_maxbackups
tags:
  - audit
  - apiserver
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "Maximum number of retained audit log files (apiserver --audit-log-maxbackup); default 10."
relations: []
---

# audit_log_maxbackups

## Summary
Maximum number of old audit log files to retain, passed to the kube-apiserver `--audit-log-maxbackup` flag. Default is `10`. Applies when API server auditing (`kubernetes_audit`) is enabled.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/main.yml` as `audit_log_maxbackups: 10`. The default value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related audit-log rotation variables: `audit_log_maxage`, `audit_log_maxsize`, `audit_log_path`; gated by `kubernetes_audit`.

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.

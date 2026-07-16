---
id: VARIABLE-AUDIT_LOG_PATH
type: variable
title: audit_log_path
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - audit_log_path
tags:
  - audit
  - apiserver
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "Audit log file path passed to apiserver --audit-log-path; default /var/log/audit/kube-apiserver-audit.log."
relations: []
---

# audit_log_path

## Summary
Full path of the audit log file written by the kube-apiserver, passed to its `--audit-log-path` flag. Default is `/var/log/audit/kube-apiserver-audit.log`. Its directory component also drives `audit_log_mountpath`. Applies when API server auditing (`kubernetes_audit`) is enabled.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/main.yml` as `audit_log_path: /var/log/audit/kube-apiserver-audit.log`. The default value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Referenced by `audit_log_mountpath` (`audit_log_path | dirname`); related variables: `audit_log_hostpath`, `audit_log_name`, `audit_log_maxage/maxbackups/maxsize`; gated by `kubernetes_audit`.

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.

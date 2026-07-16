---
id: VARIABLE-AUDIT_LOG_HOSTPATH
type: variable
title: audit_log_hostpath
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - audit_log_hostpath
tags:
  - audit
  - apiserver
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "Host directory mounted into the apiserver for audit logs; default /var/log/kubernetes/audit."
relations: []
---

# audit_log_hostpath

## Summary
Host-node directory that is mounted into the kube-apiserver static pod to store audit log files. Default is `/var/log/kubernetes/audit`. Applies when API server auditing (`kubernetes_audit`) is enabled.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/main.yml` as `audit_log_hostpath: /var/log/kubernetes/audit`. The default value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related audit-log variables: `audit_log_path`, `audit_log_name`, `audit_log_mountpath`, `audit_log_maxage`, `audit_log_maxbackups`, `audit_log_maxsize`; gated by `kubernetes_audit`.

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.

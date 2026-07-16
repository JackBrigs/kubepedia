---
id: VARIABLE-AUDIT_LOG_MOUNTPATH
type: variable
title: audit_log_mountpath
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - audit_log_mountpath
tags:
  - audit
  - apiserver
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "In-container mount path for the audit log volume; computed as audit_log_path | dirname."
relations: []
---

# audit_log_mountpath

## Summary
Path inside the kube-apiserver container where the audit log volume is mounted. It is computed from `audit_log_path` by taking its directory component, so it defaults to the directory portion of `/var/log/audit/kube-apiserver-audit.log` (i.e. `/var/log/audit`). Applies when API server auditing (`kubernetes_audit`) is enabled.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/main.yml` as `audit_log_mountpath: "{{ audit_log_path | dirname }}"`. The computed expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Depends on `audit_log_path`; related variables: `audit_log_hostpath`, `audit_log_name`; gated by `kubernetes_audit`.

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.

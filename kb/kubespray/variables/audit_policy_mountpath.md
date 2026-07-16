---
id: VARIABLE-AUDIT_POLICY_MOUNTPATH
type: variable
title: audit_policy_mountpath
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - audit_policy_mountpath
tags:
  - audit
  - apiserver
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "In-container mount path for the audit policy volume; computed as audit_policy_hostpath."
relations: []
---

# audit_policy_mountpath

## Summary
Path inside the kube-apiserver container where the audit policy directory is mounted. It is set equal to `audit_policy_hostpath`, so host and container paths for the audit policy match. Applies when API server auditing (`kubernetes_audit`) is enabled.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/main.yml` as `audit_policy_mountpath: "{{ audit_policy_hostpath }}"`. The computed expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Depends on `audit_policy_hostpath` (itself derived from `audit_policy_file`); gated by `kubernetes_audit`.

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.

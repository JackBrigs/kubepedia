---
id: VARIABLE-AUDIT_POLICY_HOSTPATH
type: variable
title: audit_policy_hostpath
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - audit_policy_hostpath
tags:
  - audit
  - apiserver
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "Host directory holding the audit policy file; computed as audit_policy_file | dirname."
relations: []
---

# audit_policy_hostpath

## Summary
Host-node directory that contains the audit policy file and is mounted into the kube-apiserver static pod. Computed from `audit_policy_file` by taking its directory component. Also serves as the value for `audit_policy_mountpath`. Applies when API server auditing (`kubernetes_audit`) is enabled.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/main.yml` as `audit_policy_hostpath: "{{ audit_policy_file | dirname }}"`. The computed expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Depends on `audit_policy_file`; referenced by `audit_policy_mountpath` (set equal to it); gated by `kubernetes_audit`.

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.

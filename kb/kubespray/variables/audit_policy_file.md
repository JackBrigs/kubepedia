---
id: VARIABLE-AUDIT_POLICY_FILE
type: variable
title: audit_policy_file
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - audit_policy_file
tags:
  - audit
  - apiserver
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "Path to the audit policy YAML (apiserver --audit-policy-file); computed from kube_config_dir."
relations: []
---

# audit_policy_file

## Summary
Path to the audit policy YAML file that the kube-apiserver loads via `--audit-policy-file`. Computed from `kube_config_dir` as `{{ kube_config_dir }}/audit-policy/apiserver-audit-policy.yaml`. Its directory component drives `audit_policy_hostpath`. Applies when API server auditing (`kubernetes_audit`) is enabled.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/main.yml` as `audit_policy_file: "{{ kube_config_dir }}/audit-policy/apiserver-audit-policy.yaml"`. The computed expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Depends on `kube_config_dir`; referenced by `audit_policy_hostpath` (`audit_policy_file | dirname`); gated by `kubernetes_audit`.

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.

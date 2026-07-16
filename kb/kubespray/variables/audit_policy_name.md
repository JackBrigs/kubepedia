---
id: VARIABLE-AUDIT_POLICY_NAME
type: variable
title: audit_policy_name
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - audit_policy_name
tags:
  - audit
  - control-plane
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "Defines the audit policy name, default audit-policy"
relations: []
---

# audit_policy_name

## Summary
Sets the name used for the Kubernetes API server audit policy (used for the ConfigMap / hostpath naming). Default: `audit-policy`.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/main.yml` as:

```yaml
audit_policy_name: audit-policy
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0. Related keys in the same block include `audit_policy_hostpath: "{{ audit_policy_file | dirname }}"` and `audit_policy_mountpath: "{{ audit_policy_hostpath }}"`.

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Related variables: `audit_policy_hostpath`, `audit_policy_mountpath`, `kubernetes_audit`.

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.

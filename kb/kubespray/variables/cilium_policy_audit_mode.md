---
id: VARIABLE-CILIUM_POLICY_AUDIT_MODE
type: variable
title: cilium_policy_audit_mode
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_policy_audit_mode
tags:
  - cilium
  - policy
  - security
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "Defines cilium_policy_audit_mode, default false"
relations:
  - type: see_also
    target: COMPONENT-CILIUM
---

# cilium_policy_audit_mode

## Summary
Enables Cilium policy audit mode. When `true`, network policies are evaluated but not enforced (violations are logged instead of dropped). Default is `false`, so policies are enforced normally.

## Implementation
Defined in `roles/network_plugin/cilium/defaults/main.yml` as:

```yaml
cilium_policy_audit_mode: false
```

The default value `false` is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (only the line number shifts between tags).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Applies only when `kube_network_plugin: cilium`. Useful for validating policy sets before enforcing them.

## References
- roles/network_plugin/cilium/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.

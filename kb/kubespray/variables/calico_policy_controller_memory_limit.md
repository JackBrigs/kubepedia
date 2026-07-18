---
id: VARIABLE-CALICO_POLICY_CONTROLLER_MEMORY_LIMIT
type: variable
title: calico_policy_controller_memory_limit
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - calico_policy_controller_memory_limit
tags:
  - kubernetes-apps
  - policy-controller
  - variable
sources:
  - type: code
    path: roles/kubernetes-apps/policy_controller/calico/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/policy_controller/calico/defaults/main.yml
    note: "default: 256M"
relations: []
---
<!-- generated: variable-stub -->

# calico_policy_controller_memory_limit

## Summary

Kubespray variable `calico_policy_controller_memory_limit` — default `256M`. Defined in `roles/kubernetes-apps/policy_controller/calico/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubernetes-apps/policy_controller/calico/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
calico_policy_controller_memory_limit: 256M
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubernetes-apps/policy_controller/calico/defaults/main.yml` (Kubespray `v2.31.0`).

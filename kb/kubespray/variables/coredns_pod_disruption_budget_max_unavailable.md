---
id: VARIABLE-COREDNS_POD_DISRUPTION_BUDGET_MAX_UNAVAILABLE
type: variable
title: coredns_pod_disruption_budget_max_unavailable
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - coredns_pod_disruption_budget_max_unavailable
tags:
  - kubernetes-apps
  - ansible
  - variable
sources:
  - type: code
    path: roles/kubernetes-apps/ansible/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/ansible/defaults/main.yml
    note: "default: 30%"
relations: []
---
<!-- generated: variable-stub -->

# coredns_pod_disruption_budget_max_unavailable

## Summary

Kubespray variable `coredns_pod_disruption_budget_max_unavailable` — default `30%`. Defined in `roles/kubernetes-apps/ansible/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubernetes-apps/ansible/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
coredns_pod_disruption_budget_max_unavailable: 30%
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubernetes-apps/ansible/defaults/main.yml` (Kubespray `v2.31.0`).

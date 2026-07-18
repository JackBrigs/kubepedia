---
id: VARIABLE-DNS_AUTOSCALER_AFFINITY
type: variable
title: dns_autoscaler_affinity
status: active
kubespray_version: ">=v2.28.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - dns_autoscaler_affinity
tags:
  - kubernetes-apps
  - ansible
  - variable
sources:
  - type: code
    path: roles/kubernetes-apps/ansible/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/ansible/defaults/main.yml
    note: "default: {}"
relations: []
---
<!-- generated: variable-stub -->

# dns_autoscaler_affinity

## Summary

Kubespray variable `dns_autoscaler_affinity` — default `{}`. Defined in `roles/kubernetes-apps/ansible/defaults/main.yml`. Present in Kubespray
`v2.28.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubernetes-apps/ansible/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
dns_autoscaler_affinity: {}
```

## Compatibility

Present in the Kubespray tags `v2.28.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubernetes-apps/ansible/defaults/main.yml` (Kubespray `v2.31.0`).

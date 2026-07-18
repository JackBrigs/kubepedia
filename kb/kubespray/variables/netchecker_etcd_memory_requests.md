---
id: VARIABLE-NETCHECKER_ETCD_MEMORY_REQUESTS
type: variable
title: netchecker_etcd_memory_requests
status: active
kubespray_version: ">=v2.27.0 <=v2.30.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - netchecker_etcd_memory_requests
tags:
  - kubernetes-apps
  - ansible
  - variable
sources:
  - type: code
    path: roles/kubernetes-apps/ansible/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.30.0/roles/kubernetes-apps/ansible/defaults/main.yml
    note: "default: 128M"
relations: []
---
<!-- generated: variable-stub -->

# netchecker_etcd_memory_requests

## Summary

Kubespray variable `netchecker_etcd_memory_requests` — default `128M`. Defined in `roles/kubernetes-apps/ansible/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.30.0` of the indexed range. **Removed after `v2.30.0`** (absent in later tags of the range). (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubernetes-apps/ansible/defaults/main.yml` (Kubespray `v2.30.0`):

```yaml
netchecker_etcd_memory_requests: 128M
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.30.0`. **Removed after `v2.30.0`** (absent in later tags of the range). Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubernetes-apps/ansible/defaults/main.yml` (Kubespray `v2.30.0`).

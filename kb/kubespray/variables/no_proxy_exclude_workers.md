---
id: VARIABLE-NO_PROXY_EXCLUDE_WORKERS
type: variable
title: no_proxy_exclude_workers
status: active
kubespray_version: ">=v2.31.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - no_proxy_exclude_workers
tags:
  - network-facts
  - variable
sources:
  - type: code
    path: roles/network_facts/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_facts/defaults/main.yml
    note: "default: false"
relations: []
---
<!-- generated: variable-stub -->

# no_proxy_exclude_workers

## Summary

Kubespray variable `no_proxy_exclude_workers` — default `false`. Defined in `roles/network_facts/defaults/main.yml`. Present in Kubespray
`v2.31.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/network_facts/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
no_proxy_exclude_workers: false
```

## Compatibility

Present in the Kubespray tags `v2.31.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/network_facts/defaults/main.yml` (Kubespray `v2.31.0`).

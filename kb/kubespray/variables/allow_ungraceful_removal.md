---
id: VARIABLE-ALLOW_UNGRACEFUL_REMOVAL
type: variable
title: allow_ungraceful_removal
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - allow_ungraceful_removal
tags:
  - remove-node
  - pre-remove
  - variable
sources:
  - type: code
    path: roles/remove_node/pre_remove/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/remove_node/pre_remove/defaults/main.yml
    note: "default: false"
relations: []
---
<!-- generated: variable-stub -->

# allow_ungraceful_removal

## Summary

Kubespray variable `allow_ungraceful_removal` — default `false`. Defined in `roles/remove_node/pre_remove/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/remove_node/pre_remove/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
allow_ungraceful_removal: false
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/remove_node/pre_remove/defaults/main.yml` (Kubespray `v2.31.0`).

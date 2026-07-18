---
id: VARIABLE-DELETE_NODE_DELAY_SECONDS
type: variable
title: delete_node_delay_seconds
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - delete_node_delay_seconds
tags:
  - remove-node
  - post-remove
  - variable
sources:
  - type: code
    path: roles/remove-node/post-remove/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/remove-node/post-remove/defaults/main.yml
    note: "default: 3"
relations: []
---
<!-- generated: variable-stub -->

# delete_node_delay_seconds

## Summary

Kubespray variable `delete_node_delay_seconds` — default `3`. Defined in `roles/remove-node/post-remove/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/remove-node/post-remove/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
delete_node_delay_seconds: 3
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/remove-node/post-remove/defaults/main.yml` (Kubespray `v2.31.0`).

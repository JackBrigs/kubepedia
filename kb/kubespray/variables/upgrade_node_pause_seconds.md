---
id: VARIABLE-UPGRADE_NODE_PAUSE_SECONDS
type: variable
title: upgrade_node_pause_seconds
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - upgrade_node_pause_seconds
tags:
  - upgrade
  - pre-upgrade
  - variable
sources:
  - type: code
    path: roles/upgrade/pre-upgrade/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/upgrade/pre-upgrade/defaults/main.yml
    note: "default: 0"
relations: []
---
<!-- generated: variable-stub -->

# upgrade_node_pause_seconds

## Summary

Kubespray variable `upgrade_node_pause_seconds` — default `0`. Defined in `roles/upgrade/pre-upgrade/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/upgrade/pre-upgrade/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
upgrade_node_pause_seconds: 0
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/upgrade/pre-upgrade/defaults/main.yml` (Kubespray `v2.31.0`).

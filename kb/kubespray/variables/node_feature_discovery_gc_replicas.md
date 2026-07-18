---
id: VARIABLE-NODE_FEATURE_DISCOVERY_GC_REPLICAS
type: variable
title: node_feature_discovery_gc_replicas
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - node_feature_discovery_gc_replicas
tags:
  - kubernetes-apps
  - node-feature-discovery
  - variable
sources:
  - type: code
    path: roles/kubernetes-apps/node_feature_discovery/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/node_feature_discovery/defaults/main.yml
    note: "default: 1"
relations: []
---
<!-- generated: variable-stub -->

# node_feature_discovery_gc_replicas

## Summary

Kubespray variable `node_feature_discovery_gc_replicas` — default `1`. Defined in `roles/kubernetes-apps/node_feature_discovery/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubernetes-apps/node_feature_discovery/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
node_feature_discovery_gc_replicas: 1
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubernetes-apps/node_feature_discovery/defaults/main.yml` (Kubespray `v2.31.0`).

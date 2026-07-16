---
id: VARIABLE-CILIUM_CLUSTER_ID
type: variable
title: cilium_cluster_id
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_cluster_id
tags:
  - cilium
  - cni
  - clustermesh
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "Cilium ClusterMesh unique cluster ID; default 0"
relations:
  - type: see_also
    target: COMPONENT-CILIUM
---

# cilium_cluster_id

## Summary
Numeric identifier for the Cilium cluster, used by Cilium ClusterMesh to distinguish clusters. Default is `0`.

## Implementation
Defined in `roles/network_plugin/cilium/defaults/main.yml` as `cilium_cluster_id: 0`. The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray >=v2.29.0 <=v2.31.0. Applies only when Cilium is the selected CNI. Related: `cilium_cluster_name`.

## References
- roles/network_plugin/cilium/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.

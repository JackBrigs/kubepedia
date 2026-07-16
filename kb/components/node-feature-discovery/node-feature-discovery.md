---
id: COMPONENT-NODE_FEATURE_DISCOVERY
type: component
title: node-feature-discovery
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: "0.16.4"
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - node-feature-discovery
tags:
  - nfd
  - scheduling
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "node_feature_discovery_version / node_feature_discovery_image_repo / node_feature_discovery_image_tag"
relations: []
---

# node-feature-discovery

## Summary
node-feature-discovery (NFD) is the Kubernetes SIG project that detects hardware and software capabilities of nodes and advertises them as node labels (and optionally extended resources), enabling capability-aware scheduling. In Kubespray it is an opt-in add-on: the enable flag `node_feature_discovery_enabled` defaults to `false`, so it is not deployed unless explicitly enabled. Across all indexed tags (v2.29.0 through v2.31.0) the pinned version is `0.16.4`.

## Context
This document covers Kubespray tags v2.29.0, v2.29.1, v2.30.0, and v2.31.0. NFD is disabled by default (`node_feature_discovery_enabled: false`). When enabled it is deployed by the `kubernetes-apps/node_feature_discovery` role (gated in `roles/kubernetes-apps/meta/main.yml`). It runs a master/worker topology that labels nodes with detected features so that workloads can target nodes by capability. It depends only on a running cluster and does not require external storage.

## Implementation
The version is defined in `roles/kubespray_defaults/defaults/main/download.yml`:

```yaml
node_feature_discovery_version: 0.16.4
node_feature_discovery_image_repo: "{{ kube_image_repo }}/nfd/node-feature-discovery"
node_feature_discovery_image_tag: "v{{ node_feature_discovery_version }}"
```

The image tag is derived by prefixing `v` to the version. The version is identical in every indexed tag:

| Tag | node_feature_discovery_version |
|-----|--------------------------------|
| v2.29.0 | 0.16.4 |
| v2.29.1 | 0.16.4 |
| v2.30.0 | 0.16.4 |
| v2.31.0 | 0.16.4 |

Image repo (v2.31.0): `{{ kube_image_repo }}/nfd/node-feature-discovery`; image tag `v0.16.4`.

## Configuration
- Enable flag: `node_feature_discovery_enabled` — default `false` (`roles/kubernetes-apps/node_feature_discovery/defaults/main.yml`; also set `false` in `inventory/sample/group_vars/k8s_cluster/addons.yml`).
- Version var: `node_feature_discovery_version` — default `0.16.4`.
- Image repo: `node_feature_discovery_image_repo` — `{{ kube_image_repo }}/nfd/node-feature-discovery`.
- Image tag: `node_feature_discovery_image_tag` — `v{{ node_feature_discovery_version }}`.

## Compatibility
The pinned version is `0.16.4` for all four indexed tags (no change between v2.29.0 and v2.31.0). Applicable to the Kubernetes versions shipped by those Kubespray tags (approximately Kubernetes 1.31–1.35). Suitable for clusters needing capability-based node labeling and scheduling.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.

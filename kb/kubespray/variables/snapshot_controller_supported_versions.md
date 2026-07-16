---
id: VARIABLE-SNAPSHOT_CONTROLLER_SUPPORTED_VERSIONS
type: variable
title: snapshot_controller_supported_versions
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - snapshot_controller_supported_versions
tags:
  - csi
  - storage
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Mapping of Kubernetes minor version to the supported snapshot-controller image tag"
relations: []
---

# snapshot_controller_supported_versions

## Summary
A mapping (dict) from Kubernetes minor version (`kube_major_version`) to the
supported CSI snapshot-controller image tag. It is consumed by
`snapshot_controller_image_tag`. The image tag is `v7.0.2` for every entry in
all four tags; only the set of covered Kubernetes minors changes between
releases.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml`. The tag value
is always `v7.0.2`, but the Kubernetes minor keys shift per Kubespray version:

| Kubespray | Kubernetes keys (all mapped to v7.0.2) |
|-----------|----------------------------------------|
| v2.29.0   | '1.31', '1.32', '1.33'                 |
| v2.29.1   | '1.31', '1.32', '1.33'                 |
| v2.30.0   | '1.32', '1.33', '1.34'                 |
| v2.31.0   | '1.33', '1.34', '1.35'                 |

## Compatibility
Kubespray v2.29.0 through v2.31.0. Consumed by `snapshot_controller_image_tag`
via the `kube_major_version` lookup key.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.

---
id: VARIABLE-SNAPSHOT_CONTROLLER_IMAGE_TAG
type: variable
title: snapshot_controller_image_tag
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - snapshot_controller_image_tag
tags:
  - csi
  - storage
  - image
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Image tag for the CSI snapshot-controller, selected by Kubernetes major version"
relations: []
---

# snapshot_controller_image_tag

## Summary
Container image tag for the CSI external snapshot-controller. It is looked up
from `snapshot_controller_supported_versions` using the cluster's
`kube_major_version` key, so the effective tag depends on the deployed
Kubernetes minor version.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml`:

```yaml
snapshot_controller_image_tag: "{{ snapshot_controller_supported_versions[kube_major_version] }}"
```

The expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0. In
all four tags the resolved value is `v7.0.2` for every supported Kubernetes
minor (the mapping table itself shifts which minors it covers - see
`snapshot_controller_supported_versions`).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Depends on
`snapshot_controller_supported_versions` and `kube_major_version`. Paired with
`snapshot_controller_image_repo`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.

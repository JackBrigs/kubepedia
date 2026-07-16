---
id: VARIABLE-KUBELET_BINARY_CHECKSUM
type: variable
title: kubelet_binary_checksum
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubelet_binary_checksum
tags:
  - kubelet
  - checksum
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Computed checksum for the kubelet binary, selected by arch and kube_version"
relations:
  - type: see_also
    target: CONCEPT-CONTROL_PLANE_COMPONENT_VERSIONS
---

# kubelet_binary_checksum

## Summary
Holds the checksum used to verify the downloaded kubelet binary. It is not a static value: it is looked up from the `kubelet_checksums` map by CPU architecture and the target Kubernetes version.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as a computed expression:

```yaml
kubelet_binary_checksum: "{{ kubelet_checksums[image_arch][kube_version] }}"
```

The expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (only the line number shifts: 183 in v2.29.0, 185 in v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Depends on `kubelet_checksums` (the source map), `image_arch`, and `kube_version`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.

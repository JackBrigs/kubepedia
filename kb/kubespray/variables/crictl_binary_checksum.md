---
id: VARIABLE-CRICTL_BINARY_CHECKSUM
type: variable
title: crictl_binary_checksum
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - crictl_binary_checksum
tags:
  - crictl
  - checksum
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Checksum of the crictl binary archive, looked up by arch and version"
relations: []
---

# crictl_binary_checksum

## Summary
The expected checksum of the downloaded crictl (cri-tools) binary archive, used
to verify the download. Computed by indexing the `crictl_checksums` map by the
target architecture and crictl version.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as the same
computed expression across all four tags:

```yaml
crictl_binary_checksum: "{{ crictl_checksums[image_arch][crictl_version] }}"
```

The expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0. The
resolved checksum values live in the `crictl_checksums` map in
`roles/kubespray_defaults/vars/main/checksums.yml`.

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Depends on `image_arch`,
`crictl_version`, and the `crictl_checksums` map.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- roles/kubespray_defaults/vars/main/checksums.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.

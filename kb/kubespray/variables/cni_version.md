---
id: VARIABLE-CNI_VERSION
type: variable
title: cni_version
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cni_version
tags:
  - cni
  - version
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "CNI plugins version, derived from the first key of the amd64 checksums map"
relations:
  - type: see_also
    target: COMPONENT-CNI_PLUGINS
---

# cni_version

## Summary
Version of the CNI plugins to install. Computed as the first key of the `cni_binary_checksums['amd64']` map, so the default tracks the newest entry defined in that checksum table.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

```yaml
cni_version: "{{ (cni_binary_checksums['amd64'] | dict2items)[0].key }}"
```

This computed expression is unchanged across v2.29.0-v2.31.0 (line 115 in v2.29.0, 117 in v2.29.1/v2.30.0/v2.31.0). The resolved value depends on the `cni_binary_checksums` table, which may differ per tag.

## Compatibility
Kubespray >=v2.29.0 <=v2.31.0. Depends on `cni_binary_checksums`. Consumed by `cni_download_url` and `cni_binary_checksum`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.

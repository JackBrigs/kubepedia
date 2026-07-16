---
id: VARIABLE-SKOPEO_VERSION
type: variable
title: skopeo_version
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - skopeo_version
tags:
  - skopeo
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Selects the skopeo version as the first amd64 key from the checksums map"
relations: []
---

# skopeo_version

## Summary
The skopeo binary version, taken as the first `amd64` key of the checksums map. Computed as `"{{ (skopeo_binary_checksums['amd64'] | dict2items)[0].key }}"`, which resolves to `1.16.1`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

```yaml
skopeo_version: "{{ (skopeo_binary_checksums['amd64'] | dict2items)[0].key }}"
```

The expression is unchanged across v2.29.0-v2.31.0 (line 127 in v2.29.0, 129 in v2.29.1/v2.30.0/v2.31.0). The first `amd64` key in `skopeo_binary_checksums` is `1.16.1` in all four tags, so the effective version is `1.16.1`.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Derived from `skopeo_binary_checksums`; feeds `skopeo_download_url` and `skopeo_binary_checksum`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- roles/kubespray_defaults/vars/main/checksums.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.

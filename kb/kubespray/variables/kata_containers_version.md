---
id: VARIABLE-KATA_CONTAINERS_VERSION
type: variable
title: kata_containers_version
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kata_containers_version
tags:
  - kata
  - version
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Selected Kata Containers version, derived from the first amd64 checksum key"
relations: []
---

# kata_containers_version

## Summary
The Kata Containers version to install. Not a literal default: it is computed as the first key of the amd64 branch of `kata_containers_binary_checksums`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml`:

```yaml
kata_containers_version: "{{ (kata_containers_binary_checksums['amd64'] | dict2items)[0].key }}"
```

The expression is unchanged across v2.29.0-v2.31.0 (line 78 in v2.29.0; line 80 in v2.29.1, v2.30.0, v2.31.0). In every one of the four tags the first amd64 key is `3.7.0`, so the resolved default version is `3.7.0` throughout (even though v2.30.0 trimmed the older entries in the checksum map).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Sourced from `kata_containers_binary_checksums`; feeds `kata_containers_download_url` and `kata_containers_binary_checksum`. Relevant only when `kata_containers_enabled: true`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- roles/kubespray_defaults/vars/main/checksums.yml (source map)
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.

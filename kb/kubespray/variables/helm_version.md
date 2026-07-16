---
id: VARIABLE-HELM_VERSION
type: variable
title: helm_version
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - helm_version
tags:
  - helm
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Computed Helm version, derived from the checksums map"
relations: []
---

# helm_version

## Summary
The Helm version Kubespray downloads and installs. It is not hard-coded but computed from the first key of the `amd64` entry in `helm_archive_checksums`, so the default follows whichever version tops the checksums map for that tag.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

```yaml
helm_version: "{{ (helm_archive_checksums['amd64'] | dict2items)[0].key }}"
```

The computed expression is unchanged across v2.29.0-v2.31.0 (the effective version depends on the `helm_archive_checksums` map in `vars/main/checksums.yml`).

## Compatibility
Kubespray v2.29.0-v2.31.0. Related: `helm_archive_checksums`, `helm_download_url`, `helm_archive_checksum`, `helm_enabled`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.

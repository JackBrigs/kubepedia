---
id: VARIABLE-DOWNLOAD_DEFAULTS
type: variable
title: download_defaults
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - download_defaults
tags:
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Default field values merged into each entry of downloads"
relations: []
---

# download_defaults

## Summary
A dictionary of default field values that are combined with each entry in `downloads`, so individual download definitions only need to override the fields that differ.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml`:

```yaml
download_defaults:
  container: false
  file: false
  repo: None
  tag: None
  enabled: false
  dest: None
  url: None
  unarchive: false
  owner: "{{ kube_owner }}"
  mode: None
```

The block is unchanged across v2.29.0, v2.29.1, v2.30.0 and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Provides the base for entries in `downloads`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.

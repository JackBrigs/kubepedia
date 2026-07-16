---
id: VARIABLE-IMAGE_ARCH
type: variable
title: image_arch
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - image_arch
tags:
  - download
  - architecture
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Container image architecture, defaults to host_architecture or 'amd64'"
relations: []
---

# image_arch

## Summary
Selects the CPU architecture used when resolving container image references for downloads. It defaults to the detected host architecture, falling back to `amd64` when that is unavailable.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

```yaml
image_arch: "{{ host_architecture | default('amd64') }}"
```

The expression is unchanged across v2.29.0–v2.31.0 (only the line number shifts: line 73 in v2.29.0, line 75 in v2.29.1/v2.30.0/v2.31.0).

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Depends on `host_architecture` being set during fact gathering.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.

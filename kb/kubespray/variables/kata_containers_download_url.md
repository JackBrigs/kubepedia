---
id: VARIABLE-KATA_CONTAINERS_DOWNLOAD_URL
type: variable
title: kata_containers_download_url
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kata_containers_download_url
tags:
  - kata
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "URL of the Kata Containers static release tarball"
relations: []
---

# kata_containers_download_url

## Summary
The download URL for the Kata Containers static release tarball. Built from `github_url`, the selected `kata_containers_version`, and `image_arch`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml`:

```yaml
kata_containers_download_url: "{{ github_url }}/kata-containers/kata-containers/releases/download/{{ kata_containers_version }}/kata-static-{{ kata_containers_version }}-{{ image_arch }}.tar.xz"
```

Unchanged across v2.29.0-v2.31.0 (line 168 in v2.29.0; line 170 in v2.29.1, v2.30.0, v2.31.0). The sample inventory `inventory/sample/group_vars/all/offline.yml` (line 59) shows a commented `files_repo`-based override for offline installs.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Depends on `github_url`, `kata_containers_version`, and `image_arch`. Relevant only when `kata_containers_enabled: true`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- inventory/sample/group_vars/all/offline.yml (offline override, commented)
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.

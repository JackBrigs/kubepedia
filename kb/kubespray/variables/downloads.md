---
id: VARIABLE-DOWNLOADS
type: variable
title: downloads
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - downloads
tags:
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Dictionary of all downloadable files and container images"
relations: []
---

# downloads

## Summary
A large dictionary defining every downloadable artifact (files and container images) used by Kubespray, keyed by component (e.g. `etcd`, `cni`, ...). Each entry specifies fields such as `container`, `file`, `enabled`, `dest`, `repo`, `tag`, `checksum`, `url`, `unarchive`, `owner`, `mode`, and `groups`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as `downloads:`. Each entry is combined with the base field values in `download_defaults`. Example (`etcd` entry, v2.31.0):

```yaml
downloads:
  etcd:
    container: "{{ etcd_deployment_type != 'host' }}"
    file: "{{ etcd_deployment_type == 'host' }}"
    enabled: true
    dest: "{{ local_release_dir }}/etcd-{{ etcd_version }}-linux-{{ image_arch }}.tar.gz"
    repo: "{{ etcd_image_repo }}"
    tag: "{{ etcd_image_tag }}"
    ...
```

The `downloads:` key is present in all four tags; individual component entries evolve with component versions.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Consumed by the download role; see also `download_defaults`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.

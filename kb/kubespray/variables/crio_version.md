---
id: VARIABLE-CRIO_VERSION
type: variable
title: crio_version
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - crio_version
tags:
  - download
  - cri-o
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "computed default derived from crio_archive_checksums and kube_major_next_version"
relations: []
---

# crio_version

## Summary

`crio_version` selects the version of the CRI-O container runtime to install. It is
not hard-coded: it is computed from the `crio_archive_checksums` map, choosing the
highest known version lower than `kube_major_next_version`.

## Implementation

Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

```yaml
crio_version: "{{ (crio_archive_checksums['amd64'].keys() | select('version', kube_major_next_version, '<'))[0] }}"
```

The expression is unchanged across v2.29.0-v2.31.0. The effective value depends on the
target Kubernetes version and on the entries present in `crio_archive_checksums`.

## Compatibility

- Kubespray `v2.29.0`-`v2.31.0`: same computed expression.
- Related: `crio_archive_checksums`, `kube_major_next_version`, `crio_download_url`,
  `crio_archive_checksum`.

## References

- `roles/kubespray_defaults/defaults/main/download.yml`
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.

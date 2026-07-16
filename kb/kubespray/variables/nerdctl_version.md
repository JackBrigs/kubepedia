---
id: VARIABLE-NERDCTL_VERSION
type: variable
title: nerdctl_version
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - nerdctl_version
tags:
  - download
  - nerdctl
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Derives the nerdctl version from the first key of nerdctl_archive_checksums['amd64']"
relations:
  - type: see_also
    target: COMPONENT-NERDCTL
---

# nerdctl_version

## Summary
Version of the `nerdctl` binary that Kubespray downloads. It is not a hardcoded literal but is derived from the checksum dictionary, taking the first (newest) key of the amd64 checksums.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as a computed expression:

```yaml
nerdctl_version: "{{ (nerdctl_archive_checksums['amd64'] | dict2items)[0].key }}"
```

The expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0. The resolved version depends on the contents of `nerdctl_archive_checksums` in each tag.

## Compatibility
Kubespray range: `>=v2.29.0 <=v2.31.0`. Depends on the `nerdctl_archive_checksums` dictionary; the effective version tracks whichever checksum entry is listed first.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.

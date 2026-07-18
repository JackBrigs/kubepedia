---
id: VARIABLE-CALICO_CRDS_ARCHIVE_CHECKSUM
type: variable
title: calico_crds_archive_checksum
status: active
kubespray_version: ">=v2.27.0 <=v2.27.1"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - calico_crds_archive_checksum
tags:
  - kubespray-defaults
  - variable
sources:
  - type: code
    path: roles/kubespray-defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.27.1/roles/kubespray-defaults/defaults/main/download.yml
    note: "default: {{ calico_crds_archive_checksums[calico_version] }}"
relations: []
---
<!-- generated: variable-stub -->

# calico_crds_archive_checksum

## Summary

Kubespray variable `calico_crds_archive_checksum` — default `{{ calico_crds_archive_checksums[calico_version] }}`. Defined in `roles/kubespray-defaults/defaults/main/download.yml`. Present in Kubespray
`v2.27.0`–`v2.27.1` of the indexed range. **Removed after `v2.27.1`** (absent in later tags of the range). (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubespray-defaults/defaults/main/download.yml` (Kubespray `v2.27.1`):

```yaml
calico_crds_archive_checksum: {{ calico_crds_archive_checksums[calico_version] }}
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.27.1`. **Removed after `v2.27.1`** (absent in later tags of the range). Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubespray-defaults/defaults/main/download.yml` (Kubespray `v2.27.1`).

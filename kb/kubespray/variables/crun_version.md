---
id: VARIABLE-CRUN_VERSION
type: variable
title: crun_version
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - crun_version
tags:
  - download
  - crun
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "computed default: first key of the crun_checksums amd64 map"
relations:
  - type: see_also
    target: VARIABLE-CONTAINER_MANAGER
---

# crun_version

## Summary

`crun_version` selects the version of the crun OCI runtime to download. It is not
hard-coded: it defaults to the first key of the `crun_checksums['amd64']` map (its
newest/topmost entry).

## Implementation

Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

```yaml
crun_version: "{{ (crun_checksums['amd64'] | dict2items)[0].key }}"
```

The expression is unchanged across v2.29.0-v2.31.0. The effective value depends on the
entries present in `crun_checksums`.

## Compatibility

- Kubespray `v2.29.0`-`v2.31.0`: same computed expression.
- Related: `crun_checksums`, `crun_enabled`, `crun_download_url`, `crun_binary_checksum`.

## References

- `roles/kubespray_defaults/defaults/main/download.yml`
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.

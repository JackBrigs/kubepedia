---
id: VARIABLE-GVISOR_VERSION
type: variable
title: gvisor_version
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - gvisor_version
tags:
  - gvisor
  - container-runtime
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Computed gVisor (runsc) version, derived from the checksums map"
relations: []
---

# gvisor_version

## Summary
Selects the gVisor `runsc` version that Kubespray downloads and installs. It is not a hard-coded string but is computed from the first key of the `amd64` entry in `gvisor_runsc_binary_checksums`, so the default follows whichever version tops the checksums map for that tag.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

```yaml
gvisor_version: "{{ (gvisor_runsc_binary_checksums['amd64'] | dict2items)[0].key }}"
```

The computed expression is unchanged across v2.29.0-v2.31.0 (the effective version depends on the `gvisor_runsc_binary_checksums` map in `vars/main/checksums.yml`).

## Compatibility
Kubespray v2.29.0-v2.31.0. Related: `gvisor_runsc_binary_checksums`, `gvisor_enabled`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.

---
id: VARIABLE-CRIO_SUPPORTED_VERSIONS
type: variable
title: crio_supported_versions
status: active
kubespray_version: ">=v2.27.0 <=v2.28.1"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - crio_supported_versions
tags:
  - kubespray-defaults
  - variable
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.28.1/roles/kubespray_defaults/defaults/main/download.yml
    note: "default: (structured / block value — see source)"
relations: []
---
<!-- generated: variable-stub -->

# crio_supported_versions

## Summary

Kubespray variable `crio_supported_versions` — default `(structured / block value — see source)`. Defined in `roles/kubespray_defaults/defaults/main/download.yml`. Present in Kubespray
`v2.27.0`–`v2.28.1` of the indexed range. **Removed after `v2.28.1`** (absent in later tags of the range). (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubespray_defaults/defaults/main/download.yml` (Kubespray `v2.28.1`):

```yaml
crio_supported_versions: (structured / block value — see source)
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.28.1`. **Removed after `v2.28.1`** (absent in later tags of the range). Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubespray_defaults/defaults/main/download.yml` (Kubespray `v2.28.1`).

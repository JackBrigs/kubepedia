---
id: VARIABLE-YOUKI_BIN_DIR
type: variable
title: youki_bin_dir
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - youki_bin_dir
tags:
  - container-engine
  - youki
  - variable
sources:
  - type: code
    path: roles/container-engine/youki/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/youki/defaults/main.yml
    note: "default: {{ bin_dir }}"
relations: []
---
<!-- generated: variable-stub -->

# youki_bin_dir

## Summary

Kubespray variable `youki_bin_dir` — default `{{ bin_dir }}`. Defined in `roles/container-engine/youki/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/container-engine/youki/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
youki_bin_dir: {{ bin_dir }}
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/container-engine/youki/defaults/main.yml` (Kubespray `v2.31.0`).

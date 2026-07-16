---
id: VARIABLE-CRUN_ENABLED
type: variable
title: crun_enabled
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - crun_enabled
tags:
  - crun
  - runtime
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "crun_enabled: false (default)"
relations:
  - type: see_also
    target: VARIABLE-CONTAINER_MANAGER
---

# crun_enabled

## Summary

`crun_enabled` toggles installation of the crun OCI runtime. The default is `false`,
so crun is not deployed unless explicitly enabled.

## Implementation

Defined in `roles/kubespray_defaults/defaults/main/main.yml` as:

```yaml
crun_enabled: false
```

The default is unchanged across v2.29.0-v2.31.0 (the line number shifts between tags:
L344 in v2.29.0/v2.29.1, L345 in v2.30.0, L357 in v2.31.0).

## Compatibility

- Kubespray `v2.29.0`-`v2.31.0`: default `false`.
- Related: `crun_version`, `crun_download_url`, `crun_binary_checksum`.

## References

- `roles/kubespray_defaults/defaults/main/main.yml`
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.

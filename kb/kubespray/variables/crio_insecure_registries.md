---
id: VARIABLE-CRIO_INSECURE_REGISTRIES
type: variable
title: crio_insecure_registries
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - crio_insecure_registries
tags:
  - cri-o
  - registry
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "crio_insecure_registries: [] (empty list default)"
relations: []
---

# crio_insecure_registries

## Summary

`crio_insecure_registries` lists container registries that CRI-O should treat as
insecure (allowing plain HTTP or skipped TLS verification). The default is an empty
list, meaning no insecure registries are configured.

## Implementation

Defined in `roles/kubespray_defaults/defaults/main/main.yml` as:

```yaml
crio_insecure_registries: []
```

The default is unchanged across v2.29.0-v2.31.0 (the line number shifts between tags:
L363 in v2.29.0/v2.29.1, L364 in v2.30.0, L376 in v2.31.0).

## Compatibility

- Kubespray `v2.29.0`-`v2.31.0`: default empty list.
- Applies when `container_manager: crio`. Populate with registry hostnames to allow
  insecure pulls.

## References

- `roles/kubespray_defaults/defaults/main/main.yml`
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.

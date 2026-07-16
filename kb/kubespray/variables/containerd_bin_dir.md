---
id: VARIABLE-CONTAINERD_BIN_DIR
type: variable
title: containerd_bin_dir
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - containerd_bin_dir
tags:
  - containerd
  - path
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Directory for containerd binaries, defaults to bin_dir"
relations: []
---

# containerd_bin_dir

## Summary
Directory where containerd binaries are installed. Defaults to the value of `bin_dir`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as:

```yaml
containerd_bin_dir: "{{ bin_dir }}"
```

This computed expression is unchanged across v2.29.0-v2.31.0 (line 109 in v2.29.0/v2.29.1/v2.31.0, 110 in v2.30.0).

## Compatibility
Kubespray >=v2.29.0 <=v2.31.0. Depends on `bin_dir`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.

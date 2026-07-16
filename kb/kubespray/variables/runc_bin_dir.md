---
id: VARIABLE-RUNC_BIN_DIR
type: variable
title: runc_bin_dir
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - runc_bin_dir
tags:
  - runc
  - container-runtime
sources:
  - type: code
    path: roles/container-engine/runc/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/runc/defaults/main.yml
    note: "Defines runc_bin_dir defaulting to bin_dir"
relations: []
---

# runc_bin_dir

## Summary
Directory into which the runc binary is installed. Defaults to the value of `bin_dir`.

## Implementation
Defined in `roles/container-engine/runc/defaults/main.yml` as `runc_bin_dir: "{{ bin_dir }}"`. The computed expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Present in Kubespray >=v2.29.0 <=v2.31.0. Resolves to whatever `bin_dir` is set to. Related variable: `bin_dir`.

## References
- roles/container-engine/runc/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.

---
id: VARIABLE-ENABLE_CDI
type: variable
title: enable_cdi
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - enable_cdi
tags:
  - containerd
  - cdi
sources:
  - type: code
    path: roles/container-engine/containerd/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/containerd/defaults/main.yml
    note: "Default enable_cdi: false"
relations: []
---

# enable_cdi

## Summary
Enables the Container Device Interface (CDI) in the containerd configuration. Default: `false`.

## Implementation
Defined in `roles/container-engine/containerd/defaults/main.yml` as `enable_cdi: false`. The value is unchanged across v2.29.0, v2.29.1, v2.30.0 and v2.31.0 (the line moved from 130 to 129 between v2.29.1 and v2.30.0, but the default is identical).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Applies to the containerd container-engine role.

## References
- roles/container-engine/containerd/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.

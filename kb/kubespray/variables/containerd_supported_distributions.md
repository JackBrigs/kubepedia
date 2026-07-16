---
id: VARIABLE-CONTAINERD_SUPPORTED_DISTRIBUTIONS
type: variable
title: containerd_supported_distributions
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - containerd_supported_distributions
tags:
  - containerd
  - distributions
sources:
  - type: code
    path: roles/container-engine/containerd/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/containerd/defaults/main.yml
    note: "List of Linux distributions on which containerd installation is supported"
relations:
  - type: see_also
    target: COMPONENT-CONTAINERD
---

# containerd_supported_distributions

## Summary
A list of Linux distribution names (`ansible_distribution` values) on which the containerd role supports installation. Used to guard/validate that containerd is being installed on a supported OS.

## Implementation
Defined in `roles/container-engine/containerd/defaults/main.yml` as a YAML list. The list is identical across v2.29.0–v2.31.0 (line 109 in v2.29.x, line 108 in v2.30.0/v2.31.0):

```yaml
containerd_supported_distributions:
  - "CentOS"
  - "OracleLinux"
  - "RedHat"
  - "Ubuntu"
  - "Debian"
  - "Fedora"
  - "AlmaLinux"
  - "Rocky"
  - "Amazon"
  - "Flatcar"
  - "Flatcar Container Linux by Kinvolk"
  - "Suse"
  - "openSUSE Leap"
  - "openSUSE Tumbleweed"
  - "Kylin Linux Advanced Server"
  - "UnionTech"
  - "UniontechOS"
  - "openEuler"
```

## Compatibility
Present and unchanged in v2.29.0–v2.31.0.

## References
- roles/container-engine/containerd/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.

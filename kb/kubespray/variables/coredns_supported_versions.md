---
id: VARIABLE-COREDNS_SUPPORTED_VERSIONS
type: variable
title: coredns_supported_versions
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - coredns_supported_versions
tags:
  - coredns
  - versions
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Map of Kubernetes minor version -> CoreDNS version used to derive coredns_version"
relations:
  - type: see_also
    target: COMPONENT-COREDNS
---

# coredns_supported_versions

## Summary
A mapping from Kubernetes minor version (e.g. `'1.33'`) to the CoreDNS image
version that Kubespray installs for that Kubernetes release. Used to compute
`coredns_version`. The map content differs between tags.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml`. The map is
keyed by quoted Kubernetes minor version and changes per tag:

| Tag | Map content |
|-----|-------------|
| v2.29.0 | `'1.33': 1.12.0`, `'1.32': 1.11.3`, `'1.31': 1.11.3` |
| v2.29.1 | `'1.33': 1.12.0`, `'1.32': 1.11.3`, `'1.31': 1.11.3` |
| v2.30.0 | `'1.34': 1.12.1`, `'1.33': 1.12.0`, `'1.32': 1.11.3` |
| v2.31.0 | `'1.35': 1.12.4`, `'1.34': 1.12.1`, `'1.33': 1.12.0` |

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Consumed by `coredns_version`
(`coredns_supported_versions[kube_major_version]`).

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.

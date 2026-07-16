---
id: VARIABLE-KUBECTL_CHECKSUMS
type: variable
title: kubectl_checksums
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubectl_checksums
tags:
  - kubectl
  - checksum
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/vars/main/checksums.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/vars/main/checksums.yml
    note: "Map of kubectl SHA256 checksums keyed by architecture and Kubernetes version"
relations: []
---

# kubectl_checksums

## Summary
A nested map of SHA256 checksums for the `kubectl` binary, keyed by CPU
architecture (`arm`, `arm64`, `amd64`, `ppc64le`, ...) and then by Kubernetes
version. Consumed by `kubectl_binary_checksum` to verify downloads.

## Implementation
Defined in `roles/kubespray_defaults/vars/main/checksums.yml` (starts at the
`kubectl_checksums:` key). It is a large data table, not a scalar. The set of
per-version checksum entries differs between tags because each release supports a
different span of Kubernetes versions; the structure (arch -> version -> sha256)
is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0. Definition start line:
206 (v2.29.0), 230 (v2.29.1), 176 (v2.30.0), 149 (v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Referenced by `kubectl_binary_checksum`.

## References
- roles/kubespray_defaults/vars/main/checksums.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.

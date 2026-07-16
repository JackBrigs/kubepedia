---
id: VARIABLE-RUNC_CHECKSUMS
type: variable
title: runc_checksums
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - runc_checksums
tags:
  - runc
  - checksum
sources:
  - type: code
    path: roles/kubespray_defaults/vars/main/checksums.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/vars/main/checksums.yml
    note: "Map of runc SHA checksums keyed by arch and version"
relations: []
---

# runc_checksums

## Summary
A nested map of runc binary SHA checksums, keyed by architecture (e.g. `amd64`, `arm64`) and then by runc version. Provides the source data for `runc_binary_checksum` and drives the default `runc_version` selection.

## Implementation
Defined in `roles/kubespray_defaults/vars/main/checksums.yml` under the top-level `runc_checksums:` key. The set of listed versions and per-arch checksum entries changes between tags as new runc releases are added, but the variable name, location, and structure (arch -> version -> checksum) are unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Present in Kubespray >=v2.29.0 <=v2.31.0. Consumed by `runc_binary_checksum` and `runc_version`.

## References
- roles/kubespray_defaults/vars/main/checksums.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.

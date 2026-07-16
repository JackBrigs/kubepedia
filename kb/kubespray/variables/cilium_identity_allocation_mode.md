---
id: VARIABLE-CILIUM_IDENTITY_ALLOCATION_MODE
type: variable
title: cilium_identity_allocation_mode
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_identity_allocation_mode
tags:
  - cilium
  - networking
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "cilium_identity_allocation_mode: crd (default, unchanged value; file moved in v2.31.0)"
relations:
  - type: see_also
    target: COMPONENT-CILIUM
---

# cilium_identity_allocation_mode

## Summary

`cilium_identity_allocation_mode` selects how Cilium allocates security
identities. The default is `crd` across `v2.29.0`-`v2.31.0`. The value is
unchanged, but the defining file moved between tags.

## Implementation

The literal value `crd` is unchanged across all four tags. The definition moved
location:

| Tag | Defining path |
| --- | --- |
| v2.29.0 | `roles/network_plugin/cilium/defaults/main.yml` (line 32) |
| v2.29.1 | `roles/network_plugin/cilium/defaults/main.yml` (line 32) |
| v2.30.0 | `roles/network_plugin/cilium/defaults/main.yml` (line 30) |
| v2.31.0 | `roles/kubespray_defaults/defaults/main/main.yml` (line 234) |

With `crd`, identities are stored as Kubernetes CRDs (the alternative being a
key-value store).

## Compatibility

- Kubespray `v2.29.0`-`v2.31.0`: default `crd`.
- Effective only with `kube_network_plugin: cilium`.
- File relocated to the kubespray_defaults role in `v2.31.0`.

## References

- v2.29.0-v2.30.0: `roles/network_plugin/cilium/defaults/main.yml`
- v2.31.0: `roles/kubespray_defaults/defaults/main/main.yml`
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.

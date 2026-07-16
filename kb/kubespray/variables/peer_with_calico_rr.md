---
id: VARIABLE-PEER_WITH_CALICO_RR
type: variable
title: peer_with_calico_rr
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - peer_with_calico_rr
tags:
  - calico
  - bgp
  - cni
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Whether Calico nodes peer with dedicated route reflectors; computed from presence of the calico_rr host group."
relations: []
---

# peer_with_calico_rr

## Summary
Controls whether Calico nodes establish BGP peering with dedicated Calico route reflectors. The value is computed automatically: it is true when a non-empty `calico_rr` host group is present in the inventory, and false otherwise.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as a computed default:

```yaml
peer_with_calico_rr: "{{ 'calico_rr' in groups and groups['calico_rr'] | length > 0 }}"
```

The expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line number drifts from 224 in v2.29.0 to 237 in v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Applies to the Calico CNI. Related concepts: the `calico_rr` inventory host group and the `peer_with_router` variable.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.

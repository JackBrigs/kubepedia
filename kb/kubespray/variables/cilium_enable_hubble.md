---
id: VARIABLE-CILIUM_ENABLE_HUBBLE
type: variable
title: cilium_enable_hubble
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: 2026-07-16
confidence: confirmed
aliases:
  - cilium_enable_hubble
tags:
  - cilium
  - hubble
  - observability
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "cilium_enable_hubble: false (default, unchanged v2.29.0–v2.31.0)"
relations:
  - type: part_of
    target: COMPONENT-CILIUM
---

# cilium_enable_hubble

## Summary

`cilium_enable_hubble` toggles Hubble, Cilium's network observability layer
(flow visibility, metrics, service map). The default is `false` across
`v2.29.0`–`v2.31.0`, so Hubble is not deployed unless explicitly enabled.

## Implementation

Defined in `roles/network_plugin/cilium/defaults/main.yml` (`false`, unchanged
across all four tags). Enabling it deploys the Hubble components alongside Cilium;
related `cilium_hubble_*` variables configure the relay and UI. Applies only when
[[COMPONENT-CILIUM]] is the CNI.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`: default `false`.
- Effective only with `kube_network_plugin: cilium`.
- Enabling Hubble adds observability workloads; size the cluster accordingly.

## References

- `roles/network_plugin/cilium/defaults/main.yml` — default (tags v2.29.0
  `9991412`, v2.29.1 `0c6a295`, v2.30.0 `f4ccdb5`, v2.31.0 `1c9add4`).

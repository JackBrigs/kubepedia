---
id: VARIABLE-CILIUM_MTU
type: variable
title: cilium_mtu
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_mtu
tags:
  - cilium
  - cni
  - mtu
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "Default cilium_mtu: \"0\""
relations:
  - type: see_also
    target: COMPONENT-CILIUM
---

# cilium_mtu

## Summary
Sets the MTU used by Cilium for its network devices. Default `"0"`, which lets Cilium auto-detect the MTU. Rendered into the Cilium Helm values as `MTU`.

## Implementation
Defined in `roles/network_plugin/cilium/defaults/main.yml` as `cilium_mtu: "0"`. Consumed by `roles/network_plugin/cilium/templates/values.yaml.j2` as `MTU: {{ cilium_mtu }}`. The default value `"0"` is unchanged across v2.29.0-v2.31.0 (line number shifts: 9 in v2.29.0/v2.29.1, 7 in v2.30.0/v2.31.0). The sample inventory `k8s-net-cilium.yml` shows a commented `# cilium_mtu: ""` example.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Note the role default `"0"` differs from the commented sample-inventory example `""`.

## References
- roles/network_plugin/cilium/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.

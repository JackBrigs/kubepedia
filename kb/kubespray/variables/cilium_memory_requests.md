---
id: VARIABLE-CILIUM_MEMORY_REQUESTS
type: variable
title: cilium_memory_requests
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_memory_requests
tags:
  - cilium
  - cni
  - resources
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "Default cilium_memory_requests: 64M"
relations:
  - type: see_also
    target: COMPONENT-CILIUM
---

# cilium_memory_requests

## Summary
Sets the memory resource request for the Cilium agent pods. Default `64M`. Exposed to users (commented) in the sample inventory `k8s-net-cilium.yml`.

## Implementation
Defined in `roles/network_plugin/cilium/defaults/main.yml` as `cilium_memory_requests: 64M` (under the "Limits for apps" comment). In v2.31.0 it is also referenced in `roles/network_plugin/cilium/templates/values.yaml.j2` as `memory: "{{ cilium_memory_requests }}"`. The default value `64M` is unchanged across v2.29.0-v2.31.0 (line number shifts: 43 in v2.29.0/v2.29.1, 41 in v2.30.0, 26 in v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related variables: `cilium_cpu_requests`, `cilium_memory_limit`, `cilium_cpu_limit`.

## References
- roles/network_plugin/cilium/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.

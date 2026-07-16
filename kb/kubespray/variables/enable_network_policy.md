---
id: VARIABLE-ENABLE_NETWORK_POLICY
type: variable
title: enable_network_policy
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - enable_network_policy
tags:
  - network
  - cni
  - network-policy
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Enables Kubernetes NetworkPolicy support; default true"
relations: []
---

# enable_network_policy

## Summary
Toggles Kubernetes NetworkPolicy support in the cluster's CNI configuration. Default is `true`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml`:
```yaml
enable_network_policy: true
```
The default value `true` is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (only the line number varies).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Behavior depends on the selected `kube_network_plugin`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.

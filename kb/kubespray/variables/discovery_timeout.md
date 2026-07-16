---
id: VARIABLE-DISCOVERY_TIMEOUT
type: variable
title: discovery_timeout
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - discovery_timeout
tags:
  - kubeadm
  - control-plane
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "Defines discovery_timeout with default 5m0s (control-plane role)"
relations: []
---

# discovery_timeout

## Summary
Timeout used by kubeadm during the node discovery/bootstrap phase (TLS bootstrap join). It is defined in two roles with different defaults: `5m0s` in the control-plane role and `60s` in the kubeadm role.

## Implementation
Defined in two places, both present in all four tags with unchanged values:

| source_path | default |
| --- | --- |
| roles/kubernetes/control-plane/defaults/main/main.yml | `5m0s` |
| roles/kubernetes/kubeadm/defaults/main.yml | `60s` |

Line numbers: control-plane role line 42 (v2.29.0/v2.29.1) / line 45 (v2.30.0/v2.31.0); kubeadm role line 4 in all four tags. Values `5m0s` and `60s` are unchanged across v2.29.0-v2.31.0.

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Consumed when rendering kubeadm configuration for control-plane init and node join.

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- roles/kubernetes/kubeadm/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.

---
id: VARIABLE-KUBE_APISERVER_NODE_PORT_RANGE
type: variable
title: kube_apiserver_node_port_range
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_apiserver_node_port_range
tags:
  - apiserver
  - networking
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "Default \"30000-32767\" — kube-apiserver --service-node-port-range"
relations: []
---

# kube_apiserver_node_port_range

## Summary
Port range reserved for Kubernetes Services of type NodePort, passed to the kube-apiserver `--service-node-port-range` flag. Default is `"30000-32767"`.

## Implementation
Defined as `kube_apiserver_node_port_range: "30000-32767"` in `roles/kubernetes/control-plane/defaults/main/main.yml` and mirrored in `roles/kubernetes/node/defaults/main.yml` (used by the node role, e.g. for firewall/port handling). The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Available in Kubespray v2.29.0–v2.31.0. Applies to both control-plane and node roles.

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- roles/kubernetes/node/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.

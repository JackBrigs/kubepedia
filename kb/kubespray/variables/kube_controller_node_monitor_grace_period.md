---
id: VARIABLE-KUBE_CONTROLLER_NODE_MONITOR_GRACE_PERIOD
type: variable
title: kube_controller_node_monitor_grace_period
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_controller_node_monitor_grace_period
tags:
  - control-plane
  - kube-controller-manager
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "Defines node-monitor-grace-period for kube-controller-manager; default 40s"
relations:
  - type: see_also
    target: CONCEPT-CONTROL_PLANE_COMPONENT_VERSIONS
---

# kube_controller_node_monitor_grace_period

## Summary
Sets the `--node-monitor-grace-period` flag passed to kube-controller-manager via the kubeadm config. Amount of time a node is allowed to be unresponsive before being marked unhealthy. Default: `40s`.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/main.yml` as `kube_controller_node_monitor_grace_period: 40s`. It is rendered into the kubeadm config templates `roles/kubernetes/control-plane/templates/kubeadm-config.v1beta3.yaml.j2` (through v2.30.0) and `kubeadm-config.v1beta4.yaml.j2` as the `node-monitor-grace-period` controller-manager arg. The value `40s` is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Available in Kubespray v2.29.0 through v2.31.0. Related: `kube_controller_node_monitor_period`.

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.

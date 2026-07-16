---
id: VARIABLE-KUBE_CONTROLLER_MANAGER_LEADER_ELECT_LEASE_DURATION
type: variable
title: kube_controller_manager_leader_elect_lease_duration
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_controller_manager_leader_elect_lease_duration
tags:
  - control-plane
  - kube-controller-manager
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "Defines the leader-elect-lease-duration for kube-controller-manager; default 15s"
relations: []
---

# kube_controller_manager_leader_elect_lease_duration

## Summary
Sets the `--leader-elect-lease-duration` flag passed to kube-controller-manager via the kubeadm config. Controls how long a non-leader waits before attempting to acquire leadership when the current lease is not renewed. Default: `15s`.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/main.yml` as `kube_controller_manager_leader_elect_lease_duration: 15s`. It is rendered into the kubeadm config templates `roles/kubernetes/control-plane/templates/kubeadm-config.v1beta3.yaml.j2` (through v2.30.0) and `kubeadm-config.v1beta4.yaml.j2` as the `leader-elect-lease-duration` controller-manager arg. The value `15s` is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Available in Kubespray v2.29.0 through v2.31.0. Related: `kube_controller_manager_leader_elect_renew_deadline`.

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.

---
id: VARIABLE-KUBE_CONTROLLER_MANAGER_LEADER_ELECT_RENEW_DEADLINE
type: variable
title: kube_controller_manager_leader_elect_renew_deadline
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_controller_manager_leader_elect_renew_deadline
tags:
  - control-plane
  - kube-controller-manager
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "Defines the leader-elect-renew-deadline for kube-controller-manager; default 10s"
relations: []
---

# kube_controller_manager_leader_elect_renew_deadline

## Summary
Sets the `--leader-elect-renew-deadline` flag passed to kube-controller-manager via the kubeadm config. Controls the interval within which the acting leader must renew its lease before stopping leadership. Default: `10s`.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/main.yml` as `kube_controller_manager_leader_elect_renew_deadline: 10s`. It is rendered into the kubeadm config templates `roles/kubernetes/control-plane/templates/kubeadm-config.v1beta3.yaml.j2` (through v2.30.0) and `kubeadm-config.v1beta4.yaml.j2` as the `leader-elect-renew-deadline` controller-manager arg. The value `10s` is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Available in Kubespray v2.29.0 through v2.31.0. Related: `kube_controller_manager_leader_elect_lease_duration`.

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.

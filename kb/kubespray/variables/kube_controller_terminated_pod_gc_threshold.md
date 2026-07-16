---
id: VARIABLE-KUBE_CONTROLLER_TERMINATED_POD_GC_THRESHOLD
type: variable
title: kube_controller_terminated_pod_gc_threshold
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_controller_terminated_pod_gc_threshold
tags:
  - control-plane
  - kube-controller-manager
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "Defines terminated-pod-gc-threshold for kube-controller-manager; default 12500"
relations:
  - type: see_also
    target: CONCEPT-CONTROL_PLANE_COMPONENT_VERSIONS
---

# kube_controller_terminated_pod_gc_threshold

## Summary
Sets the `--terminated-pod-gc-threshold` flag passed to kube-controller-manager via the kubeadm config. Number of terminated pods that can exist before the terminated pod garbage collector starts deleting them. Default: `12500`.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/main.yml` as `kube_controller_terminated_pod_gc_threshold: 12500`. It is rendered into the kubeadm config templates `roles/kubernetes/control-plane/templates/kubeadm-config.v1beta3.yaml.j2` (through v2.30.0) and `kubeadm-config.v1beta4.yaml.j2` as the `terminated-pod-gc-threshold` controller-manager arg. The value `12500` is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Available in Kubespray v2.29.0 through v2.31.0.

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.

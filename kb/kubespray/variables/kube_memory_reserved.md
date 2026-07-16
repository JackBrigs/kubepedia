---
id: VARIABLE-KUBE_MEMORY_RESERVED
type: variable
title: kube_memory_reserved
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_memory_reserved
tags:
  - kubelet
  - resources
sources:
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "Defines kube_memory_reserved default 256Mi"
relations: []
---

# kube_memory_reserved

## Summary
Amount of memory reserved by kubelet for Kubernetes system daemons (the kube-reserved memory allocation). Default is `256Mi`. The sample inventory suggests `512Mi` for control plane nodes via `kube_control_plane.yml`, but the role default remains `256Mi`.

## Implementation
Defined in `roles/kubernetes/node/defaults/main.yml`:

```yaml
kube_memory_reserved: "256Mi"
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0. The sample inventory `inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml` shows it commented as `256Mi`, and `kube_control_plane.yml` shows a commented override of `512Mi`.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related variables: `kube_cpu_reserved`, `kube_ephemeral_storage_reserved`, `kube_pid_reserved`, `kube_reserved`.

## References
- roles/kubernetes/node/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.

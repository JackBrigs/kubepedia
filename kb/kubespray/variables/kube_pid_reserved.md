---
id: VARIABLE-KUBE_PID_RESERVED
type: variable
title: kube_pid_reserved
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_pid_reserved
tags:
  - kubelet
  - resources
sources:
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "Defines kube_pid_reserved default 1000"
relations: []
---

# kube_pid_reserved

## Summary
Number of process IDs (PIDs) reserved by kubelet for Kubernetes system daemons (the kube-reserved PID allocation). Default is `"1000"`.

## Implementation
Defined in `roles/kubernetes/node/defaults/main.yml`:

```yaml
kube_pid_reserved: "1000"
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0. It is exposed as commented `# kube_pid_reserved: "1000"` in the sample inventory files `k8s-cluster.yml` and `kube_control_plane.yml`.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related variables: `kube_memory_reserved`, `kube_cpu_reserved`, `kube_ephemeral_storage_reserved`, `kube_reserved`.

## References
- roles/kubernetes/node/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.

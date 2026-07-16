---
id: VARIABLE-KUBE_RESERVED
type: variable
title: kube_reserved
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_reserved
tags:
  - kubelet
  - resource-reservation
sources:
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "Defines kube_reserved with default false"
relations: []
---

# kube_reserved

## Summary
Toggle for reserving compute resources for kube resources on nodes. Default is `false` (no reservation). The sample inventory shows it commented as `# kube_reserved: false`.

## Implementation
Defined in `roles/kubernetes/node/defaults/main.yml` at line 40:

```yaml
kube_reserved: false
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0. The sample inventory `inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml` carries a commented `# kube_reserved: false` example (role default takes precedence).

## Compatibility
Available in Kubespray v2.29.0 through v2.31.0. Related reservation variables in the same file: `kube_memory_reserved` (`256Mi`), `kube_cpu_reserved` (`100m`), `kube_ephemeral_storage_reserved` (`500Mi`), `kube_pid_reserved` (`1000`), and `kube_reserved_cgroups`.

## References
- roles/kubernetes/node/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.

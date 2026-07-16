---
id: PRACTICE-CGROUPS
type: best_practice
title: cgroups resource reservation and node allocatable enforcement
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - node allocatable
tags:
  - cgroups
  - kubelet
  - resources
sources:
  - type: docs
    path: docs/operations/cgroups.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/operations/cgroups.md
    note: "kubelet cgroup limits, reservations, and node allocatable enforcement"
relations: []
---

# cgroups resource reservation and node allocatable enforcement

## Summary
kubelet can use cgroups to limit resource usage and avoid contention between containers and host daemons. Kubespray exposes variables to enforce node allocatable at several levels (pods, kube-reserved, system-reserved) and to reserve CPU/memory/storage/PID for the kube and system daemon slices. Enforcing reserved levels requires pointing kubelet at dedicated cgroups.

## Context
Applies when tuning kubelet resource management on cluster nodes. The main switch is `kubelet_enforce_node_allocatable`. Enforcing `kube-reserved` or `system-reserved` additionally requires `kube_reserved_cgroups` / `system_reserved_cgroups` to be specified. Reserving resources (memory/CPU/etc.) does not by itself require running daemons in dedicated cgroups — that is only needed to enforce limits on those daemons.

## Implementation
Node allocatable enforcement (comma-separated levels):
```yaml
kubelet_enforce_node_allocatable: "pods"
# kubelet_enforce_node_allocatable: "pods,kube-reserved"
# kubelet_enforce_node_allocatable: "pods,kube-reserved,system-reserved"
```

Full example reserving resources for kube and system daemons:
```yaml
kubelet_enforce_node_allocatable: "pods,kube-reserved,system-reserved"

# kube_reserved: true runs kubelet and container-engine daemons in a dedicated cgroup.
# Required to enforce limits on those daemons; not required merely to reserve resources.
kube_reserved: true
kube_reserved_cgroups_for_service_slice: kube.slice
kube_reserved_cgroups: "/{{ kube_reserved_cgroups_for_service_slice }}"
kube_memory_reserved: 256Mi
kube_cpu_reserved: 100m
# kube_ephemeral_storage_reserved: 2Gi
# kube_pid_reserved: "1000"

system_reserved: true
system_reserved_cgroups_for_service_slice: system.slice
system_reserved_cgroups: "/{{ system_reserved_cgroups_for_service_slice }}"
system_memory_reserved: 512Mi
system_cpu_reserved: 500m
# system_ephemeral_storage_reserved: 2Gi
# system_pid_reserved: "1000"
```

Resulting cgroups hierarchy (slices):
```
/ (Cgroups Root)
├── kubepods.slice        (kubepods-besteffort.slice, kubepods-burstable.slice, ...)
├── kube.slice            ({{container_manager}}.service, kubelet.service, ...)
├── system.slice
└── ...
```

Caveats:
- To enforce `kube-reserved` / `system-reserved`, the corresponding `*_reserved_cgroups` must be set.
- `kube_reserved: true` / `system_reserved: true` place daemons in dedicated cgroups, which is required only to enforce limits on them, not to make plain reservations.
- See the upstream Kubernetes "Reserve Compute Resources" documentation for details.

## References
- docs/operations/cgroups.md (tag v2.31.0 1c9add4)

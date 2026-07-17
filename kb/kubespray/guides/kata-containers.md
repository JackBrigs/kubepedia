---
id: PRACTICE-KATA_CONTAINERS
type: best_practice
title: Kata Containers runtime in Kubespray
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - Kata VM runtime
tags:
  - cri
  - kata
  - sandbox
sources:
  - type: docs
    path: docs/CRI/kata-containers.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/CRI/kata-containers.md
    note: "Enabling and configuring Kata Containers lightweight-VM runtime"
relations:
  - type: see_also
    target: CONCEPT-CONTAINER_RUNTIMES
---

# Kata Containers runtime in Kubespray

## Summary
Kata Containers is a secure container runtime that runs workloads inside lightweight virtual machines. Kubespray supports it only with the Qemu hypervisor. It is enabled via containerd, generates a `kata-qemu` RuntimeClass, and integrates with the Kubernetes Pod Overhead feature for accurate VM resource accounting.

## Context
Applies when you need VM-level workload isolation. Requires `container_manager: containerd` and `etcd_deployment_type: host`. By default pods still use runc; only pods that reference the `kata-qemu` RuntimeClass run under Kata. Qemu is the only supported hypervisor.

## Implementation
Enable Kata Containers:

```yaml
# k8s-cluster.yml
container_manager: containerd
kata_containers_enabled: true
```

```yaml
# etcd.yml
etcd_deployment_type: host
```

Run a workload under Kata by setting `runtimeClassName: kata-qemu` in the pod spec (verify with `kubectl get runtimeclass`, which shows the `kata-qemu` class/handler).

Pod Overhead (recommended, and mandatory if Kata pods use resource limits):

- Configure the kubelet cgroup driver:
  - `kubelet_cgroup_driver: cgroupfs` — works best.
  - `kubelet_cgroup_driver: systemd` — usable when running cgroups v2.
- Qemu hypervisor overhead values:

```yaml
kata_containers_qemu_overhead: true
kata_containers_qemu_overhead_fixed_cpu: 10m
kata_containers_qemu_overhead_fixed_memory: 290Mi
```

Optional:

- `kata_containers_version: 2.2.2` — pin a specific Kata release (see Kata Containers GitHub releases).
- `kata_containers_qemu_debug: 'false'` — debug is disabled by default for all Kata components; toggle here.

Caveat: Pod Overhead is mandatory for Kata pods that declare resource limits, so the kubelet cgroup driver must be set accordingly.

## References
- docs/CRI/kata-containers.md (tag v2.31.0 1c9add4)

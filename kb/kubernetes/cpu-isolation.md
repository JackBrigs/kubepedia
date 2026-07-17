---
id: CONFIG-CPU_ISOLATION
type: configuration
title: "Running OS/kubelet and workloads on separate CPU cores (CPU isolation)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: confirmed
aliases:
  - cpu isolation
  - dedicate cpu cores to kubelet
  - run os and kubelet on separate cores
  - reservedSystemCPUs
  - cpuManagerPolicy static
  - exclusive cpu cores for pods
  - cpu pinning kubernetes
  - isolate system cpus from workloads
tags:
  - kubernetes
  - kubelet
  - cpu
  - performance
  - configuration
sources:
  - type: code
    path: roles/kubernetes/node/templates/kubelet-config.v1beta1.yaml.j2
    lines: "81-127"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/templates/kubelet-config.v1beta1.yaml.j2
    note: "kubelet_config_extra_args merge; cpuManagerPolicy/(+Options)/topologyManagerPolicy rendered when defined (tag v2.31.0)"
  - type: docs
    path: kubernetes.io — Control CPU Management Policies / Reserve Compute Resources
    url: https://kubernetes.io/docs/tasks/administer-cluster/cpu-management-policies/
    note: "reservedSystemCPUs pins system+kubelet to a CPU set; static CPU manager gives Guaranteed pods exclusive cores"
relations:
  - type: see_also
    target: PRACTICE-CGROUPS
  - type: see_also
    target: CONFIG-KUBELET_CONFIGURATION
  - type: see_also
    target: TROUBLE-OOMKILLED
---

# Running OS/kubelet and workloads on separate CPU cores (CPU isolation)

## Summary

To keep the **OS + kubelet** off the cores your **workloads** use, combine two kubelet
mechanisms: **`reservedSystemCPUs`** pins system/kubelet housekeeping to a specific CPU
set, and **`cpuManagerPolicy: static`** hands the *remaining* cores out **exclusively** to
Guaranteed pods. Kubespray exposes the CPU-manager policy as a variable but has **no
dedicated variable for `reservedSystemCPUs`** — you set it through
`kubelet_config_extra_args`.

## Configuration

**1. Pin the OS/kubelet to specific cores — `reservedSystemCPUs`:**

Kubespray has no first-class variable for it; inject it via the free-form kubelet config:

```yaml
# reserve physical cores 0-1 for the system + kubelet; pods use the rest
kubelet_config_extra_args:
  reservedSystemCPUs: "0-1"
```

`reservedSystemCPUs` takes an explicit CPU list/range and takes precedence over the
`--kube-reserved`/`--system-reserved` *cpu quantities* for placement — the reserved cores
are removed from the pool the CPU manager can hand to pods.

**2. Give workloads exclusive cores — static CPU manager:**

```yaml
kubelet_cpu_manager_policy: "static"
# optional refinements:
# kubelet_cpu_manager_policy_options: { full-pcpus-only: "true" }
# kubelet_topology_manager_policy: "single-numa-node"   # NUMA alignment
```

With `static`, **Guaranteed** pods (integer CPU `requests == limits`) get **exclusive**
cores from the non-reserved set; other pods share the leftover shared pool.

**3. (Accounting) reserve resources for the system/kube slices:**

Pair with `kube_reserved`/`system_reserved` + their cgroups so the reserved cores/memory
are also accounted out of node Allocatable — see [[PRACTICE-CGROUPS]].

## Compatibility

- Applies to Kubespray `v2.29.0`–`v2.31.0`.
- **static CPU manager needs `reservedSystemCPUs` (or `kube/system-reserved` cpu) set** —
  the reserved amount must be non-zero, otherwise the kubelet won't start the static
  policy. Reserve at least one core for the system.
- **`cpuManagerPolicy` is a node-level setting changed only at kubelet (re)start**;
  switching to `static` on a running node requires removing the CPU manager state file
  (`/var/lib/kubelet/cpu_manager_state`) and restarting the kubelet, or the kubelet fails
  to start. Roll it out per node deliberately.
- Only **Guaranteed QoS** pods get exclusive cores — Burstable/BestEffort still float on
  the shared pool. Size requests accordingly.
- **NUMA:** for latency-sensitive workloads add `kubelet_topology_manager_policy` so CPU
  and device allocations align on the same NUMA node.
- For true kernel-level isolation of the reserved cores (keeping *all* other kernel
  threads off them) you additionally need host-level `isolcpus`/`nohz_full` boot params —
  that is an OS concern outside Kubespray/kubelet config.

## References

- kubelet template (`kubelet_config_extra_args`, `cpuManagerPolicy`) at tag `v2.31.0`;
  kubernetes.io CPU management policies. Resource reservation: [[PRACTICE-CGROUPS]];
  kubelet config surface: [[CONFIG-KUBELET_CONFIGURATION]].

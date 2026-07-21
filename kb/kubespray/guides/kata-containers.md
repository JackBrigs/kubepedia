---
id: PRACTICE-KATA_CONTAINERS
type: best_practice
title: Kata Containers runtime in Kubespray
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-21"
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
  - type: code
    path: roles/container-engine/containerd/tasks/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/containerd/tasks/main.yml
    note: "'Copy containerd config file' (kata-qemu runtime block) notifies Restart containerd — the node-level disruption of enabling Kata"
  - type: code
    path: roles/container-engine/containerd/handlers/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/containerd/handlers/main.yml
    note: "'Restart containerd' + 'wait for containerd' (ctr images ls, 8 retries)"
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

## Service impact

Enabling Kata is a **node-level runtime change**, not an add-on install.

- **containerd restarts on every node.** `kata_containers_enabled` is rendered into
  containerd's `config.toml` (the `runtimes.kata-qemu` block), and that template task
  notifies `Restart containerd`
  (`roles/container-engine/containerd/tasks/main.yml` → `handlers/main.yml`, which then waits
  for `ctr images ls` to answer). Already-running containers survive a containerd restart
  because their shims are separate processes, but the kubelet loses its CRI connection for
  those seconds: the node reports `NotReady`, and no pod can start, stop, or be probed
  meanwhile. Drain first if the node runs anything latency-sensitive.
- **Existing pods do not become Kata pods.** Only pods that ask for
  `runtimeClassName: kata-qemu` use it; everything else keeps running under runc. So the
  functional change is opt-in — the disruption is not.
- **Changing `kubelet_cgroup_driver` is the expensive part.** Pod Overhead requires a
  specific cgroup driver, and switching drivers on a live node changes the cgroup layout the
  kubelet manages: drain the node, apply, and let pods be rescheduled. Do not flip it
  cluster-wide in one run.
- **Prerequisites are hard blockers, not warnings.** Kata needs
  `container_manager: containerd` and `etcd_deployment_type: host`; a cluster running
  kubeadm-managed etcd or another runtime cannot enable it without a much larger migration.
  Hardware virtualisation must be available on the node — without it Kata pods fail to start
  while everything else looks healthy.
- **Rollout:** enable on a labelled subset of nodes first (AWX: job tag `kata-containers`
  with a `Limit` of those hosts), verify `kubectl get runtimeclass` and one test pod, then
  widen. **Backout** is `kata_containers_enabled: false` plus another run — which restarts
  containerd again — after removing every pod that references the RuntimeClass.

## References
- docs/CRI/kata-containers.md (tag v2.31.0 1c9add4)

---
id: TROUBLE-OOMKILLED
type: troubleshooting
title: "Container OOMKilled (exit 137) / node memory pressure"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - OOMKilled
  - exit code 137
  - out of memory pod
  - node memory pressure eviction
  - container killed memory limit
tags:
  - troubleshooting
  - memory
  - resources
  - nodes
sources:
  - type: docs
    path: Kubernetes resource management / node-pressure eviction
    url: https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/
    note: "OOM kill vs kubelet eviction behaviour"
relations:
  - type: see_also
    target: PRACTICE-CGROUPS
  - type: see_also
    target: TROUBLE-DISK_PRESSURE_EVICTION
  - type: see_also
    target: CONFIG-KUBELET_CONFIGURATION
---

# Container OOMKilled (exit 137) / node memory pressure

## Summary

`OOMKilled` (last state, exit code **137**) means a container exceeded its memory
**limit**, or the **node** ran out of memory and the kernel OOM killer picked a process.
The two are different: a per-container limit hit affects one container; node-level memory
pressure can take out multiple pods and cause kubelet evictions. Fix by right-sizing
requests/limits and reserving node memory.

## Problem

`kubectl get pod` shows restarts; `kubectl describe pod` shows
`Last State: Terminated, Reason: OOMKilled, Exit Code: 137`. Or nodes flap and multiple
pods restart/evict under memory pressure.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`.
- **Container OOM:** the container's `resources.limits.memory` was exceeded — the cgroup
  OOM-kills that container only.
- **Node OOM / pressure:** total usage exceeds capacity minus reservations; the kubelet
  evicts pods on `MemoryPressure`, and the kernel may OOM-kill before that. Kubespray's
  `kube_reserved`/`system_reserved` (off by default) carve out memory for the kubelet and
  system so workloads can't starve them ([[PRACTICE-CGROUPS]]).

## Diagnostics

- Confirm the cause: `kubectl describe pod <name>` → `OOMKilled` + exit `137` under Last
  State.
- Usage vs limit: `kubectl top pod` / `kubectl top node` (needs metrics-server) — is the
  container near its limit, or the node near capacity?
- Node view: `kubectl describe node <node>` → `MemoryPressure` condition, Allocatable vs
  Capacity, and eviction events.
- On the node: `dmesg | grep -i oom` / `journalctl -k | grep -i oom` shows kernel OOM
  kills and which process.

## Known Issues

**Fixes:**

- **Right-size the container:** raise `resources.limits.memory` (and set a realistic
  `requests.memory` so the scheduler places it correctly). A limit set too low for the
  real working set guarantees repeated OOM kills.
- **Reserve node headroom:** enable `kube_reserved` / `system_reserved` so the kubelet and
  OS keep memory, preventing node-wide OOM ([[PRACTICE-CGROUPS]]).
- **Add capacity / spread load:** more/larger nodes, or anti-affinity to spread memory-
  heavy pods.
- **Node OOM behaviour (cgroup v2):** the `singleProcessOOMKill` kubelet option (Kubernetes
  1.32+) changes whether one process or the whole container's group is killed — see
  [[CONFIG-KUBELET_CONFIGURATION]].

**Gotchas:**

- Exit `137` = 128 + 9 (SIGKILL) — usually OOM, but any SIGKILL shows 137; confirm the
  `OOMKilled` reason, don't assume from the code alone.
- **Requests ≠ limits:** scheduling uses requests; OOM uses limits. A pod can schedule fine
  (low request) and still OOM (low limit) under load.
- Memory pressure and **disk** pressure are different evictions — a `DiskPressure` eviction
  is not OOM ([[TROUBLE-DISK_PRESSURE_EVICTION]]).

## References

- Kubernetes resource management / node-pressure eviction. Node reservations:
  [[PRACTICE-CGROUPS]]; kubelet OOM option: [[CONFIG-KUBELET_CONFIGURATION]].

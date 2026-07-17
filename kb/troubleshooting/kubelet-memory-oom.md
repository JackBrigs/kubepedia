---
id: TROUBLE-KUBELET_MEMORY_OOM
type: troubleshooting
title: "kubelet: memory leak / systemd resets kubepods.slice limit → OOM"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: verified
aliases:
  - kubelet memory leak oomkill workloads
  - kubelet container gc leak
  - kubepods.slice memory limit reset
  - systemd cgroup memory limit full ram
tags:
  - troubleshooting
  - kubelet
  - memory
  - cgroup
sources:
  - type: docs
    path: kubelet container-GC memory leak
    url: https://github.com/kubernetes/kubernetes/issues/131905
    note: "GarbageCollect retains references"
  - type: docs
    path: systemd resets kubepods.slice MemoryLimit
    url: https://github.com/kubernetes/kubernetes/issues/88197
    note: "systemd re-applies unit MemoryLimit to full RAM"
relations:
  - type: see_also
    target: TROUBLE-KUBELET_PLEG_NOT_HEALTHY
  - type: see_also
    target: TROUBLE-CGROUP_DRIVER_MISMATCH
---

# kubelet: memory leak / systemd resets kubepods.slice limit → OOM

## Summary

Two node-OOM causes rooted in kubelet: kubelet's **own RSS leaks** over days (and since kubelet
runs at high OOM priority, the kernel kills *workloads* first), and with the **systemd cgroup
driver** systemd periodically **resets `kubepods.slice`'s memory limit to full node RAM**,
overcommitting into reserved space.

## Problem

- kubelet RSS grows over days; workloads get OOM-killed while kubelet survives; `kubectl top
  nodes` = `<unknown>`, `crictl stats` hangs.
- With `--kube-reserved`/`--system-reserved` + systemd driver, the enforced limit on
  `kubepods.slice` intermittently **jumps to full RAM** → pods/daemons OOM-killed.

## Context

- Applies to Kubernetes **1.29–1.35**. Related: PLEG stalls
  ([[TROUBLE-KUBELET_PLEG_NOT_HEALTHY]]), cgroup driver ([[TROUBLE-CGROUP_DRIVER_MISMATCH]]).

## Diagnostics

- **kubelet leak:** the container-GC path (`GarbageCollect` retains internal references so Go GC
  can't reclaim — `container_gc.go`), plus a metrics/goroutine leak from **stuck kubelet↔
  containerd stats** calls. No merged fix for the GC leak (#131905 closed not-planned) —
  **periodic kubelet restarts** are the documented mitigation; alert on kubelet
  `process_resident_memory_bytes`. For the stats variant, fix the underlying containerd stall
  (upgrade containerd — [[TROUBLE-CONTAINERD_SHIM_MEMORY_LEAK]]).
- **systemd resets the cgroup limit:** kubelet sets `memory.limit_in_bytes` on the cgroup
  directly, but systemd periodically re-applies the **unit's `MemoryLimit` property** (which
  kubelet didn't lower), resetting the file to full RAM (issue #88197). **Verify:** compare
  `systemctl show kubepods.slice -p MemoryLimit` vs the cgroup file after a `daemon-reload`.
  **Fix:** ensure kubelet writes the systemd property (PR #102147); keep runtime **and** kubelet
  both on the `systemd` driver.

## Known Issues

- Because kubelet has a protective OOM score, node memory pressure manifests as **workload**
  OOM-kills, masking the real culprit — check kubelet's own RSS trend.

## References

- k8s #131905 / #115192 / #88197, PR #102147 (above); PLEG:
  [[TROUBLE-KUBELET_PLEG_NOT_HEALTHY]]; containerd leak: [[TROUBLE-CONTAINERD_SHIM_MEMORY_LEAK]].

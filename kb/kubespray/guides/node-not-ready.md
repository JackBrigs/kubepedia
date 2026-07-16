---
id: PRACTICE-NODE_NOT_READY
type: best_practice
title: Node NotReady triage (day-2 runbook)
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - node NotReady
  - node down
  - kubelet not ready
tags:
  - operations
  - diagnostics
  - troubleshooting
sources:
  - type: docs
    path: docs/operations
    url: https://github.com/kubernetes-sigs/kubespray/tree/v2.31.0/docs/operations
    note: "operational context; commands are standard Kubernetes tooling"
relations:
  - type: see_also
    target: PRACTICE-CLUSTER_HEALTH_CHECKS
  - type: see_also
    target: PRACTICE-CILIUM_DIAGNOSTICS
---

# Node NotReady triage (day-2 runbook)

## Summary

A node shows `NotReady` when its kubelet stops reporting healthy. The usual causes
are kubelet down, container runtime down, CNI not ready, disk/memory pressure, or
certificate/clock problems. This runbook localizes the fault quickly.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0` clusters (containerd runtime, kubelet
  as a systemd service).

## Diagnostics

```bash
kubectl get nodes -o wide
kubectl describe node <node> | sed -n '/Conditions:/,/Events:/p'   # which condition is false + reason
```

Look at the `Ready` condition message. Then on the node (SSH):

```bash
systemctl status kubelet --no-pager
journalctl -u kubelet -n 80 --no-pager        # the actual error is almost always here
systemctl status containerd --no-pager        # runtime up? (see PRACTICE-CONTAINERD_DIAGNOSTICS)
crictl info | head                            # runtime responsive?
df -h /var/lib/kubelet /var/lib/containerd     # DiskPressure?
free -m                                        # MemoryPressure?
```

## Implementation

Common causes → action:
- **kubelet crashloop** → read `journalctl -u kubelet`; frequent culprits: bad
  kubelet config, expired certs ([[PRACTICE-CERTIFICATE_EXPIRY]]), swap enabled
  when `kubelet_fail_swap_on`.
- **runtime down** → [[PRACTICE-CONTAINERD_DIAGNOSTICS]].
- **CNI not ready** ("network plugin is not ready") → [[PRACTICE-CILIUM_DIAGNOSTICS]].
- **DiskPressure / MemoryPressure** → free space / evict; check `system_reserved`.
- **Clock skew** → `timedatectl`; TLS fails on large skew.

If the node is unrecoverable, drain and replace it
([[PRACTICE-NODES_ADD_REPLACE]]).

## References

- Standard `kubectl`/`kubelet`/`crictl` tooling; Kubespray `docs/operations/`.

---
id: TROUBLE-POD_CONTAINERCREATING
type: troubleshooting
title: "Pod stuck in ContainerCreating (CNI / sandbox / mount)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - ContainerCreating stuck
  - cni plugin not initialized
  - network not ready
  - failed to create pod sandbox
  - pod not starting
  - NetworkPluginNotReady
tags:
  - troubleshooting
  - pods
  - cni
  - networking
sources:
  - type: docs
    path: Kubernetes pod-lifecycle / CNI readiness
    url: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/
    note: "kubelet reports NetworkReady=false until a CNI config is present in /etc/cni/net.d"
relations:
  - type: see_also
    target: TROUBLE-CILIUM_CONFIG_VALIDATION
  - type: see_also
    target: TROUBLE-CONTAINERD_REGISTRY_CONFIG
  - type: see_also
    target: TROUBLE-PVC_PENDING_NO_STORAGECLASS
---

# Pod stuck in ContainerCreating (CNI / sandbox / mount)

## Summary

A Pod stays `ContainerCreating` when the kubelet can't finish setting it up — most often
the **CNI isn't ready** (no network for the sandbox), but also a failing **image pull**,
an unbound **volume**, or a **sandbox** creation error. `kubectl describe pod` names the
specific reason; this triage maps each to its fix.

## Problem

`kubectl get pods` shows `ContainerCreating` (or `0/1` never becoming Ready) for a long
time; the node may report `NetworkPluginNotReady` / `container runtime network not ready:
cni plugin not initialized`.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`.
- The kubelet marks the node `NetworkReady=false` until a CNI writes its config into
  `/etc/cni/net.d/` and its pods are running — new/all Pods on that node stay
  `ContainerCreating` until then.

## Diagnostics

- **`kubectl describe pod <name>`** — the Events section states the exact blocker (network
  / image / mount / sandbox). Start here.
- **CNI readiness:** `kubectl -n kube-system get pods -l k8s-app=cilium -o wide` (or your
  CNI) — agents Running on the node? `ls /etc/cni/net.d/` on the node — is there a CNI
  config?
- **Node condition:** `kubectl describe node <node>` — look for `NetworkPluginNotReady` /
  runtime errors.
- **Runtime:** `crictl ps -a` / `journalctl -u kubelet -e` for sandbox (`RunPodSandbox`)
  errors.

## Known Issues

Map the `describe` reason to its fix:

- **Network / CNI not ready** (`cni plugin not initialized`, `NetworkPluginNotReady`) —
  the CNI DaemonSet isn't healthy on that node. Check Cilium/CNI pods and their logs; a
  bad Cilium config aborts before it's ready ([[TROUBLE-CILIUM_CONFIG_VALIDATION]]); a
  blocked overlay port (VXLAN 8472) also breaks it
  ([[TROUBLE-FIREWALL_PORTS_BLOCKED]]).
- **Image pull** (`ErrImagePull`/`ImagePullBackOff` shown alongside) — registry/mirror/
  auth ([[TROUBLE-CONTAINERD_REGISTRY_CONFIG]], [[TROUBLE-IMAGE_PULL_RATE_LIMIT]]).
- **Volume / mount** (`unbound PersistentVolumeClaims`, `FailedMount`) — no
  provisioner/StorageClass ([[TROUBLE-PVC_PENDING_NO_STORAGECLASS]]) or a CSI attach/mount
  error.
- **Sandbox creation** (`Failed to create pod sandbox`) — runtime issue: check the CRI
  socket/cgroup driver ([[TROUBLE-CGROUP_DRIVER_MISMATCH]]) and the pause/sandbox image is
  pullable.

**Gotchas:**

- A **fresh node** shows every Pod `ContainerCreating` until the CNI rolls out there — wait
  for the CNI DaemonSet, don't chase individual Pods.
- `ContainerCreating` on **one** node vs the whole cluster narrows it fast: one node →
  that node's kubelet/CNI/runtime; all nodes → the CNI or a cluster-wide dependency.

## References

- Kubernetes pod lifecycle / CNI readiness. Related causes:
  [[TROUBLE-CILIUM_CONFIG_VALIDATION]], [[TROUBLE-CONTAINERD_REGISTRY_CONFIG]],
  [[TROUBLE-PVC_PENDING_NO_STORAGECLASS]], [[TROUBLE-CGROUP_DRIVER_MISMATCH]].

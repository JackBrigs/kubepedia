---
id: TROUBLE-CONTAINERD_SHIM_MEMORY_LEAK
type: troubleshooting
title: "containerd: shim/daemon memory leak (reaper deadlock, exec streams)"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: verified
aliases:
  - containerd-shim-runc-v2 memory leak
  - containerd goroutine leak exec
  - containers UNKNOWN crictl
  - shim reaper mutex deadlock
tags:
  - troubleshooting
  - containerd
  - memory
  - runtime
sources:
  - type: docs
    path: shim reaper mutex deadlock (20GB)
    url: https://github.com/containerd/containerd/issues/9217
    note: "reaper_unix.go lock contention; containers UNKNOWN"
  - type: docs
    path: exec websocket goroutine leak
    url: https://github.com/containerd/containerd/issues/11950
    note: "wsstream Open not closed after exec"
relations:
  - type: see_also
    target: COMPONENT-CONTAINERD
  - type: see_also
    target: TROUBLE-KUBELET_MEMORY_OOM
---

# containerd: shim/daemon memory leak (reaper deadlock, exec streams)

## Summary

containerd or its `containerd-shim-runc-v2` processes grow to many GB of RSS and only a restart
frees them. Two known leaks: a **reaper mutex deadlock** in the shim, and a **goroutine leak on
`kubectl exec`** (websocket streams not closed).

## Problem

- Shim processes grow to **20 GB+** RSS; containers show `UNKNOWN` in `crictl`;
  `context deadline exceeded` in logs; a shim with no children won't exit.
- containerd RSS climbs on exec-heavy nodes; goroutine dump shows accumulating
  `wsstream.(*Conn).Open` / `createWebSocketStreams`.

## Context

- Applies to Kubernetes **1.29–1.35** on containerd ([[COMPONENT-CONTAINERD]]). The kubelet may
  OOM as a downstream effect ([[TROUBLE-KUBELET_MEMORY_OOM]]).

## Diagnostics

- **Reaper deadlock (shim 20 GB):** lock contention in the shim's process-reaper path
  (`reaper_unix.go`) — exit events pile up behind a held mutex and never drain; goroutine dump
  shows many blocked in `sync.runtime_SemacquireMutex → Mutex.lockSlow`. No committed fix.
  **Clear it:** delete the stuck task/sandbox (`crictl rmp -f` / `ctr task kill`); a containerd
  restart clears leaked shims. Keep shims on the newest 1.7.x (issue #9217).
- **Exec websocket leak:** the websocket to containerd's CRI stream server isn't always closed
  after `exec`, leaving stream goroutines blocked; triggered notably by **kubectl ≥1.30 version
  skew**. **Fix:** upgrade containerd to a patched 1.7.x/2.0.x (stream timeouts/proper close,
  e.g. 1.7.29 / 2.0.7+); restart periodically on exec-heavy nodes; avoid large kubectl skew
  (issue #11950 / k8s #126608).

## Known Issues

- `containers UNKNOWN` in `crictl` is the tell that shims are wedged — a containerd restart is
  the reliable recovery.

## References

- containerd #9217 / #11950, k8s #126608 (above); component: [[COMPONENT-CONTAINERD]]; kubelet
  OOM: [[TROUBLE-KUBELET_MEMORY_OOM]].

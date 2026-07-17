---
id: TROUBLE-CONTAINERD_STALE_SANDBOX_RECOVERY
type: troubleshooting
title: "containerd: stale sandbox / reserved name after crash or disk-full"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: verified
aliases:
  - failed to destroy network for sandbox unexpected end of JSON input
  - stoppodsandbox failed
  - failed to reserve container name is reserved for
  - pods stuck terminating containerd
tags:
  - troubleshooting
  - containerd
  - runtime
  - cni
sources:
  - type: docs
    path: StopPodSandbox JSON-input investigation
    url: https://marcusnoble.co.uk/2025-09-28-investigating-and-fixing-stoppodsandbox-from-runtime-service-failed-kubelet-errors/
    note: "truncated CNI result cache under /var/lib/cni/results/"
  - type: docs
    path: reserve container name after ENOSPC
    url: https://github.com/containerd/containerd/issues/11504
    note: "stale name reservation on restart recovery"
relations:
  - type: see_also
    target: COMPONENT-CONTAINERD
  - type: see_also
    target: TROUBLE-NAMESPACE_STUCK_TERMINATING
---

# containerd: stale sandbox / reserved name after crash or disk-full

## Summary

After a node crash, ungraceful containerd exit, or a disk-full event, pods get stuck because
containerd can't tear down a **stale sandbox** or can't reuse a **reserved container name**.

## Problem

- Pods stuck `Terminating`; kubelet: `StopPodSandbox from runtime service failed: ... failed to
  destroy network for sandbox "...": ... decoding version from network config: unexpected end
  of JSON input`.
- `CreateContainerError: failed to reserve container name "..."`; on startup: `failed to
  recover state: ... name xxx is reserved for xxx`.

## Context

- Applies to Kubernetes **1.29–1.35** on containerd ([[COMPONENT-CONTAINERD]]). Namespace-stuck
  is a related terminating class ([[TROUBLE-NAMESPACE_STUCK_TERMINATING]]).

## Diagnostics

- **`unexpected end of JSON input` on sandbox stop:** a **zero-byte/truncated CNI result cache
  file** (from a crash / ungraceful exit) under **`/var/lib/cni/results/`** — containerd's CNI
  teardown can't parse it, so the sandbox never stops. **Fix:** delete the corrupted cache file
  (`rm -f /var/lib/cni/results/<network>-<SANDBOX_ID>-eth0`), then `crictl rmp <SANDBOX_ID>`.
- **`name … is reserved`:** on restart the CRI plugin reloads on-disk container state; after an
  **`ENOSPC`** (disk-full) event, containers are skipped during recovery but their **name
  reservation remains**, colliding when kubelet re-creates the same-named container. **Fix:**
  free disk space; restart containerd then kubelet for clean recovery; force-remove orphans
  (`crictl rm -f` / `crictl rmp -f`) (issues #11504/#7247).

## Known Issues

- Alert on `StopPodSandbox` failures — they silently pile up stuck pods. Upstream plans to
  tolerate `ENOSPC` during restart recovery.

## References

- StopPodSandbox writeup + containerd #11504/#7247 (above); component: [[COMPONENT-CONTAINERD]];
  namespaces: [[TROUBLE-NAMESPACE_STUCK_TERMINATING]].

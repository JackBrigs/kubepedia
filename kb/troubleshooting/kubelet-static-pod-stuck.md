---
id: TROUBLE-KUBELET_STATIC_POD_STUCK
type: troubleshooting
title: "kubelet: static pod won't restart after manifest edit + kubelet restart"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: verified
aliases:
  - static pod not restarting
  - pod worker requested for removal still not fully terminated
  - control plane static pod gone after manifest edit
  - mirror pod stuck
tags:
  - troubleshooting
  - kubelet
  - static-pods
  - control-plane
sources:
  - type: docs
    path: static pod pending-removal issue
    url: https://github.com/kubernetes/kubernetes/issues/109596
    note: "pod-worker termination leaves pod pending removal"
relations:
  - type: see_also
    target: COMPONENT-CONTAINERD
  - type: see_also
    target: CONCEPT-TROUBLESHOOTING_MAP
---

# kubelet: static pod won't restart after manifest edit + kubelet restart

## Summary

After editing a manifest in `/etc/kubernetes/manifests` and restarting kubelet, a control-plane
**static pod doesn't come back**. The pod-worker termination state machine left it "pending
removal", blocking recreation.

## Problem

- A control-plane static pod (apiserver/etcd/etc.) doesn't return after a manifest change +
  kubelet restart.
- kubelet log: `Pod worker has been requested for removal but is still not fully terminated`;
  containers killed but the **sandbox stays live**; mirror pod stuck.

## Context

- Applies to Kubernetes **1.29–1.35** (race confirmed on 1.22.8; the code path persists;
  PR #106394 addressed related handling but not this — issue #109596 closed not-planned).

## Diagnostics

- **Recovery:** **restart kubelet a second time** (triggers the cleanup and recreation); or
  delete the stale sandbox with **`crictl rmp <SANDBOX_ID>`** before restarting kubelet.
- **Avoid the trigger:** don't make **rapid successive** manifest edits across kubelet
  restarts; let each change settle (`crictl ps` shows the new static pod) before the next.
- Confirm the manifest is valid YAML (a bad manifest is a different failure — kubelet logs a
  parse error and never creates the pod).

## Known Issues

- This affects the **control plane** (static pods are how kubeadm/Kubespray run apiserver/etcd),
  so a stuck static pod can take a control-plane node's component down — recover promptly.

## References

- k8s issue #109596 (above); runtime: [[COMPONENT-CONTAINERD]].

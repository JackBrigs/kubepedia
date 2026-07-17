---
id: TROUBLE-KUBELET_NODE_NOTREADY_CNI
type: troubleshooting
title: "kubelet: node NotReady — CNI not initialized (cni plugin not initialized)"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: verified
aliases:
  - cni plugin not initialized
  - container runtime network not ready
  - NetworkPluginNotReady
  - node kubeletnotready after kubeadm init
tags:
  - troubleshooting
  - kubelet
  - cni
  - nodes
sources:
  - type: docs
    path: node NotReady CNI issue
    url: https://github.com/kubernetes/kubernetes/issues/125267
    note: "networkReady false; /etc/cni/net.d empty"
relations:
  - type: see_also
    target: COMPONENT-CALICO
  - type: see_also
    target: COMPONENT-CILIUM
  - type: see_also
    target: TROUBLE-CALICO_NODE_ISSUES
---

# kubelet: node NotReady — CNI not initialized (cni plugin not initialized)

## Summary

A node stays `NotReady` right after joining with `Container runtime network not ready:
NetworkReady=false ... cni plugin not initialized`. kubelet gates node readiness on the CRI
reporting a **usable CNI** — the CNI isn't installed or its config hasn't landed.

## Problem

- Node condition `Ready=False`, reason `KubeletNotReady`.
- kubelet log: `"Container runtime network not ready" networkReady="NetworkReady=false
  reason:NetworkPluginNotReady message:Network plugin returns error: cni plugin not initialized"`.

## Context

- Applies to Kubernetes **1.29–1.35**. **Expected transient** right after `kubeadm init`/join
  until the CNI comes up; **persistent** = the CNI is broken.

## Diagnostics

- **Check the CNI config landed:** `ls /etc/cni/net.d` should be non-empty; `crictl info` shows
  the network status. Empty means the CNI DaemonSet hasn't written its config.
- **Check the CNI pods:** the CNI DaemonSet (Calico/Cilium) must be `Ready` — a crashlooping or
  `Pending` CNI pod (RBAC, image pull, node selector, kernel floor) leaves the node NotReady.
  See [[COMPONENT-CALICO]] / [[COMPONENT-CILIUM]] and [[TROUBLE-CALICO_NODE_ISSUES]].
- **Order:** the control-plane node is NotReady until its CNI is up — this is normal during
  bootstrap; only investigate if it doesn't clear once the CNI pods are Ready.

## Known Issues

- A half-installed CNI (config present but agent crashlooping) shows the same message — always
  check both the config file **and** the CNI pod health.

## References

- k8s issue #125267 (above); CNIs: [[COMPONENT-CALICO]], [[COMPONENT-CILIUM]]; Calico node
  triage: [[TROUBLE-CALICO_NODE_ISSUES]].

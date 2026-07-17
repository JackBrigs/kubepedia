---
id: TROUBLE-K8S_KUBEPROXYVERSION_FIELD_REMOVED
type: troubleshooting
title: "node.status kubeProxyVersion is empty — field deprecated and no longer populated (K8s 1.33)"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: ">=1.33 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: confirmed
aliases:
  - kubeProxyVersion empty
  - node kubeProxyVersion not populated
  - DisableNodeKubeProxyVersion
  - kubectl node kube-proxy version blank
  - status.nodeInfo.kubeProxyVersion deprecated
tags:
  - kubernetes
  - troubleshooting
  - kube-proxy
  - upgrade
sources:
  - type: code
    path: keps/sig-network/4004-deprecate-kube-proxy-version
    url: https://github.com/kubernetes/enhancements/tree/master/keps/sig-network/4004-deprecate-kube-proxy-version
    note: "DisableNodeKubeProxyVersion feature gate on-by-default v1.33 (kep.yaml); field no longer populated"
relations:
  - type: see_also
    target: CONCEPT-K8S_UPGRADE_SILENT_CHANGES
  - type: see_also
    target: CONCEPT-KUBE_PROXY
  - type: see_also
    target: CONCEPT-K8S_FEATURE_GATES
---

# node.status kubeProxyVersion is empty — field deprecated and no longer populated (K8s 1.33)

## Summary

`Node.status.nodeInfo.kubeProxyVersion` was **inaccurate by design** (the kubelet reported its own
version, not kube-proxy's) and has been **deprecated**; the `DisableNodeKubeProxyVersion` feature gate
is **on by default from K8s 1.33**, so the field is **no longer populated**. Dashboards, inventory
scripts, or CMDB integrations that read it get an empty value after the cluster reaches 1.33 (Kubespray
v2.31.0 sits at K8s 1.33+). Nothing is broken in the cluster — only tooling that trusted a field that
was never reliable.

## Problem

- `kubectl get node -o jsonpath='{.status.nodeInfo.kubeProxyVersion}'` returns **empty**.
- A monitoring/inventory tool that displayed "kube-proxy version" now shows blank / null for all nodes.
- Alerts or reports keyed on that field fire falsely.

## Context

- The `DisableNodeKubeProxyVersion` gate went **on by default in K8s 1.33** (`keps/sig-network/4004-...`).
  In the Kubespray range that is **v2.31.0** (K8s 1.33+); earlier Kubespray tags (K8s ≤1.32) still
  populate it.
- Why: the field was set by the **kubelet** to the kubelet/node version, never to the actual kube-proxy
  version — it was misleading and is being removed rather than fixed.

## Diagnostics

- Confirm the K8s minor: `kubectl version` — if the server is **≥1.33**, an empty `kubeProxyVersion` is
  **expected**, not a fault.
- Verify the real kube-proxy version another way: `kubectl -n kube-system get ds kube-proxy -o
  jsonpath='{.spec.template.spec.containers[0].image}'` (image tag), or `kubectl -n kube-system exec
  <kube-proxy-pod> -- kube-proxy --version` ([[CONCEPT-KUBE_PROXY]]).

## Known Issues

- **Fix:** update tooling to **stop reading** `status.nodeInfo.kubeProxyVersion`; derive the version
  from the kube-proxy DaemonSet image or `kube-proxy --version` instead.
- **Cilium/kube-proxy-free clusters:** the field was already meaningless there (no kube-proxy) — this
  just makes it empty everywhere consistently.
- This is a **silent, non-breaking** change ([[CONCEPT-K8S_UPGRADE_SILENT_CHANGES]]); the risk is only
  false alerts from tooling. There is no supported way to keep populating it long-term (the gate exists
  transitionally — [[CONCEPT-K8S_FEATURE_GATES]]).

## References

- `keps/sig-network/4004-deprecate-kube-proxy-version` (kep.yaml: gate on-by-default v1.33).
  Silent-change list [[CONCEPT-K8S_UPGRADE_SILENT_CHANGES]]; kube-proxy [[CONCEPT-KUBE_PROXY]];
  feature gates [[CONCEPT-K8S_FEATURE_GATES]].

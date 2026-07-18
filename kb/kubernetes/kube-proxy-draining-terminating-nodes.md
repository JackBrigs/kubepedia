---
id: CONCEPT-K8S_KUBE_PROXY_DRAINING_NODES
type: concept
title: "kube-proxy routes LB traffic away from terminating nodes (GA 1.31)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.30 <=1.35"
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - KubeProxyDrainingTerminatingNodes
  - kube-proxy terminating node traffic
  - dropped connections rolling upgrade loadbalancer
  - externalTrafficPolicy Cluster terminating
tags:
  - kubernetes
  - kube-proxy
  - networking
sources:
  - type: code
    path: keps/sig-network/3836-kube-proxy-improved-ingress-connectivity-reliability
    url: https://github.com/kubernetes/enhancements/tree/master/keps/sig-network/3836-kube-proxy-improved-ingress-connectivity-reliability
    note: "kep.yaml: alpha 1.28, beta 1.30, stable 1.31"
relations:
  - type: see_also
    target: CONCEPT-KUBE_PROXY
  - type: see_also
    target: CONCEPT-K8S_UPGRADE_SILENT_CHANGES
  - type: see_also
    target: PRACTICE-RUNBOOK_NODE_MAINTENANCE
---

# kube-proxy routes LB traffic away from terminating nodes (GA 1.31)

## Summary

`kube-proxy` now steers external LoadBalancer traffic **away from nodes that are terminating or
not-ready**, so rolling node operations drop fewer connections. `KubeProxyDrainingTerminatingNodes`
reached **beta in 1.30** and **GA in 1.31** (Kubespray v2.29.0+). It specifically improves the
`externalTrafficPolicy: Cluster` case during node drains/upgrades — an automatic reliability win with
no config to set.

## Context

- Milestone (`keps/sig-network/3836-...` kep.yaml): alpha **1.28**, beta **1.30**, stable **1.31**.
- **What changes:** with `externalTrafficPolicy: Cluster`, a node that is **terminating** (has a
  deletion timestamp) is used as an LB target **only if no ready non-terminating endpoints remain** —
  so an external LB health-check race during drain no longer blackholes traffic to a departing node.
- **Operator impact (positive):** smoother node maintenance and upgrades ([[PRACTICE-RUNBOOK_NODE_MAINTENANCE]],
  [[CONCEPT-KUBE_PROXY]]); no action required. CNIs in kube-proxy-replacement mode implement their own
  equivalent — this KEP is about the in-tree kube-proxy path.

## References

- `keps/sig-network/3836-kube-proxy-improved-ingress-connectivity-reliability` (kep.yaml GA 1.31).
  kube-proxy [[CONCEPT-KUBE_PROXY]]; node maintenance [[PRACTICE-RUNBOOK_NODE_MAINTENANCE]]; silent
  changes [[CONCEPT-K8S_UPGRADE_SILENT_CHANGES]].

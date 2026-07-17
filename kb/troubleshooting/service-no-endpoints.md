---
id: TROUBLE-SERVICE_NO_ENDPOINTS
type: troubleshooting
title: "Service unreachable / has no endpoints"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: verified
aliases:
  - service no endpoints
  - cannot reach service
  - service not working
  - connection refused clusterip
  - selector does not match pods
  - endpoints empty
  - endpointslice empty
tags:
  - troubleshooting
  - service
  - networking
  - kube-proxy
sources:
  - type: docs
    path: Kubernetes debug services
    url: https://kubernetes.io/docs/tasks/debug/debug-application/debug-service/
    note: "Service → EndpointSlice population depends on selector match + pod readiness"
relations:
  - type: see_also
    target: PRACTICE-SERVICE_NETWORKING_DEBUG
  - type: see_also
    target: CONCEPT-KUBE_PROXY
  - type: see_also
    target: CONCEPT-TROUBLESHOOTING_MAP
---

# Service unreachable / has no endpoints

## Summary

A `ClusterIP` Service works only if it has **endpoints** — ready pods whose labels match
its **selector**. The most common "service doesn't work" cause is an **empty endpoint
list**: the selector matches nothing, or the matched pods aren't **Ready**. If endpoints
*are* present but traffic still fails, the problem moves to kube-proxy/CNI or NetworkPolicy.

## Problem

Connecting to a Service (ClusterIP:port, or `svc.ns.svc.cluster.local`) times out or gives
`connection refused`, while the backing pods themselves are up.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`.
- Traffic path: **Service → EndpointSlice (ready pods) → kube-proxy/CNI rules → pod**. A
  break anywhere makes the Service unreachable; isolate *which* hop.

## Diagnostics

- **Endpoints first:** `kubectl get endpointslices -l kubernetes.io/service-name=<svc>`
  (or `kubectl get endpoints <svc>`). **Empty = selector/readiness problem**; populated =
  a downstream (proxy/policy) problem.
- **Selector match:** `kubectl describe svc <svc>` (its `Selector`) vs
  `kubectl get pods --show-labels` — do any pods' labels match **exactly**?
- **Readiness:** `kubectl get pods` — endpoints only include **Ready** pods; a failing
  readiness probe keeps a running pod out of the endpoint list.
- **Ports:** confirm the Service `targetPort` matches the container's actual listen port.
- **From inside the cluster:** `kubectl run -it --rm netcheck --image=busybox:1.36 -- wget
  -qO- <svc>.<ns>:<port>` — cluster-DNS + connectivity in one shot.

## Known Issues

**Endpoints empty:**

- **Selector mismatch** — the Service `selector` doesn't match the pods' labels (typo,
  wrong label, wrong namespace). Fix the selector or the pod labels.
- **No Ready pods** — pods exist but fail readiness → not added to endpoints. Fix the
  readiness probe / the app.
- **Wrong `targetPort`** — endpoints exist but point at a port nothing listens on.

**Endpoints present but unreachable:**

- **kube-proxy not programming rules** — kube-proxy pod down, or in a mode that isn't
  working ([[CONCEPT-KUBE_PROXY]]); with a **kube-proxy-free CNI** (Cilium eBPF) the CNI
  owns Service routing — check the CNI, not kube-proxy.
- **NetworkPolicy** — a default-deny or restrictive policy blocks traffic to the pods;
  check policies in the target namespace.
- **Cross-node path broken** — overlay/firewall (VXLAN, ports) —
  [[TROUBLE-FIREWALL_PORTS_BLOCKED]], [[TROUBLE-VXLAN_MTU_MISMATCH]].

**Gotchas:**

- `type: LoadBalancer`/NodePort still need working endpoints first — a `<pending>` external
  IP is a different problem ([[TROUBLE-METALLB_SERVICE_PENDING]]).
- **Headless** Services (`clusterIP: None`) return pod IPs directly via DNS — "no
  ClusterIP" is expected there, not a fault.
- `externalTrafficPolicy: Local` drops traffic on nodes with no local pod — expected, not
  a bug.

## References

- Kubernetes debug-service. Runbook: [[PRACTICE-SERVICE_NETWORKING_DEBUG]]; proxy:
  [[CONCEPT-KUBE_PROXY]]; symptom map: [[CONCEPT-TROUBLESHOOTING_MAP]].

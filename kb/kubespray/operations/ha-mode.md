---
id: PRACTICE-HA_MODE
type: best_practice
title: High-availability endpoints (etcd and kube-apiserver)
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: 2026-07-16
confidence: verified
aliases:
  - ha mode
  - ha endpoints
  - apiserver load balancing
tags:
  - ha
  - load-balancer
  - operations
sources:
  - type: docs
    path: docs/operations/ha-mode.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/operations/ha-mode.md
    note: "etcd HA; localhost vs external apiserver load balancing"
relations:
  - type: see_also
    target: VARIABLE-LOADBALANCER_APISERVER_LOCALHOST
  - type: see_also
    target: COMPONENT-KUBE_VIP
---

# High-availability endpoints (etcd and kube-apiserver)

## Summary

Two endpoints need to be highly available: the **etcd cluster** and the
**kube-apiserver**. etcd is HA once it has multiple members; the API server needs
a load balancer in front of it. Kubespray's default is a per-node localhost load
balancer.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`.
- etcd HA: the API servers are configured with the full list of etcd peers, so a
  multi-member (e.g. 3-node) etcd cluster is already HA.
- kube-apiserver HA: needs a reverse proxy / load balancer.

## Implementation

**Localhost load balancing (default).** Each non-control-plane node runs an
nginx-based proxy to reach the API servers, controlled by
[[VARIABLE-LOADBALANCER_APISERVER_LOCALHOST]] (default `true`, or `false` when an
external `loadbalancer_apiserver` is defined). The local LB port defaults to
`kube_apiserver_port`. Kubespray configures kubelet and kube-proxy on non-control
nodes to use this local endpoint. It adds extra API health checks but avoids
external LB infrastructure.

**External load balancer / VIP.** If you do not use the localhost LB, provide an
external LB or use [[COMPONENT-KUBE_VIP]] for a control-plane virtual IP.
Otherwise Kubespray configures only a non-HA endpoint pointing at the first
`kube_control_plane` node's `access_ip`.

## Compatibility

- Verified against `v2.31.0` docs; the HA model (etcd peer list + localhost vs
  external LB) is stable across the indexed range.

## References

- `docs/operations/ha-mode.md` (tag `v2.31.0` `1c9add4`).
- Related: `loadbalancer_apiserver_localhost`, `loadbalancer_apiserver_port`,
  `kube_apiserver_port`.

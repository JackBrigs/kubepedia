---
id: CONCEPT-SERVICE_EXPOSURE
type: concept
title: "Exposing services in Kubespray (kube-vip, MetalLB, Cilium LB, Ingress)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - service exposure
  - how to expose services
  - loadbalancer options bare metal
  - kube-vip vs metallb vs cilium
  - external ip bare metal
tags:
  - networking
  - load-balancer
  - ingress
  - service
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "kube_vip / metallb / cilium LB enable flags (tag v2.31.0)"
relations:
  - type: see_also
    target: TROUBLE-METALLB_SERVICE_PENDING
  - type: see_also
    target: CONCEPT-CILIUM_LOADBALANCING
  - type: see_also
    target: TROUBLE-KUBE_VIP_VIP_NOT_UP
---

# Exposing services in Kubespray (kube-vip, MetalLB, Cilium LB, Ingress)

## Summary

On bare metal there is no cloud load balancer, so Kubespray offers several ways to expose
Services. They solve **different** problems — a control-plane VIP, `type: LoadBalancer`
external IPs, and L7 HTTP routing — and some overlap (don't run two LoadBalancer
controllers at once). This map picks the right tool.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`. All options are opt-in.
- Two questions decide the choice: **what** are you exposing (the API / a
  `LoadBalancer` Service / an HTTP route) and **how** is it announced (L2/ARP vs BGP).

## Implementation

**Control-plane API VIP → kube-vip:**

- `kube_vip_enabled` + `kube_vip_controlplane_enabled` — a single virtual IP for the API
  server (HA endpoint), announced via ARP or BGP ([[TROUBLE-KUBE_VIP_VIP_NOT_UP]]).
- kube-vip can **also** do Service LoadBalancer (`kube_vip_services_enabled`), but its
  primary role in Kubespray is the API VIP.

**`type: LoadBalancer` external IPs → MetalLB *or* Cilium LB (pick one):**

- **MetalLB** — CNI-agnostic; L2 (needs `kube_proxy_strict_arp: true`) or BGP; address
  pools ([[TROUBLE-METALLB_SERVICE_PENDING]]).
- **Cilium LB** — only with the Cilium CNI; LB IPAM + L2 announcements (a direct MetalLB
  L2 replacement) or BGP ([[CONCEPT-CILIUM_LOADBALANCING]]).
- **Do not run MetalLB and Cilium L2/BGP together** — two controllers announcing the same
  VIPs conflict.

**HTTP(S) routing (L7) → Ingress / Gateway API:**

- Kubespray no longer bundles **ingress-nginx** (removed in `v2.31.0` —
  [[COMPONENT-INGRESS_NGINX]]); deploy an ingress controller yourself, or use Cilium's
  Gateway API / Ingress support.
- The in-tree **ALB** controller (`ingress_alb_enabled`) is AWS-specific.
- Ingress needs an external IP to land on — typically a `LoadBalancer` Service from
  MetalLB/Cilium, closing the loop.

## Compatibility

- **Decision shortcut:** API HA → kube-vip; bare-metal `LoadBalancer` IPs → MetalLB
  (any CNI) or Cilium LB (Cilium only); HTTP routing → an ingress controller (BYO) landing
  on a LoadBalancer IP.
- L2 vs BGP is the same trade-off across MetalLB and Cilium: L2 needs one shared segment;
  BGP needs peered routers but scales across subnets.
- With Cilium eBPF kube-proxy replacement, Cilium already owns Service datapath — using
  Cilium LB there is the natural fit ([[CONCEPT-CILIUM_LOADBALANCING]]).

## References

- kube-vip / MetalLB / Cilium LB enable flags at tag `v2.31.0`. See
  [[TROUBLE-KUBE_VIP_VIP_NOT_UP]], [[TROUBLE-METALLB_SERVICE_PENDING]],
  [[CONCEPT-CILIUM_LOADBALANCING]], [[COMPONENT-INGRESS_NGINX]].

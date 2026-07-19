---
id: TROUBLE-METALLB_L2_STRICTARP_UNREACHABLE
type: troubleshooting
title: "MetalLB L2: EXTERNAL-IP assigned but unreachable — kube-proxy IPVS needs strictARP"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-19"
confidence: confirmed
aliases:
  - metallb ip assigned but not reachable
  - metallb l2 no arp reply
  - ipvs strictarp metallb
  - loadbalancer ip times out
  - kube_proxy_strict_arp metallb
tags:
  - troubleshooting
  - networking
  - metallb
  - kube-proxy
  - interaction
sources:
  - type: code
    path: roles/network_plugin / kube-proxy strictARP
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "kube_proxy_strict_arp must be true for MetalLB L2 when kube_proxy_mode=ipvs"
  - type: external
    path: MetalLB IPVS / strictARP requirement
    url: https://metallb.universe.tf/installation/#preparation
    note: "with IPVS kube-proxy, strictARP must be enabled or L2 speaker ARP is shadowed by kube-ipvs0"
relations:
  - type: see_also
    target: VARIABLE-KUBE_PROXY_STRICT_ARP
  - type: see_also
    target: COMPONENT-METALLB
  - type: see_also
    target: CONCEPT-KUBE_PROXY
  - type: see_also
    target: TROUBLE-METALLB_SERVICE_PENDING
  - type: see_also
    target: CONCEPT-COMPONENT_INTERACTION_FAILURES
---

# MetalLB L2: EXTERNAL-IP assigned but unreachable — kube-proxy IPVS needs strictARP

## Summary

A classic **two-component seam**: MetalLB assigns the LoadBalancer an `EXTERNAL-IP` (so it looks
healthy — not `<pending>`, unlike [[TROUBLE-METALLB_SERVICE_PENDING]]), but external clients **can't
reach it**. In **L2 mode with kube-proxy in IPVS**, the kube-proxy dummy interface `kube-ipvs0` binds
service IPs and answers ARP for them, **shadowing** MetalLB speaker's gratuitous ARP — so the LB IP is
never correctly ARP-resolved on the LAN. The fix is **`strictARP`**, which Kubespray exposes as
`kube_proxy_strict_arp` ([[VARIABLE-KUBE_PROXY_STRICT_ARP]]).

## Problem

- `kubectl get svc` shows a real `EXTERNAL-IP` (not `<pending>`), but `curl`/ping to it from **off the
  cluster** times out or is intermittent.
- ARP for the LB IP resolves to the **wrong MAC** (a node's `kube-ipvs0`, or flapping), not the MetalLB
  speaker's node.

## Context

- Applies across **v2.27.0–v2.31.0**. Triggered specifically by **MetalLB L2 + `kube_proxy_mode: ipvs`**
  ([[CONCEPT-KUBE_PROXY]], [[COMPONENT-METALLB]]).
- **Why:** IPVS mode creates the `kube-ipvs0` dummy interface and binds all Service (including
  LoadBalancer) IPs to it. Without `strictARP`, the node replies to ARP requests for those IPs on every
  interface, so the LAN sees ARP answers from nodes that shouldn't own the LB IP — competing with
  MetalLB's L2 speaker. Result: the IP is assigned but not reliably reachable.
- **BGP mode is different:** this specific trap is L2-mode. BGP-session issues are
  [[TROUBLE-METALLB_BGP_SESSION_DOWN]].

## Diagnostics

```bash
kubectl get svc <svc>                                  # EXTERNAL-IP present (not <pending>)
# from a LAN host: who answers ARP for the LB IP?
arping -I <iface> <EXTERNAL-IP>                        # expect ONE consistent MAC (speaker node)
# strictARP currently on?
kubectl -n kube-system get cm kube-proxy -o yaml | grep -i strictARP
```

`strictARP: false` (or absent) with IPVS mode + an unreachable LB IP = this issue.

## Known Issues

- **Fix (Kubespray):** set **`kube_proxy_strict_arp: true`** ([[VARIABLE-KUBE_PROXY_STRICT_ARP]]) and
  re-converge, so kube-proxy only answers ARP for IPs actually local to the interface — MetalLB's L2
  speaker then owns the LB IP's ARP. This is a **required** setting for MetalLB L2 on IPVS.
- **Verify after:** the kube-proxy ConfigMap shows `strictARP: true`, kube-proxy pods restarted, and
  `arping` returns a single stable MAC.
- **Alternative:** MetalLB **BGP** mode (no ARP dependency), or a CNI-native LB (Cilium
  `l2announcements` / LB-IPAM) instead of MetalLB.

## References

- Kubespray `kube_proxy_strict_arp`; MetalLB IPVS/strictARP preparation. Variable
  [[VARIABLE-KUBE_PROXY_STRICT_ARP]]; component [[COMPONENT-METALLB]]; kube-proxy
  [[CONCEPT-KUBE_PROXY]]; pending-IP case [[TROUBLE-METALLB_SERVICE_PENDING]]; interaction spine
  [[CONCEPT-COMPONENT_INTERACTION_FAILURES]].

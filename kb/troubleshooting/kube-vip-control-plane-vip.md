---
id: TROUBLE-KUBE_VIP_CONTROL_PLANE_VIP
type: troubleshooting
title: "kube-vip: control-plane VIP not reachable / not failing over"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.8.0 <=1.2.1"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - kube-vip vip not working
  - control plane vip unreachable
  - kube-vip leader election
  - kube-vip arp bgp
tags:
  - troubleshooting
  - kube-vip
  - control-plane
  - ha
  - networking
sources:
  - type: docs
    path: kube-vip documentation
    url: https://kube-vip.io/docs/
    note: "ARP vs BGP, leader election, control-plane VIP"
relations:
  - type: see_also
    target: COMPONENT-KUBE_VIP
  - type: see_also
    target: TROUBLE-FIREWALL_PORTS_BLOCKED
---

# kube-vip: control-plane VIP not reachable / not failing over

## Summary

The HA control-plane **VIP** is unreachable, or it doesn't move when the leader node dies.
kube-vip advertises the VIP via **ARP (layer2)** or **BGP** and picks a holder via **leader
election**; the failure is usually a mode/network mismatch or a leader-election problem.

## Problem

- `kubectl`/kubelets can't reach the API VIP (timeouts).
- On leader node failure the VIP doesn't migrate; API stays down until manual action.
- VIP flaps between nodes.

## Context

- Applies to kube-vip **0.8–1.2.1** (base ≤1.0.3 — [[COMPONENT-KUBE_VIP]]). Runs as a static
  pod / DaemonSet on control-plane nodes.

## Diagnostics

- **ARP (layer2) mode:** the VIP must be in the **same L2 subnet** as the nodes; the network
  must allow **gratuitous ARP**. Many clouds block ARP-based VIPs → use BGP or a cloud LB
  instead. Check that only one node answers ARP for the VIP.
- **BGP mode:** the BGP peer/ASN config must be correct and the session **Established** —
  verify with the upstream router; the VIP `/32` should be advertised from the current leader.
- **Leader election:** kube-vip uses a lease; check the kube-vip pod logs on each node for who
  holds leadership. A node that can't reach the API server can't participate — a chicken/egg
  during a full control-plane outage.
- **Ports/firewall:** API port (6443) to the VIP must be open; BGP needs TCP/179
  ([[TROUBLE-FIREWALL_PORTS_BLOCKED]]).

## Known Issues

- Mixing kube-vip ARP with a cloud that filters MAC/ARP silently fails — confirm the platform
  supports layer2 VIPs before choosing ARP mode.

## References

- kube-vip docs (above); component: [[COMPONENT-KUBE_VIP]]; ports:
  [[TROUBLE-FIREWALL_PORTS_BLOCKED]].

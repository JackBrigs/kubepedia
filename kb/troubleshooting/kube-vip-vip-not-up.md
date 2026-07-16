---
id: TROUBLE-KUBE_VIP_VIP_NOT_UP
type: troubleshooting
title: "kube-vip control-plane VIP does not come up"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube-vip VIP not working
  - control plane VIP down
  - kube_vip_arp_enabled
  - kube_vip_bgp_enabled
  - kube_vip_controlplane_enabled
  - kube-vip no mode selected
  - apiserver VIP unreachable
tags:
  - troubleshooting
  - kube-vip
  - control-plane
  - load-balancer
  - ha
sources:
  - type: code
    path: roles/kubernetes/node/tasks/loadbalancer/kube-vip.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/tasks/loadbalancer/kube-vip.yml
    note: "kube-vip manifest rendering + BGP source assert (tag v2.31.0)"
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "kube_vip_* defaults (tag v2.31.0)"
relations:
  - type: see_also
    target: COMPONENT-KUBE_VIP
  - type: see_also
    target: TROUBLE-KUBE_VIP_CAPS_VERSION
  - type: see_also
    target: VARIABLE-KUBE_VIP_ADDRESS
---

# kube-vip control-plane VIP does not come up

## Summary

kube-vip provides a virtual IP for the control plane (and optionally Services). It needs
an explicit **mode** — **ARP** (layer-2) or **BGP** (routed) — to advertise the VIP. The
most common failure is enabling kube-vip and a VIP address but selecting **no mode** (or
the wrong one for the network), so the VIP is configured but never reachable. All the
knobs are **off by default**, so a working setup requires several deliberate settings.

## Problem

The control-plane VIP (`kube_vip_address`) is unreachable: `kubectl`/join through the VIP
times out, the API endpoint doesn't answer on the VIP even though individual
control-plane node IPs work, or the VIP never appears on any node's interface.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`. kube-vip runs as a static pod on
  control-plane nodes (`roles/kubernetes/node/tasks/loadbalancer/kube-vip.yml`).
- Relevant defaults (all **off/empty** unless set):
  - `kube_vip_enabled: false` — master switch.
  - `kube_vip_address:` — the VIP (must be set, and free on the subnet).
  - `kube_vip_controlplane_enabled: false` — advertise the **API** VIP.
  - `kube_vip_services_enabled: false` — VIP-based Service LB.
  - `kube_vip_arp_enabled: false` — **ARP/L2** mode.
  - `kube_vip_bgp_enabled: false` — **BGP** mode.
  - `kube_vip_interface:` — interface to host the VIP (auto if empty).
  - `kube_vip_lb_fwdmethod: local` — forwarding method (`masquerade` switches to the
    `-iptables` image variant).

## Diagnostics

- kube-vip pod: `kubectl -n kube-system get pods -l name=kube-vip -o wide` and
  `kubectl -n kube-system logs <kube-vip-pod>` — the logs state the elected leader and
  the advertised mode.
- VIP presence: on the leader node `ip addr | grep <kube_vip_address>` (ARP mode assigns
  the VIP to an interface).
- Mode sanity: confirm exactly one of `kube_vip_arp_enabled` / `kube_vip_bgp_enabled` is
  true and matches your network (L2 same-subnet → ARP; routed/L3 → BGP).
- Reachability: `nc -vz <kube_vip_address> 6443` from another node.

## Known Issues

- **No mode selected:** `kube_vip_enabled: true` with a VIP but **neither**
  `kube_vip_arp_enabled` **nor** `kube_vip_bgp_enabled` → the VIP is never advertised.
  Enable the mode that fits your network.
- **Control-plane VIP not enabled:** set `kube_vip_controlplane_enabled: true` for the
  API VIP (separate from `kube_vip_services_enabled`).
- **Wrong mode for the network:** ARP requires all control-plane nodes on the **same L2
  subnet** as the VIP; across subnets/routers use BGP with your routers peered.
- **Interface not auto-detected:** set `kube_vip_interface` explicitly (multi-NIC or
  non-default interface names).
- **BGP mis-config:** Kubespray asserts you set **only one** of `kube_vip_bgp_sourceip`
  or `kube_vip_bgp_sourceif` (`fail_msg: "kube-vip allows only one of …"`); setting both
  aborts the run.
- **VIP address in use / not routable:** pick a free IP on the right subnet; a duplicate
  or off-subnet VIP won't answer.
- Version/capabilities mismatches are a separate failure mode — see
  [[TROUBLE-KUBE_VIP_CAPS_VERSION]].

## References

- kube-vip loadbalancer task + `kube_vip_*` defaults at tag `v2.31.0`.
- Component: [[COMPONENT-KUBE_VIP]]; VIP address var: [[VARIABLE-KUBE_VIP_ADDRESS]].

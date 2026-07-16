---
id: TROUBLE-METALLB_SERVICE_PENDING
type: troubleshooting
title: "MetalLB: LoadBalancer service stuck EXTERNAL-IP <pending>"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - metallb pending external-ip
  - loadbalancer service pending
  - metallb no ip assigned
  - kube_proxy_strict_arp metallb
  - metallb address pool
  - metallb layer2 not working
tags:
  - troubleshooting
  - metallb
  - load-balancer
  - networking
sources:
  - type: docs
    path: docs/ingress/metallb.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/ingress/metallb.md
    note: "MetalLB prerequisites (kube_proxy_strict_arp), pools, layer2/BGP (tag v2.31.0)"
  - type: code
    path: roles/kubernetes-apps/metallb/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/metallb/defaults/main.yml
    note: "metallb_enabled / metallb_speaker_enabled / metallb_namespace defaults (tag v2.31.0)"
relations:
  - type: see_also
    target: COMPONENT-METALLB
  - type: see_also
    target: TROUBLE-FIREWALL_PORTS_BLOCKED
  - type: see_also
    target: TROUBLE-NFTABLES_KERNEL_TOO_LOW
---

# MetalLB: LoadBalancer service stuck EXTERNAL-IP <pending>

## Summary

A `type: LoadBalancer` Service sits at `EXTERNAL-IP <pending>` when MetalLB has nothing
to hand out or can't announce. In Kubespray the two most common causes are (1) the
**Layer2 prerequisite** `kube_proxy_strict_arp: true` isn't set, and (2) **no address
pool** is configured or the pool is exhausted/not attached to a mode. MetalLB is
disabled by default, so a working setup needs several deliberate settings.

## Problem

`kubectl get svc` shows a LoadBalancer service with `EXTERNAL-IP` = `<pending>`
indefinitely; the service never gets an IP, so it's unreachable from outside the cluster.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`. Defaults: `metallb_enabled: false`,
  `metallb_speaker_enabled: "{{ metallb_enabled }}"`, `metallb_namespace:
  metallb-system`. Default mode is **Layer2** (BGP optional).
- **Layer2 prerequisite:** `kube_proxy_strict_arp: true` — required so kube-proxy's
  `kube-ipvs0` interface doesn't answer ARP for the VIPs. Without it, Layer2
  announcement doesn't work.
- Address pools are declared in `metallb_config.address_pools` and attached to a mode
  (`metallb_config.layer2: [<pool>]` or a BGP block).

## Diagnostics

- MetalLB pods: `kubectl -n metallb-system get pods` — the **controller** (allocates
  IPs) and **speaker** (announces) must be Running.
- Service events: `kubectl describe svc <svc>` — MetalLB posts the reason
  (`no available IPs`, `no matching IPAddressPool`, etc.).
- Pools: `kubectl -n metallb-system get ipaddresspools,l2advertisements` — confirm a pool
  exists, has free range, and (Layer2) an L2Advertisement references it.
- speaker logs: `kubectl -n metallb-system logs ds/speaker` for announce/ARP errors.

## Known Issues

**Fixes — set in inventory, re-run the metallb role:**

- **Enable MetalLB:** `metallb_enabled: true` (also enables the speaker).
- **Layer2 prerequisite:** `kube_proxy_strict_arp: true` — without it Layer2 silently
  fails to announce. Applies to the kube-proxy config, so it needs kube-proxy re-applied.
- **Define a pool:** add `metallb_config.address_pools.<name>.ip_range` (range or CIDR)
  and attach it: `metallb_config.layer2: [<name>]` for Layer2 (or a BGP peer block).
- **Pool exhausted:** each LoadBalancer IP consumes one address — size the range for the
  number of services, or free unused ones.
- **`auto_assign: false` pools:** you **must** set `spec.loadBalancerIP` on the service
  explicitly, or it stays pending (that pool won't auto-allocate).
- **avoid_buggy_ips:** with it true, `.0`/`.255` are skipped — don't count on them.

**Gotchas:**

- Firewall: MetalLB speaker needs `7472` (metrics) and `7946` TCP/UDP (memberlist) open
  between nodes — see [[TROUBLE-FIREWALL_PORTS_BLOCKED]].
- The VIP range must be **on the L2 network** and free (Layer2); for routed setups use
  BGP with peers configured.
- If you also run Calico BGP, advertise the pool
  (`calico_advertise_service_loadbalancer_ips`).

## References

- `docs/ingress/metallb.md` (prerequisites, pools, layer2/BGP) and metallb defaults at
  tag `v2.31.0`. Component: [[COMPONENT-METALLB]].

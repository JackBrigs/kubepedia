---
id: TROUBLE-ARP_NEIGH_TABLE_OVERFLOW
type: troubleshooting
title: "Neighbour table overflow at scale — raise net.ipv4.neigh gc_thresh (ARP/NDP cache)"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-19"
confidence: confirmed
aliases:
  - neighbour table overflow
  - arp_cache neighbor table overflow
  - gc_thresh3 kubernetes
  - intermittent connectivity large cluster
  - net.ipv4.neigh.default.gc_thresh
  - ndp table full ipv6
tags:
  - troubleshooting
  - networking
  - scale
  - kernel
sources:
  - type: external
    path: Linux neighbour table (gc_thresh1/2/3)
    url: https://www.kernel.org/doc/Documentation/networking/ip-sysctl.txt
    note: "gc_thresh1 min, gc_thresh2 soft, gc_thresh3 hard cap of the ARP/NDP cache; overflow drops packets"
relations:
  - type: see_also
    target: CONCEPT-SCALE_LIMITS
  - type: see_also
    target: CONCEPT-CLUSTER_NETWORKING
  - type: see_also
    target: PRACTICE-KERNEL_REQUIREMENTS
  - type: see_also
    target: TROUBLE-CONNTRACK_TABLE_FULL
---

# Neighbour table overflow at scale — raise net.ipv4.neigh gc_thresh (ARP/NDP cache)

## Summary

A large, flat cluster (many nodes/pods on the same L2, or a CNI with lots of direct routes/peers) can
exhaust the kernel **neighbour (ARP/NDP) cache**. Once it hits the hard cap `gc_thresh3`, the kernel
logs **`neighbour: arp_cache: neighbor table overflow!`** and **drops packets** — intermittent,
maddening connectivity loss that no single component's logs explain. The fix is raising the
`net.ipv4.neigh.default.gc_thresh*` sysctls (and the IPv6 `net.ipv6.neigh.default.*` for dual-stack).

## Problem

- `dmesg` / kernel log spams `neighbour: arp_cache: neighbor table overflow!` (or `ndisc_cache` for
  IPv6).
- Pod-to-pod or node-to-node traffic is **intermittently dropped**; latency spikes; some flows work,
  others don't, seemingly at random — and it correlates with cluster size/connection count.

## Context

- Applies across **v2.27.0–v2.31.0**; a **scale** failure, not a version bug ([[CONCEPT-SCALE_LIMITS]]).
- **Why:** the ARP/NDP cache has three thresholds — `gc_thresh1` (below which entries are never GC'd,
  default 128), `gc_thresh2` (soft cap, default 512), `gc_thresh3` (hard cap, default 1024). A node that
  must track more than ~`gc_thresh3` neighbours (large flat networks, many pods per node with
  routed/overlay CNIs, Calico/kube-router with many peers) overflows the hard cap and drops.
- More likely with **flat L2 / routed** dataplanes than with a tunnel that hides remote pods behind a
  single node IP; dual-stack doubles the pressure (separate v4/v6 caches).

## Diagnostics

```bash
# current table size vs the hard cap
ip -s neigh show | wc -l
sysctl net.ipv4.neigh.default.gc_thresh1 net.ipv4.neigh.default.gc_thresh2 net.ipv4.neigh.default.gc_thresh3
dmesg -T | grep -i 'neighbour table overflow'
```

Table count approaching `gc_thresh3` + the dmesg line = this issue.

## Known Issues

- **Fix — raise the thresholds** on every affected node (persist via `/etc/sysctl.d/`), scaled to the
  neighbour count you expect:

  ```
  net.ipv4.neigh.default.gc_thresh1 = 4096
  net.ipv4.neigh.default.gc_thresh2 = 8192
  net.ipv4.neigh.default.gc_thresh3 = 16384
  # dual-stack: mirror for IPv6
  net.ipv6.neigh.default.gc_thresh1 = 4096
  net.ipv6.neigh.default.gc_thresh2 = 8192
  net.ipv6.neigh.default.gc_thresh3 = 16384
  ```

  Apply with `sysctl --system`. In Kubespray, add these to your node sysctl configuration so they
  survive re-converge and reboots ([[PRACTICE-KERNEL_REQUIREMENTS]]) — don't just set them live.
- **Size it right:** the hard cap should comfortably exceed peak neighbours (roughly nodes × pods-seen
  + gateways); leave headroom.
- **Reduce pressure alternatively:** a dataplane that tunnels/encapsulates remote pods (or aggregates
  routes) shrinks the neighbour set — a design lever if bumping sysctls isn't enough.

## References

- Kernel `ip-sysctl` neighbour GC thresholds. Scale spine [[CONCEPT-SCALE_LIMITS]]; networking
  [[CONCEPT-CLUSTER_NETWORKING]]; kernel prereqs [[PRACTICE-KERNEL_REQUIREMENTS]]; the other classic
  scale table [[TROUBLE-CONNTRACK_TABLE_FULL]].

---
id: CONCEPT-COREDNS_CUSTOMIZATION
type: concept
title: "CoreDNS customization in Kubespray — Corefile zones, forwarding, scaling"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-18"
confidence: confirmed
aliases:
  - coredns customization
  - corefile custom zones kubespray
  - coredns forwarding upstream
  - coredns_external_zones
  - coredns_additional_configs
  - coredns scaling autoscaler replicas
  - coredns rewrite
tags:
  - kubespray
  - coredns
  - dns
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "coredns_external_zones, coredns_additional_configs, coredns_rewrite_block, coredns_replicas, dns autoscaler vars, upstream_dns_servers"
relations:
  - type: see_also
    target: COMPONENT-COREDNS
  - type: see_also
    target: COMPONENT-NODELOCALDNS
  - type: see_also
    target: PRACTICE-DNS_STACK
  - type: see_also
    target: CONCEPT-ESCAPE_HATCHES
---

# CoreDNS customization in Kubespray — Corefile zones, forwarding, scaling

## Summary

Beyond deploying CoreDNS ([[COMPONENT-COREDNS]]), Kubespray exposes named variables to **customize the
Corefile** (custom zones, forwarders, rewrites), control **upstream forwarding**, and **scale** CoreDNS
(fixed replicas or the DNS autoscaler). This is the "how do I make cluster DNS do X" index — when the
default cluster DNS isn't enough, you rarely need to hand-edit the Corefile; a variable usually covers
it. Node-local caching is a separate layer ([[COMPONENT-NODELOCALDNS]]).

## Context

**Corefile content:**

- **`coredns_external_zones`** — inject extra zones/forwarders (e.g. forward a corporate domain to a
  specific resolver) not covered by defaults. The primary escape hatch for custom resolution
  ([[CONCEPT-ESCAPE_HATCHES]]).
- **`coredns_additional_configs`** — free-form Corefile snippet appended to the config for anything no
  named variable wraps.
- **`coredns_rewrite_block`** — `rewrite` rules (rename/CNAME-style query rewriting).
- **`coredns_default_zone_cache_block`** — tune the `cache` plugin for the default zone.
- **`enable_coredns_reverse_dns_lookups`** — toggle PTR/reverse lookups.

**Upstream forwarding:**

- **`upstream_dns_servers`** — resolvers CoreDNS forwards external queries to (default empty → uses the
  host resolver). **`dns_servers`** and `dns_domain` set the cluster resolver IPs and cluster domain.
- **`dns_mode`** — the DNS stack mode (coredns / coredns_dual / manual / none), which decides what is
  deployed.

**Scaling (two mutually-exclusive strategies):**

- **Fixed:** `coredns_replicas` — a static replica count.
- **Autoscaled:** the `dns-autoscaler` sizes CoreDNS by cluster size —
  `dns_nodes_per_replica`, `dns_cores_per_replica`, `dns_min_replicas`,
  `dns_prevent_single_point_failure`, plus `dns_autoscaler_*` resource/affinity knobs. Use the
  autoscaler on clusters whose node count varies; fixed replicas for small/stable clusters.
- **Resilience:** `coredns_pod_disruption_budget` / `_max_unavailable`, `coredns_affinity`,
  `coredns_deployment_nodeselector` spread CoreDNS across nodes so DNS survives a node loss.

**Where to customize what.** Prefer the **named variable**; fall back to `coredns_additional_configs`
for a raw Corefile snippet only when nothing wraps the setting. Per-node DNS caching and hot-path
performance are the **nodelocaldns** layer ([[COMPONENT-NODELOCALDNS]]), not CoreDNS itself. Stable
across **v2.27.0–v2.31.0**.

## References

- `roles/kubespray_defaults/defaults/main/main.yml` (coredns_* / dns_* vars) at tag v2.31.0. Component
  [[COMPONENT-COREDNS]]; node-local cache [[COMPONENT-NODELOCALDNS]]; DNS stack overview
  [[PRACTICE-DNS_STACK]]; escape hatches [[CONCEPT-ESCAPE_HATCHES]].

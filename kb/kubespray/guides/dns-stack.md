---
id: PRACTICE-DNS_STACK
type: best_practice
title: Kubespray DNS stack configuration (CoreDNS, NodeLocal DNS, resolvconf)
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - DNS stack
tags:
  - dns
  - coredns
  - networking
sources:
  - type: docs
    path: docs/advanced/dns-stack.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/advanced/dns-stack.md
    note: "Kubespray cluster DNS: dns_mode, resolvconf_mode, CoreDNS tuning, and NodeLocal DNS cache"
relations: []
---

# Kubespray DNS stack configuration (CoreDNS, NodeLocal DNS, resolvconf)

## Summary
Kubespray configures Kubernetes DNS as an authoritative server for `dns_domain` and its `svc`, `default.svc` subdomains (up to `ndots: 5` levels). Two orthogonal knobs drive behavior: `dns_mode` (how cluster DNS is installed) and `resolvconf_mode` (how host `/etc/resolv.conf` and non-k8s containers are handled). CoreDNS is the default, NodeLocal DNS cache is enabled by default since the 2.10 release. Non-cluster inventory nodes (external storage, separate etcd groups) are left for the user to configure.

## Context
Applies to any Kubespray-deployed cluster. Relevant variables live in inventory group_vars. Key decisions: whether to modify host resolv.conf (`resolvconf_mode`), which cluster DNS solution to install (`dns_mode`), upstream/backup nameservers, search domains, and CoreDNS/NodeLocal tuning. Note strict Linux limits: max 6 search domains and 256 chars total; default `svc`/`default.svc` subdomains reduce effective limits to 4 names / 239 chars unless `remove_default_searchdomains: true`.

## Implementation
### dns_mode (how cluster DNS is installed)
- `coredns` (default): CoreDNS as the default cluster DNS for all queries.
- `coredns_dual`: CoreDNS plus a secondary CoreDNS stack.
- `manual`: does not install CoreDNS; you set `manual_dns_server` for Pod DNS (install your own DNS server later).
- `none`: installs no DNS solution at all; leaves a non-functional cluster.

### resolvconf_mode (host / hostNetwork / non-k8s containers)
- `host_resolvconf` (default): modifies host `/etc/resolv.conf` and dhclient config to point at cluster DNS. Split into two stages: early (`dns_early: true`) uses `upstream_dns_servers` + `nameservers`; later reconfigured to prefer cluster DNS with the others as backups. Existing records (base/head/cloud-init/dhclient) are purged.
- `docker_dns`: adds `--dns/--dns-search/--dns-opt` flags to the docker daemon. Order of nameservers: cluster nameserver, `upstream_dns_servers`, host system nameservers. Search domains: cluster domains, `searchdomains`, host system domains. Default dns options `ndots:{{ndots}}`, `timeout:2`, `attempts:2` (override via `docker_dns_options`). Automatically adds host search domains — counts against the search-domain limit. Only affects `hostNetwork: true` pods and non-k8s containers; normal pods use kubelet `--cluster_dns`.
- `none`: does nothing to `/etc/resolv.conf`; `hostNetwork: true` pods and non-k8s containers cannot resolve cluster service names.

### Global resolv.conf tuning
- `ndots`, `dns_timeout`, `dns_attempts`: values written into `/etc/resolv.conf`. Warning: high `ndots` + many search domains degrade DNS performance.
- `searchdomains`: extra search domains added to cluster defaults; `remove_default_searchdomains: true` removes cluster default search domains.
- `nameservers`: used only by `host_resolvconf`; added after `upstream_dns_servers` as backups. Limit 3 servers, effectively 2 custom (one slot reserved for cluster).
- `upstream_dns_servers`: DNS added after cluster DNS in all modes; backups during early deployment when cluster DNS is not up yet.

### CoreDNS tuning variables
- `dns_upstream_forward_extra_opts`: dict of extra options for the CoreDNS/NodeLocal forward block.
- `coredns_kubernetes_extra_opts`, `coredns_kubernetes_extra_domains`: extend the kubernetes plugin.
- `coredns_additional_configs`, `coredns_rewrite_block`: extra config / rewrite plugin block.
- `coredns_external_zones`: array of external zones (zones, nameservers, cache, optional rewrite) injected before the kubernetes zone; useful for internal/VPN domains.
- `dns_etchosts`: hosts-file content served by CoreDNS (and NodeLocal if enabled).
- `enable_coredns_reverse_dns_lookups`: reverse lookups, default `true`.
- `coredns_default_zone_cache_block`: string block to tune default-zone cache (max TTL, success/denial counts, prefetch).
- `old_dns_domains`: list of former domains handled alongside current `dns_domain` (for migrating `dns_domain`).
- `systemd_resolved_disable_stub_listener`: sets `DNSStubListener=no` (default `true` on Flatcar); set `true` if CoreDNS fails with `address already in use`.

### NodeLocal DNS cache
- `enable_nodelocaldns: true` runs a per-node caching agent, avoiding iptables DNAT/conntrack; enabled by default since release 2.10.
- `nodelocaldns_external_zones`, `nodelocaldns_additional_configs`: extend NodeLocal config.
- HA: `enable_nodelocaldns_secondary: true` adds a redundant per-node pod. Caveat: with secondary enabled, the primary no longer tears down its iptables rules — if both daemonsets fail on the same node it can cause a DNS blackout (no fallback to central CoreDNS). `nodelocaldns_secondary_skew_seconds` (default 5) sets survival delta when both daemonsets update simultaneously.

### Caveats / limitations
- Search domains limited to 6 names / 256 chars (effectively 4 / 239 with default subdomains).
- `nameservers` limited to 3 (effectively 2 custom); mitigate with `upstream_dns_servers`.
- No custom `ndots` for SkyDNS; SkyDNS cannot forward unanswered queries to arbitrary recursive resolvers (left for future).

## References
- docs/advanced/dns-stack.md (tag v2.31.0 1c9add4)

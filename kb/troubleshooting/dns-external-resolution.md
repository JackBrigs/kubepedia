---
id: TROUBLE-DNS_EXTERNAL_RESOLUTION
type: troubleshooting
title: "Pods can't resolve external DNS (upstream forwarding)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - pods cannot resolve external names
  - SERVFAIL external dns
  - upstream_dns_servers
  - nodelocaldns forwarding
  - external domain not resolving in cluster
  - resolvconf_mode
tags:
  - troubleshooting
  - dns
  - coredns
  - nodelocaldns
  - networking
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "dns_mode / enable_nodelocaldns / nodelocaldns_ip / upstream_dns_servers / resolvconf_mode / ndots (tag v2.31.0)"
relations:
  - type: see_also
    target: PRACTICE-DNS_DEBUG
  - type: see_also
    target: PRACTICE-DNS_STACK
  - type: see_also
    target: TROUBLE-KUBESPRAY_PREFLIGHT_FAILS
---

# Pods can't resolve external DNS (upstream forwarding)

## Summary

In a stock Kubespray cluster a pod's DNS query goes: **pod → NodeLocal DNS
(`169.254.25.10`) → CoreDNS** for cluster names, and **→ upstream resolvers** for
external names. External-resolution failures (`SERVFAIL`/timeouts for public domains
while `*.svc.cluster.local` works) mean the **upstream** leg is broken: no/bad
`upstream_dns_servers`, an unusable host `/etc/resolv.conf`, a down NodeLocal DNS pod, or
UDP 53 blocked to the upstream.

## Problem

Cluster service names resolve, but external domains (e.g. `github.com`) return
`SERVFAIL`/`NXDOMAIN`/timeout from inside pods; or **all** DNS fails if NodeLocal DNS is
the sole resolver in the pod's `resolv.conf` and it's unhealthy.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`. Defaults: `dns_mode: coredns`,
  `enable_nodelocaldns: true`, `nodelocaldns_ip: 169.254.25.10`,
  `upstream_dns_servers: []`, `resolvconf_mode: host_resolvconf`, `ndots: 2`.
- With `upstream_dns_servers` **empty**, external queries are forwarded to the **host's**
  upstream nameservers (from `/etc/resolv.conf`). If the host can't resolve externally,
  neither can pods.
- Kubespray sets `ndots: 2` (lower than Kubernetes' default `5`), which reduces the
  search-domain fan-out that otherwise makes external lookups slow — a mitigation, not a
  cause.
- The preflight even asserts `/etc/resolv.conf` has a nameserver for coredns modes — see
  [[TROUBLE-KUBESPRAY_PREFLIGHT_FAILS]].

## Diagnostics

- From a pod: `kubectl run -it --rm dnstest --image=busybox:1.36 -- nslookup github.com`
  and `nslookup kubernetes.default` — cluster-OK + external-fail localises it to upstream.
- Inspect the pod resolver: `cat /etc/resolv.conf` in a pod (expect `nameserver
  169.254.25.10` with NodeLocal DNS, `ndots:2`).
- NodeLocal DNS health: `kubectl -n kube-system get pods -l k8s-app=nodelocaldns -o wide`
  and its logs; a `CrashLoopBackOff`/down node-local cache breaks DNS on that node.
- CoreDNS: `kubectl -n kube-system logs -l k8s-app=kube-dns` for upstream `SERVFAIL`.
- On the node: `cat /etc/resolv.conf` and `nslookup github.com <upstream>` — does the
  host itself resolve externally?

## Known Issues

**Fixes:**

- **Set explicit upstreams:** define `upstream_dns_servers: [<ip>, <ip>]` (e.g. internal
  resolvers) instead of relying on the host's `/etc/resolv.conf`. Re-run so CoreDNS/
  NodeLocal DNS pick it up.
- **Fix the host resolver:** if using the default (empty `upstream_dns_servers`), ensure
  each node's `/etc/resolv.conf` has a working nameserver; `resolvconf_mode`
  (`host_resolvconf`) governs how it's managed.
- **NodeLocal DNS down:** restart/repair the `nodelocaldns` DaemonSet; because pods point
  at `169.254.25.10`, a dead node-local cache takes **all** pod DNS on that node with it.
- **Firewall:** allow UDP/TCP **53** from nodes to the upstream resolvers (a blocked
  path looks exactly like SERVFAIL) — see [[TROUBLE-FIREWALL_PORTS_BLOCKED]].

**Gotchas:**

- Slow (not failing) external lookups are usually the classic `ndots` search-domain
  amplification — Kubespray's `ndots: 2` already mitigates; a pod overriding
  `dnsConfig`/`ndots` can reintroduce it.
- `dns_mode: none`/`manual` change this chain — verify the mode matches your intent
  ([[PRACTICE-DNS_STACK]]).
- Diagnosis procedure and CoreDNS Corefile details: [[PRACTICE-DNS_DEBUG]].

## References

- DNS defaults (`dns_mode`, `enable_nodelocaldns`, `upstream_dns_servers`,
  `resolvconf_mode`, `ndots`) at tag `v2.31.0`. Runbook: [[PRACTICE-DNS_DEBUG]];
  stack config: [[PRACTICE-DNS_STACK]].

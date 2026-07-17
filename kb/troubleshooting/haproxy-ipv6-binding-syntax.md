---
id: TROUBLE-HAPROXY_IPV6_BINDING
type: troubleshooting
title: "node haproxy: wrong IPv6 bind syntax in haproxy.cfg"
status: active
kubespray_version: ">=v2.29.0 <=v2.29.1"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - haproxy-ipv6-binding-syntax
tags:
  - troubleshooting
sources:
  - type: pull_request
    url: https://github.com/kubernetes-sigs/kubespray/pull/12862
    note: "fix merged in v2.30.0 (PR #12862)"
  - type: code
    path: roles/kubernetes/node/templates/loadbalancer/haproxy.cfg.j2
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.30.0/roles/kubernetes/node/templates/loadbalancer/haproxy.cfg.j2
    note: "fixed file"
relations:
  - type: see_also
    target: PRACTICE-HA_MODE
---

# node haproxy: wrong IPv6 bind syntax in haproxy.cfg

## Summary

The node-local haproxy load balancer template used incorrect syntax for binding on IPv6, so haproxy failed to start / bind on IPv6-enabled clusters. Fixed in **v2.30.0** (PR #12862).

## Problem

`haproxy.cfg.j2` rendered an invalid IPv6 `bind` line; on dual-stack/IPv6 nodes haproxy could not bind the API frontend, breaking the local apiserver LB.

## Context

- Affected Kubespray: `>=v2.29.0 <=v2.29.1`. Fixed in: `v2.30.0`.
- Confirmed via the merged PR #12862 and the tag code.

## Diagnostics

```bash
systemctl status haproxy --no-pager           # on a node using haproxy LB
journalctl -u haproxy -n 30 --no-pager        # bind/parse error?
```

## Known Issues

Root cause fixed by PR #12862 (in `roles/kubernetes/node/templates/loadbalancer/haproxy.cfg.j2`). Workaround before upgrading: correct the haproxy bind line manually, or switch the local LB type. The
durable fix is to upgrade to `v2.30.0` or later.

## References

- PR https://github.com/kubernetes-sigs/kubespray/pull/12862 — fixed in `v2.30.0`.
- `roles/kubernetes/node/templates/loadbalancer/haproxy.cfg.j2`.

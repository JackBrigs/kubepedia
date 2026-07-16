---
id: TROUBLE-NODELOCALDNS_IPV6_IP
type: troubleshooting
title: "NodeLocal DNS: IPv6 nodelocaldns_ip not handled in config"
status: active
kubespray_version: ">=v2.29.0 <=v2.30.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - nodelocaldns-ipv6-ip-render
tags:
  - troubleshooting
sources:
  - type: pull_request
    url: https://github.com/kubernetes-sigs/kubespray/pull/13087
    note: "fix merged in v2.31.0 (PR #13087)"
  - type: code
    path: roles/kubernetes-apps/ansible/templates/nodelocaldns-config.yml.j2
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/ansible/templates/nodelocaldns-config.yml.j2
    note: "fixed file"
relations: []
---

# NodeLocal DNS: IPv6 nodelocaldns_ip not handled in config

## Summary

On IPv6/dual-stack clusters, an IPv6 `nodelocaldns_ip` was not rendered correctly in the NodeLocal DNS config, breaking local DNS on those nodes. Fixed in **v2.31.0** (PR #13087).

## Problem

The `nodelocaldns-config.yml.j2` template did not correctly handle an IPv6 `nodelocaldns_ip`; the fix renders it properly for IPv6.

## Context

- Affected Kubespray: `>=v2.29.0 <=v2.30.0`. Fixed in: `v2.31.0`.
- Confirmed via the merged PR #13087 and the tag code.

## Diagnostics

```bash
kubectl -n kube-system get cm nodelocaldns -o yaml | grep -i bind
kubectl -n kube-system logs ds/nodelocaldns --tail=40
```

## Known Issues

Root cause fixed by PR #13087 (in `roles/kubernetes-apps/ansible/templates/nodelocaldns-config.yml.j2`). Workaround before upgrading: use an IPv4 `nodelocaldns_ip`, or upgrade to v2.31.0 for IPv6 support. The
durable fix is to upgrade to `v2.31.0` or later.

## References

- PR https://github.com/kubernetes-sigs/kubespray/pull/13087 — fixed in `v2.31.0`.
- `roles/kubernetes-apps/ansible/templates/nodelocaldns-config.yml.j2`.

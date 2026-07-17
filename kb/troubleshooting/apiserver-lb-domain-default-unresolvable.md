---
id: TROUBLE-APISERVER_LB_DOMAIN_DEFAULT
type: troubleshooting
title: "apiserver_loadbalancer_domain_name default no longer resolves"
status: active
kubespray_version: ">=v2.29.0 <=v2.29.1"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - apiserver-lb-domain-default-unresolvable
tags:
  - troubleshooting
sources:
  - type: pull_request
    url: https://github.com/kubernetes-sigs/kubespray/pull/12872
    note: "fix merged in v2.30.0 (PR #12872)"
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.30.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "fixed file"
relations:
  - type: see_also
    target: TROUBLE-APISERVER_CERT_SAN
---

# apiserver_loadbalancer_domain_name default no longer resolves

## Summary

The old default `lb-apiserver.kubernetes.local` for `apiserver_loadbalancer_domain_name` stopped resolving after Kubespray dropped the pseudo-DNS `/etc/hosts` injection, breaking API access through the name. Fixed in **v2.30.0** (PR #12872).

## Problem

Kubespray no longer injects `lb-apiserver.kubernetes.local` into `/etc/hosts`, so the previous default did not resolve. The fix defaults to the load-balancer IP if defined, otherwise to the node-local load balancer.

## Context

- Affected Kubespray: `>=v2.29.0 <=v2.29.1`. Fixed in: `v2.30.0`.
- Confirmed via the merged PR #12872 and the tag code.

## Diagnostics

```bash
getent hosts lb-apiserver.kubernetes.local     # does it resolve? (should not be relied on)
grep apiserver_loadbalancer_domain_name -r inventory/
```

## Known Issues

Root cause fixed by PR #12872 (in `roles/kubespray_defaults/defaults/main/main.yml`). Workaround before upgrading: set `apiserver_loadbalancer_domain_name` to a real, resolvable name/IP, or rely on the node-local LB (VARIABLE-LOADBALANCER_APISERVER_LOCALHOST). The
durable fix is to upgrade to `v2.30.0` or later.

## References

- PR https://github.com/kubernetes-sigs/kubespray/pull/12872 — fixed in `v2.30.0`.
- `roles/kubespray_defaults/defaults/main/main.yml`.

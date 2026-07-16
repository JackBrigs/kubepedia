---
id: TROUBLE-CILIUM_ENABLE_PROMETHEUS_NOOP
type: troubleshooting
title: "cilium_enable_prometheus had no effect (not wired to Helm values)"
status: active
kubespray_version: ">=v2.29.0 <=v2.30.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium-enable-prometheus-noop
tags:
  - troubleshooting
sources:
  - type: pull_request
    url: https://github.com/kubernetes-sigs/kubespray/pull/13142
    note: "fix merged in v2.31.0 (PR #13142)"
  - type: code
    path: roles/network_plugin/cilium/templates/values.yaml.j2
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/templates/values.yaml.j2
    note: "fixed file"
relations: []
---

# cilium_enable_prometheus had no effect (not wired to Helm values)

## Summary

Setting `cilium_enable_prometheus: true` did nothing — the variable was defined and documented but never mapped to the Cilium Helm values, so Prometheus metrics were not enabled. Fixed in **v2.31.0** (PR #13142).

## Problem

The variable existed in defaults/sample inventory but `prometheus.enabled` was missing from `values.yaml.j2`, making the flag a no-op. The fix adds the field so the flag works.

## Context

- Affected Kubespray: `>=v2.29.0 <=v2.30.0`. Fixed in: `v2.31.0`.
- Confirmed via merged PR #13142 and the tag code.

## Diagnostics

```bash
kubectl -n kube-system exec ds/cilium -- cilium status | grep -i prometheus
kubectl -n kube-system get pods -l k8s-app=cilium -o yaml | grep -i prometheus
```

## Known Issues

Fixed by PR #13142 (in `roles/network_plugin/cilium/templates/values.yaml.j2`). Workaround before upgrading: enable Cilium metrics directly via Helm values / a Cilium ConfigMap patch, or upgrade to v2.31.0. Durable fix: upgrade to `v2.31.0` or later.

## References

- PR https://github.com/kubernetes-sigs/kubespray/pull/13142 — fixed in `v2.31.0`.
- `roles/network_plugin/cilium/templates/values.yaml.j2`.

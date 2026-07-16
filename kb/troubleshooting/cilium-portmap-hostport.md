---
id: TROUBLE-CILIUM_PORTMAP
type: troubleshooting
title: "Cilium: hostPort/portmap handled via extra conflist instead of Cilium"
status: active
kubespray_version: ">=v2.29.0 <=v2.29.1"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium-portmap-hostport
tags:
  - troubleshooting
sources:
  - type: pull_request
    url: https://github.com/kubernetes-sigs/kubespray/pull/12814
    note: "fix merged in v2.30.0 (PR #12814)"
  - type: code
    path: roles/network_plugin/cilium/templates/values.yaml.j2
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.30.0/roles/network_plugin/cilium/templates/values.yaml.j2
    note: "fixed file"
relations: []
---

# Cilium: hostPort/portmap handled via extra conflist instead of Cilium

## Summary

hostPort (portmap) support was wired through a separate CNI conflist file rather than Cilium's own configuration, which could conflict with Cilium's chaining/datapath. Fixed in **v2.30.0** (PR #12814).

## Problem

Kubespray shipped a `000-cilium-portmap.conflist` and install step for hostPort; the fix removes it and enables portmap through Cilium's Helm values instead, aligning hostPort handling with Cilium.

## Context

- Affected Kubespray: `>=v2.29.0 <=v2.29.1`. Fixed in: `v2.30.0`.
- Confirmed via the merged PR #12814 and the tag code.

## Diagnostics

```bash
kubectl -n kube-system exec ds/cilium -- cilium status --verbose | grep -i hostport
# test a pod with a hostPort and confirm reachability
```

## Known Issues

Root cause fixed by PR #12814 (in `roles/network_plugin/cilium/templates/values.yaml.j2`). Workaround before upgrading: enable hostPort via Cilium values rather than the extra conflist. The
durable fix is to upgrade to `v2.30.0` or later.

## References

- PR https://github.com/kubernetes-sigs/kubespray/pull/12814 — fixed in `v2.30.0`.
- `roles/network_plugin/cilium/templates/values.yaml.j2`.

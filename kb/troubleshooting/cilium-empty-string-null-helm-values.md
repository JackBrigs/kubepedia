---
id: TROUBLE-CILIUM_EMPTY_STRING_NULL_HELM
type: troubleshooting
title: "Cilium: empty-string defaults render as null in Helm values"
status: active
kubespray_version: "v2.30.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium-empty-string-null-helm-values
tags:
  - troubleshooting
sources:
  - type: pull_request
    url: https://github.com/kubernetes-sigs/kubespray/pull/13109
    note: "fix merged in v2.31.0 (PR #13109)"
  - type: code
    path: roles/network_plugin/cilium/templates/values.yaml.j2
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/templates/values.yaml.j2
    note: "fixed file"
relations:
  - type: see_also
    target: COMPONENT-CILIUM
---

# Cilium: empty-string defaults render as null in Helm values

## Summary

Some Cilium options with empty-string defaults were rendered as YAML `null` in the generated Helm values, which Cilium could reject or misinterpret. Fixed in **v2.31.0** (PR #13109).

## Problem

Unquoted empty defaults in `values.yaml.j2` produced `null` instead of an empty string; the fix quotes them. Can cause Cilium install/config errors depending on the option.

## Context

- Affected Kubespray: `v2.30.0`. Fixed in: `v2.31.0`.
- Confirmed via merged PR #13109 and the tag code.

## Diagnostics

```bash
kubectl -n kube-system get cm cilium-config -o yaml | grep -iE ": null"
kubectl -n kube-system logs deploy/cilium-operator | tail -30
```

## Known Issues

Fixed by PR #13109 (in `roles/network_plugin/cilium/templates/values.yaml.j2`). Workaround before upgrading: explicitly set the affected Cilium options (avoid empty), or upgrade to v2.31.0. Durable fix: upgrade to `v2.31.0` or later.

## References

- PR https://github.com/kubernetes-sigs/kubespray/pull/13109 — fixed in `v2.31.0`.
- `roles/network_plugin/cilium/templates/values.yaml.j2`.

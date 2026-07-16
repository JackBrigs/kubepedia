---
id: TROUBLE-KUBE_VIP_CAPS_VERSION
type: troubleshooting
title: "kube-vip: excessive capabilities and version/tag mismatch"
status: active
kubespray_version: ">=v2.29.0 <=v2.29.1"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube-vip-capabilities-and-version
tags:
  - troubleshooting
sources:
  - type: pull_request
    url: https://github.com/kubernetes-sigs/kubespray/pull/12835
    note: "fix merged in v2.30.0 (PR #12835)"
  - type: code
    path: roles/kubernetes/node/templates/manifests/kube-vip.manifest.j2
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.30.0/roles/kubernetes/node/templates/manifests/kube-vip.manifest.j2
    note: "fixed file"
relations: []
---

# kube-vip: excessive capabilities and version/tag mismatch

## Summary

The kube-vip static-pod manifest requested all capabilities and used a hardcoded image tag that did not follow `kube_vip_version`, so the deployed kube-vip version could mismatch and ran over-privileged. Fixed in **v2.30.0** (PR #12835).

## Problem

The manifest dropped/added capabilities incorrectly and the image tag was a literal rather than `v{{ kube_vip_version }}`; from the fix, capabilities are minimized and the tag derives from `kube_vip_version` (see COMPONENT-KUBE_VIP).

## Context

- Affected Kubespray: `>=v2.29.0 <=v2.29.1`. Fixed in: `v2.30.0`.
- Confirmed via the merged PR #12835 and the tag code.

## Diagnostics

```bash
kubectl -n kube-system get pod -l name=kube-vip -o jsonpath="{.items[*].spec.containers[*].image}"
kubectl -n kube-system get pod -l name=kube-vip -o yaml | grep -A5 securityContext
```

## Known Issues

Root cause fixed by PR #12835 (in `roles/kubernetes/node/templates/manifests/kube-vip.manifest.j2`). Workaround before upgrading: pin `kube_vip_version` and verify the deployed image tag matches (see COMPONENT-KUBE_VIP). The
durable fix is to upgrade to `v2.30.0` or later.

## References

- PR https://github.com/kubernetes-sigs/kubespray/pull/12835 — fixed in `v2.30.0`.
- `roles/kubernetes/node/templates/manifests/kube-vip.manifest.j2`.

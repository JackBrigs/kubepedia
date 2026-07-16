---
id: TROUBLE-CONTROL_PLANE_OVERRIDE_HOSTNAME_DELEGATION
type: troubleshooting
title: "control-plane: kube_override_hostname breaks first-control-plane delegation"
status: active
kubespray_version: ">=v2.29.0 <=v2.29.1"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - control-plane-override-hostname-delegation
tags:
  - troubleshooting
sources:
  - type: pull_request
    url: https://github.com/kubernetes-sigs/kubespray/pull/12636
    note: "fix merged in v2.30.0 (PR #12636)"
  - type: code
    path: roles/kubernetes/control-plane/tasks/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.30.0/roles/kubernetes/control-plane/tasks/main.yml
    note: "fixed file"
relations: []
---

# control-plane: kube_override_hostname breaks first-control-plane delegation

## Summary

With `kube_override_hostname` set, node names from `kubectl get nodes` differ from Ansible's `inventory_hostname`, causing task delegation failures on the control plane. Fixed in **v2.30.0** (PR #12636).

## Problem

Kubespray resolved the first control-plane node from kubectl output, which does not match `inventory_hostname` when `kube_override_hostname` is used; the fix stops depending on that mapping.

## Context

- Affected Kubespray: `>=v2.29.0 <=v2.29.1`. Fixed in: `v2.30.0`.
- Confirmed via the merged PR #12636 and the tag code.

## Diagnostics

```bash
kubectl get nodes -o name          # compare node names to your inventory_hostname
grep kube_override_hostname -r inventory/
```

## Known Issues

Root cause fixed by PR #12636 (in `roles/kubernetes/control-plane/tasks/main.yml`). Workaround before upgrading: avoid `kube_override_hostname`, or upgrade so delegation no longer relies on the kubectl-to-inventory mapping. The
durable fix is to upgrade to `v2.30.0` or later.

## References

- PR https://github.com/kubernetes-sigs/kubespray/pull/12636 — fixed in `v2.30.0`.
- `roles/kubernetes/control-plane/tasks/main.yml`.

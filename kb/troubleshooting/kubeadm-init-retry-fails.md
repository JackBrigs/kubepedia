---
id: TROUBLE-KUBEADM_INIT_RETRY_FAILS
type: troubleshooting
title: "kubeadm init retry always fails on leftovers from the first try"
status: active
kubespray_version: ">=v2.29.0 <=v2.29.1"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubeadm-init-retry-fails
tags:
  - troubleshooting
sources:
  - type: pull_request
    url: https://github.com/kubernetes-sigs/kubespray/pull/12785
    note: "fix merged in v2.30.0 (PR #12785)"
  - type: code
    path: roles/kubernetes/control-plane/tasks/kubeadm-setup.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.30.0/roles/kubernetes/control-plane/tasks/kubeadm-setup.yml
    note: "fixed file"
relations: []
---

# kubeadm init retry always fails on leftovers from the first try

## Summary

When the first `kubeadm init` attempt failed and Kubespray retried, the retry always failed because artifacts from the first attempt were still present. Fixed in **v2.30.0** (PR #12785).

## Problem

The retry did not tolerate remnants (already-created files/ports) from the first `kubeadm init`; the fix ignores the related preflight/leftover errors on retry so it can proceed.

## Context

- Affected Kubespray: `>=v2.29.0 <=v2.29.1`. Fixed in: `v2.30.0`.
- Confirmed via the merged PR #12785 and the tag code.

## Diagnostics

```bash
journalctl -u kubelet -n 50 --no-pager
# on the first control-plane node, look for kubeadm init failing on "already exists" during retry
```

## Known Issues

Root cause fixed by PR #12785 (in `roles/kubernetes/control-plane/tasks/kubeadm-setup.yml`). Workaround before upgrading: clean up the failed init (`kubeadm reset` on that node) before re-running, or upgrade for the automatic retry handling. The
durable fix is to upgrade to `v2.30.0` or later.

## References

- PR https://github.com/kubernetes-sigs/kubespray/pull/12785 — fixed in `v2.30.0`.
- `roles/kubernetes/control-plane/tasks/kubeadm-setup.yml`.

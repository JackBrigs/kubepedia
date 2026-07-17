---
id: TROUBLE-ETCD_CERT_DIR_RECURSIVE_PERMS_CALICO
type: troubleshooting
title: Recursive 0700 perms on etcd cert dir break Calico in etcd datastore mode
status: active
kubespray_version: "v2.29.1"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - etcd_cert_dir_mode removal
tags:
  - etcd
  - certificates
sources:
  - type: github_pr
    url: https://github.com/kubernetes-sigs/kubespray/pull/12908
    note: "PR removing etcd_cert_dir_mode and applying cert dir perms non-recursively (merged 2026-01-27)"
relations:
  - type: see_also
    target: COMPONENT-ETCD
---

# Recursive 0700 perms on etcd cert dir break Calico in etcd datastore mode

## Summary
On clusters using Calico in etcd datastore mode with dedicated etcd nodes, applying `0700`
permissions recursively to `/etc/ssl/etcd/ssl` stripped group permissions from the etcd
certificate files that Calico depends on. This broke `calico-kube-controllers` during upgrade or
control-plane rotation. Fixed in v2.30.0 by removing `etcd_cert_dir_mode` and applying directory
permissions non-recursively.

## Problem
Clusters running Calico in **etcd datastore** mode with dedicated etcd nodes failed during
upgrade / control-plane rotation: `calico-kube-controllers` could not read the certificates
needed to access etcd. The root change concerns etcd certificate handling (and explains the
removal of the `etcd_cert_dir_mode` variable in v2.30.0), even though the visible failure is on
Calico.

## Context
- Affected Kubespray version (within scope): v2.29.1. The cache notes the recursive behavior
  applied to versions ≤ v2.29.1.
- Fixed in v2.30.0 (with backports to release-2.27/2.28/2.29).
- Trigger conditions: Calico in etcd datastore mode, dedicated etcd nodes, upgrade or
  control-plane rotation.

## Diagnostics
- Symptom: `calico-kube-controllers` fails to read etcd certificates after an upgrade or
  control-plane rotation.
- Inspect the permissions on `/etc/ssl/etcd/ssl`: with the bug, `0700` was applied recursively,
  removing group permissions from the certificate files.

## Known Issues
- Root cause: `0700` permissions were applied **recursively** to `/etc/ssl/etcd/ssl`, stripping
  group permissions from the certificate files that Calico relies on.
- Fix (breaking change in v2.30.0): PR
  [#12908](https://github.com/kubernetes-sigs/kubespray/pull/12908) (merged 2026-01-27) removed
  the `etcd_cert_dir_mode` variable (the directory mode is now always `0700`) and applies the
  directory permissions **non-recursively**. Backports to release-2.27/2.28/2.29.
- Verification against the v2.30.0 tag: the `etcd_cert_dir_mode` variable is absent from the code
  (grep over `roles/` is empty), confirming the removal. This is a breaking change for anyone who
  overrode it.

## References
- https://github.com/kubernetes-sigs/kubespray/pull/12908
- Migrated from Kubepedia 0.1.0 cache: etcd-cert-dir-recursive-perms-calico-v2.30.0.md

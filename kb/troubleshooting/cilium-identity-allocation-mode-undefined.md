---
id: TROUBLE-CILIUM_IDENTITY_ALLOCATION_MODE_UNDEFINED
type: troubleshooting
title: kubeadm task fails when cilium_identity_allocation_mode is undefined
status: active
kubespray_version: ">=v2.29.0 <=v2.30.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - cilium_identity_allocation_mode is undefined
tags:
  - cilium
  - kubeadm
  - etcd
sources:
  - type: github_pr
    url: https://github.com/kubernetes-sigs/kubespray/pull/13121
    note: "Merged PR moving the cilium_identity_allocation_mode default into shared kubespray defaults"
relations: []
---

# kubeadm task fails when cilium_identity_allocation_mode is undefined

## Summary
A task in the `kubernetes/kubeadm` role fails with `'cilium_identity_allocation_mode' is undefined` when a non-Cilium CNI is selected or the Cilium role defaults are not loaded (e.g. partial `--tags` runs). Fixed in v2.31.0 by moving the default into shared kubespray defaults; workaround is to set the variable explicitly.

## Problem
The task in the `kubernetes/kubeadm` role fails with `'cilium_identity_allocation_mode' is undefined`. It manifests when a non-Cilium CNI is chosen (`kube_network_plugin != cilium`) and/or during a partial role run (`--tags`) where the Cilium role defaults are not loaded.

## Context
- Affected versions: v2.29.0, v2.29.1, v2.30.0 (the condition was introduced by PR #12565, which landed in v2.29.0).
- Fixed versions: v2.31.0.
- Triggered when `kube_network_plugin != cilium`, or when partial `--tags` runs skip loading the Cilium role defaults.

## Diagnostics
- Look for the Ansible failure `'cilium_identity_allocation_mode' is undefined` in the `kubernetes/kubeadm` role.
- Confirm in tag v2.30.0 `roles/kubernetes/kubeadm/tasks/main.yml:211`: `kube_network_plugin != "cilium" or cilium_identity_allocation_mode != 'crd'` reads the variable without a guard.
- Confirm `cilium_identity_allocation_mode` is absent from `roles/kubespray_defaults/defaults/main/main.yml` and only defined in `roles/network_plugin/cilium/defaults/main.yml:30` (`cilium_identity_allocation_mode: crd`).

## Known Issues
Root cause: the etcd-certificate-extraction skip condition in `roles/kubernetes/kubeadm/tasks/main.yml` (introduced by PR #12565) unconditionally reads `cilium_identity_allocation_mode`, but that variable is defined only in `roles/network_plugin/cilium/defaults/main.yml`, not in the shared defaults. When Cilium is not selected the variable is undefined and the condition evaluation fails. The `or` condition still evaluates the second operand even when the first is true, so Jinja fails on the undefined variable.

Fix: PR #13121 (master → v2.31.0) moves the default `cilium_identity_allocation_mode: crd` into `roles/kubespray_defaults/defaults/main/main.yml`, where it is always available.

Workaround on v2.30.0: explicitly set `cilium_identity_allocation_mode: crd` in `group_vars` (even when the CNI is not Cilium).

## References
- https://github.com/kubernetes-sigs/kubespray/pull/13121
- Migrated from Kubepedia 0.1.0 cache: cilium-identity-allocation-mode-undefined-v2.30.0.md

---
id: TROUBLE-KUBEADM_VERSION_SKEW
type: troubleshooting
title: "kubeadm version skew: can't skip a minor / kubelet too old"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: verified
aliases:
  - kubeadm cannot upgrade skip minor
  - specified version to upgrade to is too high
  - version skew policy kubelet
  - one minor at a time upgrade
tags:
  - troubleshooting
  - kubeadm
  - upgrade
  - version
sources:
  - type: docs
    path: Kubernetes version skew policy
    url: https://kubernetes.io/releases/version-skew-policy/
    note: "kubeadm: one minor at a time; kubelet within N-3"
relations:
  - type: see_also
    target: CONCEPT-KUBESPRAY_KUBEADM_SEAM
  - type: see_also
    target: CONCEPT-KUBERNETES_VERSION_SUPPORT
  - type: see_also
    target: UPGRADE-KUBESPRAY_SEQUENTIAL
---

# kubeadm version skew: can't skip a minor / kubelet too old

## Summary

A Kubespray upgrade that jumps **more than one Kubernetes minor** fails at kubeadm's version
check — kubeadm enforces the **skew policy**: upgrade **one minor at a time**, and the kubelet
must stay within **N-3** of the control plane. This is a kubeadm refusal surfaced by Ansible
([[CONCEPT-KUBESPRAY_KUBEADM_SEAM]]).

## Problem

- `kubeadm upgrade`: `specified version to upgrade to "v1.3X.0" is too high; ... can only
  upgrade to the next minor` (or similar version-skew preflight error).
- After a big `kube_version` bump, `kubeadm upgrade apply` refuses.

## Context

- Applies to Kubespray **v2.29.0–v2.31.0** / Kubernetes **1.29–1.35**. Each Kubespray tag also
  supports only a **3-minor window** ([[CONCEPT-KUBERNETES_VERSION_SUPPORT]]), reinforcing this.

## Diagnostics

- **The rule:** the control plane upgrades **one minor at a time** (e.g. 1.31 → 1.32 → 1.33, not
  1.31 → 1.33). The **kubelet** may be up to **3 minors older** than the apiserver but never
  newer.
- **Fix — step through minors:** set `kube_version` to the **next** minor, run the upgrade, let
  it complete healthy, then bump again. Do the same across Kubespray tags — a Kubespray tag only
  ships a 3-minor window, so reaching a far target means **sequential Kubespray upgrades** too
  ([[UPGRADE-KUBESPRAY_SEQUENTIAL]]).
- **Don't force it:** ignoring the version preflight (`--ignore-preflight-errors`) to skip a
  minor is unsupported and typically breaks the control plane at the health check
  ([[TROUBLE-KUBEADM_UPGRADE_HEALTH_CHECK]]).
- **Also mind the etcd and component skew:** kubeadm bumps etcd per K8s minor; skipping minors
  skips the intended etcd steps too.

## Known Issues

- The `kube_version` you set must be one Kubespray's tag actually supports
  ([[CONCEPT-KUBERNETES_VERSION_SUPPORT]]) — an out-of-window version fails download **and**
  the kubeadm version check.

## References

- Kubernetes version-skew policy (above); seam: [[CONCEPT-KUBESPRAY_KUBEADM_SEAM]]; window:
  [[CONCEPT-KUBERNETES_VERSION_SUPPORT]]; sequential upgrades: [[UPGRADE-KUBESPRAY_SEQUENTIAL]].

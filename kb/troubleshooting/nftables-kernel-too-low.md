---
id: TROUBLE-NFTABLES_KERNEL_TOO_LOW
type: troubleshooting
title: kube-proxy nftables mode requires kernel >= 5.13
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - nftables kernel too low
  - kube_proxy_mode nftables kernel
  - nftables preflight fail
tags:
  - troubleshooting
  - kube-proxy
  - nftables
  - kernel
  - preflight
sources:
  - type: code
    path: roles/kubernetes/preinstall/tasks/0040-verify-settings.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/preinstall/tasks/0040-verify-settings.yml
    note: "assert: kernel >= 5.13 when kube_proxy_mode == nftables (tag v2.31.0)"
relations:
  - type: see_also
    target: TROUBLE-KUBESPRAY_PREFLIGHT_FAILS
  - type: see_also
    target: CONCEPT-K8S_1_33_CHANGES
  - type: see_also
    target: CONCEPT-K8S_1_35_CHANGES
---

# kube-proxy nftables mode requires kernel >= 5.13

## Summary

Kubespray refuses to deploy with `kube_proxy_mode: nftables` on hosts whose kernel is
older than **5.13**. The preflight assertion stops the run before install. This matters
now because the `nftables` backend reached GA in Kubernetes `1.33` and `ipvs` is
deprecated in `1.35`, so more operators are switching to it.

## Problem

Preinstall aborts on the task `Stop if kernel version is too low for nftables` when
`kube_proxy_mode: nftables` is set and the node kernel is `< 5.13`.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`.
- The check: `ansible_kernel.split('-')[0] is version('5.13', '>=')`, guarded by
  `when: kube_proxy_mode == 'nftables'` and `not ignore_assert_errors`.
- Upstream kube-proxy nftables itself wants a reasonably recent kernel; 5.13 is the
  floor Kubespray enforces. nftables is GA since Kubernetes `1.33`
  ([[CONCEPT-K8S_1_33_CHANGES]]); `ipvs` deprecated in `1.35`
  ([[CONCEPT-K8S_1_35_CHANGES]]).

## Diagnostics

- Check the node kernel: `uname -r` (compare the numeric part to `5.13`).
- Confirm the mode: `kube_proxy_mode` in your inventory (`k8s-cluster.yml`).
- The failing task name and the assert condition (`5.13`) identify the cause directly.

## Known Issues

- **Fix options:** upgrade the node kernel to `>= 5.13`, or keep `kube_proxy_mode:
  ipvs` / `iptables` on older kernels (both remain supported in-range; `ipvs` is
  deprecated upstream from `1.35` but still functional).
- The kernel version is parsed from `ansible_kernel` up to the first `-`; distro
  back-ported kernels reporting an old base version can trip the check even if nftables
  would work — verify the effective nft/kernel capability before overriding.
- Bypassing via `ignore_assert_errors: true` lets the deploy proceed but kube-proxy may
  then fail at runtime on an incapable kernel — not recommended.

## References

- `0040-verify-settings.yml` (nftables kernel assert) at tag `v2.31.0`.
- Preflight overview: [[TROUBLE-KUBESPRAY_PREFLIGHT_FAILS]].

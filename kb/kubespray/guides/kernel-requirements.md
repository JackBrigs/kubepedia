---
id: PRACTICE-KERNEL_REQUIREMENTS
type: best_practice
title: Kernel Requirements for Kubespray Nodes
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - kernel version requirements
tags:
  - kernel
  - os
  - preflight
sources:
  - type: docs
    path: docs/operations/kernel-requirements.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/operations/kernel-requirements.md
    note: "Minimum and recommended host kernel versions per OS, plus how to bypass kubeadm preflight when the kernel is too old"
relations:
  - type: see_also
    target: TROUBLE-NFTABLES_KERNEL_TOO_LOW
---

# Kernel Requirements for Kubespray Nodes

## Summary
Kubespray nodes must run a kernel new enough for the target Kubernetes version. For Kubernetes >=1.32.0 the recommended 4.x LTS kernel is 4.19; any 5.x or 6.x kernel is also supported. For cgroups v2 the minimum kernel is 4.15 and 5.8+ is recommended. When the host kernel is below the requirement, you can suppress the kubeadm preflight failure instead of upgrading the kernel.

## Context
Applies when preparing OS images/hosts for a Kubespray deployment, especially on older enterprise distributions. The doc provides a per-OS kernel matrix so you can tell in advance whether a distribution meets the >=4.19 recommendation. Notably several RHEL-family 8 releases and Amazon Linux 2 ship kernels below 4.19 and are flagged as non-compliant.

## Implementation
Kernel guidance for Kubernetes >=1.32.0:
- Recommended 4.x LTS kernel: 4.19; 5.x and 6.x are supported.
- cgroups v2: minimum kernel 4.15, recommended 5.8+.

If the host kernel is lower than required, ignore the kubeadm preflight error by setting:

```yaml
kubeadm_ignore_preflight_errors:
  - SystemVerification
```

Per-OS kernel matrix (does the shipped kernel meet >=4.19?):
- Compliant (>=4.19): RHEL 9 (5.14), Alma Linux 9 (5.14), Rocky Linux 9 (5.14), Oracle Linux 9 (5.14), Ubuntu 24.04 (6.6), Ubuntu 22.04 (5.15), Ubuntu 20.04 (5.4), Debian 12 (6.1), Debian 11 (5.10), Fedora 40 (6.8), Fedora 39 (6.5), openSUSE Leap 15.5 (5.14), openEuler 24.03 (6.6), openEuler 22.03 (5.10), openEuler 20.03 (4.19).
- Non-compliant (<4.19): RHEL 8 (4.18), Alma Linux 8 (4.18), Rocky Linux 8 (4.18), Oracle Linux 8 (4.18), Amazon Linux 2 (4.14).

Caveat: bypassing the preflight check only silences the validator; it does not add missing kernel features (for example cgroups v2 behavior), so prefer a compliant kernel where possible. See the Kubernetes kernel version requirements reference for authoritative details.

## References
- docs/operations/kernel-requirements.md (tag v2.31.0 1c9add4)

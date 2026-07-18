---
id: CONCEPT-TALOS_K8S_MATRIX
type: concept
title: "Talos ↔ Kubernetes support matrix (Talos 1.10–1.13) + CAPI/Omni version pairing"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: "1.13.6"
verified_at: "2026-07-18"
confidence: verified
aliases:
  - talos kubernetes support matrix
  - which kubernetes version talos supports
  - talos 1.13 kubernetes versions
  - talos capi provider versions
  - talos omni minimum version
tags:
  - talos
  - kubernetes
  - compatibility
sources:
  - type: docs
    path: public/talos/v1.13/getting-started/support-matrix.mdx
    url: https://github.com/siderolabs/docs/blob/main/public/talos/v1.13/getting-started/support-matrix.mdx
    note: "Talos 1.13 & 1.12 K8s columns + CAPI/Omni/Sidero min versions (siderolabs/docs @59a5195)"
  - type: docs
    path: website/content/v1.11/introduction/support-matrix.md
    url: https://github.com/siderolabs/talos/blob/v1.11.6/website/content/v1.11/introduction/support-matrix.md
    note: "Talos 1.11 & 1.10 rows (siderolabs/talos @v1.11.6)"
relations:
  - type: see_also
    target: CONCEPT-TALOS_UPGRADES
  - type: see_also
    target: CONCEPT-KUBERNETES_VERSION_SUPPORT
  - type: see_also
    target: CONCEPT-TALOS_CLUSTER_API
  - type: see_also
    target: CONCEPT-TALOS_OMNI
---

# Talos ↔ Kubernetes support matrix (Talos 1.10–1.13) + CAPI/Omni version pairing

## Summary

Each **Talos minor supports a rolling window of 6 Kubernetes minors**, advancing one minor per Talos
release. This is the precise matrix for recent Talos versions, plus the **version pairing** for the
Cluster API providers ([[CONCEPT-TALOS_CLUSTER_API]]) and Omni ([[CONCEPT-TALOS_OMNI]]) — which must
track the Talos minor. **Talos 1.13.6** is the current stable (v1.14 is pre-release/alpha), confirming
the KB's Talos baseline.

## Context

**Talos → Kubernetes (supported minors):**

| Talos | Supported Kubernetes | Omni min | CABPT (bootstrap) | CACPPT (control-plane) | Sidero |
|-------|----------------------|----------|-------------------|------------------------|--------|
| **1.13** | 1.31 – 1.36 | ≥ 1.8.0 | ≥ 0.6.12 | ≥ 0.5.13 | ≥ 0.6.13 |
| **1.12** | 1.30 – 1.35 | ≥ 1.4.0 | ≥ 0.6.11 | ≥ 0.5.12 | ≥ 0.6.12 |
| **1.11** | 1.29 – 1.34 | ≥ 0.50.0 | ≥ 0.6.8 | ≥ 0.5.9 | *(unverified)* |
| **1.10** | 1.28 – 1.33 | ≥ 0.49.0 | ≥ 0.6.8 | ≥ 0.5.9 | *(unverified)* |

- **Reading it:** to run K8s 1.35 you need Talos **≥1.12**; K8s 1.36 needs Talos **1.13**. Talos 1.13
  tops out at K8s 1.36. Pick the Talos version from the Kubernetes version you target (overlaps the
  Kubepedia K8s 1.29–1.35 window from Talos 1.10 up).
- **Architectures:** amd64 and arm64 for all. **Local dev:** Docker + QEMU
  ([[CONCEPT-TALOS_LOCAL_CLUSTER]]).
- **Platform tiers:** Tier 1 (tested, priority fixes) = **Metal, AWS, GCP**; Tier 2 = Azure,
  DigitalOcean, OpenStack, VMware; Tier 3 (community) = Hetzner, Oracle, Scaleway, Vultr, Upcloud,
  nocloud, etc.
- **Boot (bare metal):** ISO / PXE / disk image; x86 BIOS/UEFI/**SecureBoot**, arm64 UEFI/SecureBoot
  (SecureBoot added in 1.13). Virtualized: VMware, Hyper-V, KVM, Proxmox, Xen; plus a fixed SBC list
  (Raspberry Pi 4B/CM4, Pine64, Radxa ROCK, Jetson Nano, Turing RK1, Orange Pi 5, …).

**Lifecycle / EOL:** a Talos minor reaches **End of Community Support** when the *next* minor's `.0`
ships (e.g. 1.13 EOL at 1.14.0); enterprise support is separate (Sidero Labs). Keep Talos current so
its K8s window still covers your target ([[CONCEPT-TALOS_UPGRADES]]).

**Contrast with Kubespray.** Kubespray maps its own tags to K8s versions
([[CONCEPT-KUBERNETES_VERSION_SUPPORT]]); Talos has its **own** OS↔K8s matrix independent of Kubespray.
Talos is an alternative immutable-OS path, not a Kubespray-managed component — versions here come from
Talos/Omni docs, not Kubespray.

## References

- `siderolabs/docs` `public/talos/v1.13/getting-started/support-matrix.mdx` (@59a5195) and
  `siderolabs/talos` `website/content/v1.11/introduction/support-matrix.md` (@v1.11.6). CAPI
  [[CONCEPT-TALOS_CLUSTER_API]]; Omni [[CONCEPT-TALOS_OMNI]]; local dev [[CONCEPT-TALOS_LOCAL_CLUSTER]];
  Talos upgrades [[CONCEPT-TALOS_UPGRADES]].

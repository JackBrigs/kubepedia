---
id: CONCEPT-TALOS_UPGRADES
type: concept
title: "Talos upgrades — OS image (A/B) and Kubernetes"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: "1.13.6"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - talosctl upgrade
  - talosctl upgrade-k8s
  - talos rollback
  - talos kubernetes upgrade
  - talos support matrix
tags:
  - os
  - talos
  - upgrade
  - documentation
sources:
  - type: docs
    path: Talos upgrading Talos Linux
    url: https://www.talos.dev/latest/talos-guides/upgrading-talos/
    note: "talosctl upgrade, A/B image, rollback"
  - type: docs
    path: Talos upgrading Kubernetes
    url: https://www.talos.dev/latest/kubernetes-guides/upgrading-kubernetes/
    note: "talosctl upgrade-k8s orchestration"
relations:
  - type: see_also
    target: CONCEPT-TALOS_OS_K8S
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
  - type: see_also
    target: TROUBLE-TALOS_CP_BOOTSTRAP
---

# Talos upgrades — OS image (A/B) and Kubernetes

## Summary

Talos separates **two** upgrades: the **OS image** (`talosctl upgrade`) and **Kubernetes**
(`talosctl upgrade-k8s`). The OS upgrade is **atomic and A/B** (new image written, reboot into
it, rollback available); the Kubernetes upgrade is orchestrated across the control plane and
kubelets. Respect the Talos↔Kubernetes **support matrix**.

## Context

- Applies to Talos **1.13.x** ([[CONCEPT-TALOS_OS_K8S]]); the latest-versions view is
  [[CONCEPT-UPGRADE_HORIZON]].

## Implementation

**OS upgrade.**

- `talosctl upgrade --nodes <ip> --image ghcr.io/siderolabs/installer:v<X.Y.Z>` — Talos writes
  the new image to the alternate boot slot and reboots into it (**A/B**). `--preserve` keeps
  ephemeral data; `--stage` performs the upgrade on next boot (useful when the disk is busy).
- **One node at a time**, and **control-plane nodes one at a time** to keep **etcd quorum**.
  `talosctl health` between steps.
- **Rollback:** `talosctl rollback` boots the previous slot if the new image misbehaves.
- Talos preflight-checks etcd health and disk space before proceeding.

**Kubernetes upgrade.**

- `talosctl --nodes <cp-ip> upgrade-k8s --to <1.Y.Z>` — Talos bumps kube-apiserver,
  controller-manager, scheduler (static pods) and rolls the kubelets across all nodes, in the
  right order. It's a **control-plane-driven** operation (run once against a CP node).

**Sequencing & support.**

- Upgrade **Talos first** (within a supported Talos↔K8s pairing), then Kubernetes — or follow
  the support matrix, which lists the Kubernetes versions each Talos release supports. **Don't
  skip Talos minors**; step one minor at a time.
- **Back up first:** `talosctl etcd snapshot db.snapshot` and keep the **secrets bundle** safe
  before any upgrade.

## Compatibility

- Each Talos minor supports a **specific set of Kubernetes minors** — check the Talos support
  matrix for the exact pairing before choosing target versions; going outside it is unsupported.
- Because the rootfs is immutable and A/B, a failed OS upgrade is recoverable by rollback —
  unlike in-place distro upgrades on Kubespray nodes.

## References

- Talos upgrade guides (Talos + Kubernetes) (above); overview: [[CONCEPT-TALOS_OS_K8S]];
  bootstrap issues: [[TROUBLE-TALOS_CP_BOOTSTRAP]]; horizon: [[CONCEPT-UPGRADE_HORIZON]].

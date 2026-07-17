---
id: CONCEPT-TALOS_OS_K8S
type: concept
title: "Talos OS and Kubernetes (immutable, API-managed node OS)"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: "1.13.6"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - talos os
  - talos linux
  - talosctl
  - immutable kubernetes os
  - talos machine config
  - talos disk encryption
tags:
  - os
  - talos
  - nodes
  - immutable
  - security
sources:
  - type: docs
    path: Talos Linux documentation
    url: https://www.talos.dev/latest/
    note: official Talos docs (architecture, machine config, upgrades)
  - type: docs
    path: Talos disk encryption
    url: https://www.talos.dev/latest/talos-guides/configuration/disk-encryption/
    note: built-in LUKS2 for STATE/EPHEMERAL (nodeID/static/tpm/kms)
relations:
  - type: see_also
    target: CONCEPT-CLEVIS_LUKS2
  - type: see_also
    target: CONCEPT-UBUNTU_24_04_K8S
  - type: see_also
    target: CONCEPT-KUBERNETES_VERSION_SUPPORT
---

# Talos OS and Kubernetes (immutable, API-managed node OS)

## Summary

Talos Linux is a **minimal, immutable, API-managed** operating system built solely to run
Kubernetes. Latest **v1.13.6**. It has **no SSH, no shell, no systemd, and no package
manager** — the node is configured entirely through a declarative **machine config** (YAML) and
the **`talosctl`** gRPC API (mTLS, port 50000). **Scope note:** Talos is **not a
Kubespray-managed OS** — Kubespray provisions traditional distros (Ubuntu/Debian/RHEL-family)
over **SSH + Ansible**, which Talos does not offer. This doc is adjacent-domain context (like
the OS layer) for teams comparing or migrating.

## Context

- Applies to Talos **1.13.x** running Kubernetes in the base's `1.29`–`1.35` window; a given
  Talos release supports a **specific set of Kubernetes minors** — check the Talos support
  matrix for the exact pairing before pinning.
- Talos and Kubespray are **different provisioning models**: Kubespray = mutable distro +
  Ansible; Talos = immutable image + declarative config API. They are not mixed on one node.

## Implementation

**How Talos runs Kubernetes.**

- Machine types: **controlplane** and **worker**; the control plane is bootstrapped once with
  `talosctl bootstrap`. Talos runs etcd and the control-plane components as static pods it
  manages.
- The root filesystem is **read-only** (SquashFS, largely in RAM); persistent state lives on
  the **STATE** partition (machine config) and **EPHEMERAL** partition (`/var`, container data).
- No in-place mutation: you don't `apt install`, edit files over SSH, or run shell tuning —
  **everything is a config change** applied with `talosctl apply-config` (kernel args, sysctls,
  registry mirrors, extensions, disks). System extensions add drivers/agents (e.g. NVIDIA,
  iSCSI) at image-build time.

**Upgrades.**

- OS: **`talosctl upgrade`** swaps the whole image (A/B style, reboot); it's atomic and
  rollback-friendly.
- Kubernetes: **`talosctl upgrade-k8s`** orchestrates the control-plane/kubelet version bump —
  separate from the OS upgrade.

## Compatibility

- **cgroup v2 only** and a recent kernel — satisfies Kubernetes `1.35`'s cgroup-v1 removal by
  design ([[CONCEPT-KUBERNETES_VERSION_SUPPORT]]).
- **Built-in disk encryption (LUKS2):** the STATE and EPHEMERAL partitions can be encrypted
  with LUKS2 via the machine config, with key providers: **`nodeID`** (key derived from the
  node's identity — no external dependency), **`static`** (a fixed key), **`tpm`** (sealed to
  TPM2), and **`kms`** (fetched from a network KMS at boot). This is Talos's native alternative
  to **Clevis + LUKS2** on traditional distros ([[CONCEPT-CLEVIS_LUKS2]]).
- **KubeSpan** (optional) builds a WireGuard mesh between nodes across networks.
- **Security posture:** no interactive login and an immutable rootfs shrink the attack surface;
  the management API is mTLS-authenticated. The trade-off is that all day-2 operations go
  through `talosctl`/config, not familiar Linux tooling.

## References

- Talos docs + disk-encryption guide (above). Disk encryption on traditional distros:
  [[CONCEPT-CLEVIS_LUKS2]]; Kubespray node OS example: [[CONCEPT-UBUNTU_24_04_K8S]]; K8s window:
  [[CONCEPT-KUBERNETES_VERSION_SUPPORT]].

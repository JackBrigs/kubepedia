---
id: PRACTICE-TALOS_PRODUCTION
type: best_practice
title: "Talos in production — guidelines (HA, secrets, GitOps, security)"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: "1.13.6"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - talos best practices
  - talos production guidelines
  - talos ha control plane
  - talos gitops machine config
  - talos backup secrets
tags:
  - os
  - talos
  - best-practice
  - security
  - ha
sources:
  - type: docs
    path: Talos production notes / guides
    url: https://www.talos.dev/latest/talos-guides/
    note: "HA, disk encryption, extensions, security"
relations:
  - type: see_also
    target: CONCEPT-TALOS_OS_K8S
  - type: see_also
    target: CONCEPT-TALOS_MACHINE_CONFIG
  - type: see_also
    target: CONCEPT-TALOS_UPGRADES
  - type: see_also
    target: CONCEPT-CLEVIS_LUKS2
---

# Talos in production — guidelines (HA, secrets, GitOps, security)

## Summary

Running Talos well is mostly about embracing its **immutable, declarative** model: keep config
as code, protect the cluster's cryptographic identity, and do lifecycle operations one node at
a time. These are the guidelines that prevent the common production mistakes.

## Context

- Applies to Talos **1.13.x** clusters ([[CONCEPT-TALOS_OS_K8S]]). Complements the reference
  docs on config ([[CONCEPT-TALOS_MACHINE_CONFIG]]) and upgrades ([[CONCEPT-TALOS_UPGRADES]]).

## Implementation

**High availability.**

- Run **3 (or 5) control-plane nodes** for etcd quorum; never 2. Expose the API via the
  **control-plane VIP** or an external LB — not a single node's IP.
- Spread control-plane nodes across failure domains; keep etcd on fast disks.

**Protect the cluster identity (most important).**

- **Back up the secrets bundle** (`secrets.yaml`: cluster/etcd CAs, service-account key,
  bootstrap token) in a secret manager. Without it you cannot generate valid configs or recover
  the cluster — this is the #1 irrecoverable mistake.
- Take regular **`talosctl etcd snapshot`** backups (and before every upgrade / risky change).
- Safeguard **`talosconfig`** and **`kubeconfig`** (they grant full control); rotate as needed.

**Manage config as code / GitOps.**

- Keep a **base machine config + per-role/per-node patches** in version control; render with a
  templating tool (community **talhelper**) rather than editing full YAML by hand
  ([[CONCEPT-TALOS_MACHINE_CONFIG]]). The config is declarative source-of-truth — diff and
  review changes like any code.
- `talosctl validate` configs in CI before applying; prefer `--mode try` to test risky changes
  with auto-revert.

**Immutable operations mindset.**

- Don't reach for shell/SSH tuning (there isn't any) — sysctls, kernel args, files, mounts,
  registry mirrors are **config fields**. Add drivers/agents (NVIDIA, iSCSI, etc.) via **system
  extensions** baked into the image, not runtime installs.

**Security.**

- Restrict access to the **Talos API (port 50000)** and to the config/secrets (they contain
  credentials). Enable **disk encryption** for STATE/EPHEMERAL (native LUKS2:
  nodeID/tpm/kms) — the traditional-distro analogue is [[CONCEPT-CLEVIS_LUKS2]].
- Consider **machine-wide image signature verification** (1.13 `ImageVerificationConfig`) and
  keep nodes on a supported Talos↔Kubernetes pairing.

**Lifecycle.**

- Upgrade **one node at a time**, control-plane serially, `talosctl health` between steps; OS
  and Kubernetes upgrades are **separate** and A/B-recoverable ([[CONCEPT-TALOS_UPGRADES]]).

## References

- Talos guides (above); config: [[CONCEPT-TALOS_MACHINE_CONFIG]]; upgrades:
  [[CONCEPT-TALOS_UPGRADES]]; encryption: [[CONCEPT-CLEVIS_LUKS2]]; overview:
  [[CONCEPT-TALOS_OS_K8S]].

---
id: CONCEPT-TALOS_MACHINE_CONFIG
type: concept
title: "Talos machine config — structure, generation, applying, patches"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: "1.13.6"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - talos machine config
  - talosctl gen config
  - talos secrets bundle
  - talos config patch
  - controlplane.yaml worker.yaml
tags:
  - os
  - talos
  - configuration
  - documentation
sources:
  - type: docs
    path: Talos configuration reference
    url: https://www.talos.dev/latest/reference/configuration/
    note: "v1alpha1 Config (machine/cluster) + typed config documents"
  - type: docs
    path: Talos "getting started" / config generation
    url: https://www.talos.dev/latest/introduction/getting-started/
    note: "talosctl gen config, apply-config, bootstrap"
relations:
  - type: see_also
    target: CONCEPT-TALOS_OS_K8S
  - type: see_also
    target: CONCEPT-TALOS_TALOSCTL_WORKFLOW
  - type: see_also
    target: PRACTICE-TALOS_PRODUCTION
---

# Talos machine config — structure, generation, applying, patches

## Summary

On Talos there is **no imperative node setup** — the entire node (and cluster bootstrap) is
described by a declarative **machine config** applied through the API. Understand three things:
its **structure**, how you **generate** it (including the all-important **secrets bundle**), and
how you **apply/patch** it safely.

## Context

- Applies to Talos **1.13.x** ([[CONCEPT-TALOS_OS_K8S]]). The config is the single source of
  truth for a node — back it up and manage it as code ([[PRACTICE-TALOS_PRODUCTION]]).

## Implementation

**Structure.** The core is the `v1alpha1` **Config** with two sections plus optional typed
documents (multi-document YAML separated by `---`):

- **`machine:`** — node-scoped: `type` (`controlplane`|`worker`), `install` (disk, image,
  extensions), `network` (interfaces, VIP, hostname, nameservers), `kubelet`, `certSANs`,
  `sysctls`, `files`, `registries` (mirrors/auth), `disks`/volumes, `features`.
- **`cluster:`** — cluster-scoped: `controlPlane.endpoint` (the API URL/VIP), `clusterName`,
  `network` (podSubnets/serviceSubnets, **`cni`**), `token`, CAs, `apiServer`,
  `controllerManager`, `scheduler`, `etcd`, `inlineManifests`.
- **Typed documents (1.13):** e.g. `KubeSpanConfig`, `ImageVerificationConfig`, volume/user-
  volume configs — added as extra `---` documents alongside the v1alpha1 Config.

**Generation.**

- `talosctl gen config <cluster-name> https://<VIP-or-endpoint>:6443` produces
  **`controlplane.yaml`**, **`worker.yaml`**, and **`talosconfig`** (the client config), plus a
  **secrets bundle** (`talosctl gen secrets -o secrets.yaml`) holding the cluster PKI (cluster
  CA, etcd CA, service-account key, bootstrap token).
- **The secrets bundle is the cluster's identity** — reuse it (`--with-secrets secrets.yaml`) to
  regenerate configs, and **back it up**; losing it means you can no longer produce valid
  configs for that cluster.

**Applying.**

- `talosctl apply-config --nodes <ip> --file controlplane.yaml` with `--mode`:
  - **`auto`** (default) — reboots only if the change requires it;
  - **`no-reboot`** — apply only changes that don't need a reboot (fails otherwise);
  - **`reboot`** — always reboot to apply;
  - **`staged`** — apply on the next boot;
  - **`try`** — apply temporarily with a timeout (auto-revert) to test a change.
- First boot: a node comes up in **maintenance mode** (no config) — apply with `--insecure`
  (no client cert yet), then it uses the config's PKI.

**Patches (keep it DRY).**

- Use **config patches** instead of hand-editing full files: `--config-patch @patch.yaml`
  (RFC6902 JSON or strategic-merge YAML), or `talosctl machineconfig patch`. Pattern: one base
  config + role/node patches (community tool **talhelper** templatizes this).
- Inspect the live config with `talosctl get machineconfig -o yaml`; edit in place with
  `talosctl edit machineconfig` (applies on save).

## Compatibility

- Config schema is versioned (`v1alpha1` + typed docs); new fields arrive per Talos release —
  validate with `talosctl validate --config controlplane.yaml --mode <container|cloud|metal>`.

## References

- Talos configuration reference + getting-started (above). Workflow:
  [[CONCEPT-TALOS_TALOSCTL_WORKFLOW]]; guidelines: [[PRACTICE-TALOS_PRODUCTION]]; overview:
  [[CONCEPT-TALOS_OS_K8S]].

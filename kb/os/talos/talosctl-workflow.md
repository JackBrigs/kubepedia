---
id: CONCEPT-TALOS_TALOSCTL_WORKFLOW
type: concept
title: "talosctl workflow — endpoints/nodes, day-2 commands"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: "1.13.6"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - talosctl commands
  - talosconfig endpoints nodes
  - talosctl dashboard health
  - talosctl get resources
  - talos day 2 operations
tags:
  - os
  - talos
  - operations
  - documentation
sources:
  - type: docs
    path: talosctl CLI reference
    url: https://www.talos.dev/latest/reference/cli/
    note: "full talosctl command reference"
  - type: docs
    path: Talos "what is Talos" / API
    url: https://www.talos.dev/latest/learn-more/architecture/
    note: "apid gRPC API (port 50000), no SSH"
relations:
  - type: see_also
    target: CONCEPT-TALOS_OS_K8S
  - type: see_also
    target: CONCEPT-TALOS_MACHINE_CONFIG
  - type: see_also
    target: TROUBLE-TALOS_APID_UNREACHABLE
---

# talosctl workflow — endpoints/nodes, day-2 commands

## Summary

`talosctl` is the **only** way to operate a Talos node — there is no SSH/shell. It speaks the
**apid gRPC API** (port **50000**, mTLS) using the client cert in **`talosconfig`**. The single
most important concept is **endpoints vs nodes**.

## Context

- Applies to Talos **1.13.x** ([[CONCEPT-TALOS_OS_K8S]]). All examples assume a valid
  `talosconfig` (from `talosctl gen config` — [[CONCEPT-TALOS_MACHINE_CONFIG]]).

## Implementation

**Endpoints vs nodes.**

- **`--endpoints`** — the node(s) `talosctl` connects to (usually control-plane nodes running
  apid).
- **`--nodes`** — the node(s) the command actually targets; the request is **proxied** through
  the endpoint to the target node.
- Set defaults in `talosconfig`: `talosctl config endpoint <cp-ips>` and
  `talosctl config node <ips>`. A command with no `--nodes` targets the configured node(s).

**Core day-2 commands.**

- **Bring-up:** `gen config` / `gen secrets`; `apply-config` (see
  [[CONCEPT-TALOS_MACHINE_CONFIG]]); **`bootstrap`** (run **once**, on **one** control-plane
  node, to initialize etcd); `kubeconfig` (fetch cluster kubeconfig).
- **Inspect:** `health` (cluster health checks); `dashboard` (live TUI); `logs <service>`;
  `dmesg`; `services`; `containers`; **`get <resource>`** (Talos runs on COSI — e.g.
  `get members`, `get addresses`, `get staticpods`, `get machineconfig`); `version`.
- **Lifecycle:** **`upgrade`** (OS image) and **`upgrade-k8s`** (Kubernetes) —
  [[CONCEPT-TALOS_UPGRADES]]; `reboot`; `shutdown`; **`reset`** (wipe a node — careful);
  `rollback` (boot previous image).
- **etcd:** `etcd snapshot <file>` (backup — do this before risky ops), `etcd members`,
  `etcd remove-member`, `etcd defrag`, `etcd status`.

**No shell, so:** to "look inside", use `get`/`logs`/`dmesg`/`containers`; there is no
`kubectl exec`-style access to the host and no package installs — changes go through config.

## Compatibility

- The client (`talosctl`) should match the node's Talos minor within the supported skew;
  mismatches can surface as missing commands/resources. `talosctl` is also used against nodes
  in **maintenance mode** with `--insecure` before a config exists.

## References

- talosctl CLI reference + architecture (above). Config: [[CONCEPT-TALOS_MACHINE_CONFIG]];
  upgrades: [[CONCEPT-TALOS_UPGRADES]]; can't-connect: [[TROUBLE-TALOS_APID_UNREACHABLE]].

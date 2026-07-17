---
id: TROUBLE-TALOS_ETCD_RESTORE
type: troubleshooting
title: "Talos: recover the control plane / etcd from a snapshot (DR)"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: "1.13.6"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - talos etcd restore
  - talos bootstrap recover-from
  - talos disaster recovery
  - talos lost quorum restore snapshot
tags:
  - troubleshooting
  - talos
  - etcd
  - backup
  - disaster-recovery
sources:
  - type: docs
    path: Talos disaster recovery
    url: https://www.talos.dev/latest/advanced/disaster-recovery/
    note: "etcd snapshot + bootstrap --recover-from"
relations:
  - type: see_also
    target: TROUBLE-TALOS_CP_BOOTSTRAP
  - type: see_also
    target: PRACTICE-TALOS_PRODUCTION
  - type: see_also
    target: CONCEPT-TALOS_UPGRADES
---

# Talos: recover the control plane / etcd from a snapshot (DR)

## Summary

You lost etcd quorum (or the whole control plane). Talos recovery differs from a traditional
kubeadm restore: you rebuild etcd from a **`talosctl etcd snapshot`** using **`talosctl
bootstrap --recover-from`**. This requires the **same secrets bundle** — which is why backing it
up is non-negotiable ([[PRACTICE-TALOS_PRODUCTION]]).

## Problem

- Majority of control-plane nodes lost → etcd has no quorum → API read-only/down.
- A single control-plane node died and needs replacing.

## Context

- Applies to Talos **1.13.x**. Precondition: you have a recent **etcd snapshot** and the
  **secrets bundle** + machine configs.

## Diagnostics

**Single member lost (still have quorum):**

1. Identify it: `talosctl -n <cp> get members` / `talosctl etcd members`.
2. Remove the dead member: `talosctl -n <healthy-cp> etcd remove-member <id>`.
3. Bring up a replacement CP node (apply config); it joins etcd. Or `talosctl reset` the failed
   node and re-provision.

**Quorum lost / full DR (restore from snapshot):**

1. Take/locate the latest snapshot (routine: `talosctl -n <cp> etcd snapshot db.snapshot`).
2. Wipe/reset the control-plane nodes (or provision fresh ones) using the **same secrets
   bundle** and configs, so identities/PKI match.
3. On **one** control-plane node, restore etcd from the snapshot:
   **`talosctl bootstrap --recover-from=./db.snapshot`** (run **once**, like a normal bootstrap
   — [[TROUBLE-TALOS_CP_BOOTSTRAP]]).
4. Verify: `talosctl health`, `talosctl etcd status`, API responds.
5. Add the remaining control-plane nodes; they join the restored etcd.

## Known Issues

- **No secrets bundle = no recovery** — a snapshot alone can't rebuild the cluster without the
  matching CAs/keys. Store both.
- Take snapshots **before every upgrade / risky change** ([[CONCEPT-TALOS_UPGRADES]]); a
  snapshot is only as good as its age.
- Don't run `bootstrap`/`--recover-from` on more than one node (split etcd).

## References

- Talos disaster-recovery guide (above); bootstrap: [[TROUBLE-TALOS_CP_BOOTSTRAP]]; guidelines:
  [[PRACTICE-TALOS_PRODUCTION]]; upgrades: [[CONCEPT-TALOS_UPGRADES]].

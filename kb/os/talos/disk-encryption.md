---
id: CONCEPT-TALOS_DISK_ENCRYPTION
type: concept
title: "Talos disk encryption (native LUKS2) — providers, config, rotation"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: "1.13.6"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - talos systemDiskEncryption
  - talos luks2 nodeid tpm kms
  - talos state ephemeral encryption
  - talos encrypt disk config
tags:
  - os
  - talos
  - security
  - encryption
  - documentation
sources:
  - type: docs
    path: Talos disk encryption guide
    url: https://www.talos.dev/latest/talos-guides/configuration/disk-encryption/
    note: "machine.systemDiskEncryption: state/ephemeral, key providers"
relations:
  - type: see_also
    target: CONCEPT-TALOS_OS_K8S
  - type: see_also
    target: CONCEPT-TALOS_MACHINE_CONFIG
  - type: see_also
    target: CONCEPT-CLEVIS_LUKS2
---

# Talos disk encryption (native LUKS2) — providers, config, rotation

## Summary

Talos encrypts node partitions with **LUKS2 natively**, configured declaratively under
**`machine.systemDiskEncryption`** — no Clevis/initramfs plumbing. It's the Talos equivalent of
[[CONCEPT-CLEVIS_LUKS2]] on traditional distros, with four **key providers**: `nodeID`,
`static`, `tpm`, `kms`.

## Context

- Applies to Talos **1.13.x** ([[CONCEPT-TALOS_OS_K8S]]); set via machine config
  ([[CONCEPT-TALOS_MACHINE_CONFIG]]). Protects data **at rest** (stolen/decommissioned disks) —
  not a running node.

## Implementation

**What can be encrypted.** Two partitions, each configured independently:

- **`state`** — the STATE partition (holds the machine config / node secrets).
- **`ephemeral`** — the EPHEMERAL partition (`/var`: container data, **etcd** on control-plane
  nodes). Encrypt both for full at-rest protection.

**Config shape** (`machine.systemDiskEncryption.<state|ephemeral>`): `provider: luks2` plus a
list of **`keys`** (each key is a LUKS2 keyslot). Key providers:

- **`nodeID`** — key **derived from the node's identity** (hardware UUID + partition). Zero
  external dependencies; a disk moved to a **different** machine won't decrypt. Good default for
  bare metal without a TPM/KMS.
- **`static`** — a fixed `passphrase`. Simple but the secret lives in the config — protect the
  config accordingly.
- **`tpm`** — sealed to the node's **TPM2** (optionally to SecureBoot/PCR state). Unlocks only
  on the same, unmodified machine; a firmware/boot change can invalidate it (re-seal after
  intentional changes).
- **`kms`** — key served by a **network KMS** at boot (Talos KMS API). Central control and
  **revocation**, but adds a **boot-time network dependency** (like Tang for Clevis).

Multiple keys = multiple keyslots, so you can combine (e.g. `tpm` + a `static`/`kms` fallback)
for resilience.

**Rotation / changes.** Edit the `keys` in the config and `apply-config`; Talos manages the
LUKS2 keyslots. Adding a fallback key before removing an old one avoids lockout.

## Compatibility

- **`nodeID` vs `tpm`:** both bind to the machine; `tpm` additionally measures boot state.
  **`kms`/`static`** allow moving a disk if the key is available — pick per threat model.
- Encrypting `ephemeral` protects **etcd** at rest on control-plane nodes — recommended.
- Enabling encryption on an existing node reprovisions the partition — plan for data loss on
  EPHEMERAL unless done at install.

## References

- Talos disk-encryption guide (above); traditional-distro analogue: [[CONCEPT-CLEVIS_LUKS2]];
  config: [[CONCEPT-TALOS_MACHINE_CONFIG]]; overview: [[CONCEPT-TALOS_OS_K8S]].

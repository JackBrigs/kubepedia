---
id: CONCEPT-CLEVIS_LUKS2
type: concept
title: "Clevis + LUKS2 — automated disk encryption for Kubernetes nodes"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: verified
aliases:
  - clevis luks2
  - luks2 encryption kubernetes nodes
  - network bound disk encryption
  - nbde tang
  - tpm2 luks auto unlock
  - encryption at rest nodes
tags:
  - os
  - security
  - encryption
  - luks
  - nodes
sources:
  - type: docs
    path: Clevis (automated decryption framework)
    url: https://github.com/latchset/clevis
    note: pins (tang/tpm2/sss), clevis luks bind/unlock
  - type: docs
    path: Tang / NBDE
    url: https://github.com/latchset/tang
    note: network-bound disk encryption server
  - type: docs
    path: cryptsetup LUKS2
    url: https://gitlab.com/cryptsetup/cryptsetup
    note: LUKS2 on-disk format (Argon2, multiple keyslots)
relations:
  - type: see_also
    target: CONCEPT-TALOS_OS_K8S
  - type: see_also
    target: CONCEPT-UBUNTU_24_04_K8S
  - type: see_also
    target: CONCEPT-ADDON_ROOK_CEPH
---

# Clevis + LUKS2 — automated disk encryption for Kubernetes nodes

## Summary

**LUKS2** is the modern Linux disk-encryption format; **Clevis** automates unlocking it at boot
**without** a stored key or a human typing a passphrase — essential for unattended reboots of
Kubernetes nodes (autoscaling, HA). On traditional distros (Kubespray nodes: Ubuntu/Debian/
RHEL-family), this is the standard way to get **encryption at rest** for node root/data disks
and for storage-backend disks (Ceph OSDs, local PVs). It is the traditional-distro counterpart
to Talos's built-in LUKS2 ([[CONCEPT-TALOS_OS_K8S]]).

## Context

- Applies at the **node OS** layer (adjacent domain), independent of Kubernetes version; the
  benefit is data-at-rest protection for stolen/decommissioned disks — it does **not** protect a
  running node.
- Relevant to any encrypted-storage design: encrypting the disks under **Ceph OSDs**
  ([[CONCEPT-ADDON_ROOK_CEPH]]) or local-PV volumes, and the node's own data partition.

## Implementation

**LUKS2.** The successor to LUKS1: default in modern `cryptsetup`, uses the memory-hard
**Argon2** KDF, supports multiple **keyslots** and richer metadata. A volume is created with
`cryptsetup luksFormat --type luks2 <dev>`; a passphrase or key unlocks a keyslot.

**Clevis pins** (each binds an extra LUKS2 keyslot that unlocks automatically):

- **`tang`** — **Network-Bound Disk Encryption (NBDE):** the node fetches key material from one
  or more **Tang** servers over HTTP at boot. No secret is stored on the node; security comes
  from **network reachability** of Tang (the disk only decrypts on the trusted network).
  `clevis luks bind -d <dev> tang '{"url":"http://tang.example"}'`.
- **`tpm2`** — seals the key to the node's **TPM2**, optionally to specific **PCRs** (firmware/
  boot-measurement state). Unlocks only on the same, unmodified machine.
- **`sss`** — **Shamir Secret Sharing:** combine several pins with a **threshold** (e.g. "any 1
  of {tang, tpm2}", or "2 of 3") for resilience — so a single Tang outage or a TPM change
  doesn't lock you out.

**Boot unlock.** Clevis integrates with the **initramfs (dracut)** or a **systemd**
unlocker so the encrypted volume opens before the root/data mount — no interactive passphrase.

## Compatibility

- **Kubespray nodes:** Kubespray does not configure LUKS/Clevis itself — provision it via the
  node image / a preinstall step / your own Ansible, then run Kubespray on top. Talos nodes use
  the **native** LUKS2 config instead ([[CONCEPT-TALOS_OS_K8S]]).
- **Failure modes to plan for:**
  - **Tang unreachable at boot** → the node hangs waiting for a passphrase (no auto-unlock).
    Run redundant Tang servers and/or an `sss` threshold so one outage doesn't block boot.
  - **TPM2 PCR change** (firmware/kernel/boot update) → the `tpm2` pin fails to unseal; re-bind
    after intentional changes, or bind to stable PCRs, or use `sss` with a Tang fallback.
  - **Key rotation / server move:** re-run `clevis luks bind`/`regen` when Tang keys rotate.
- **Performance:** modern CPUs have AES-NI, so LUKS2 overhead is small; still validate under
  I/O-heavy storage (etcd, Ceph) before production.

## References

- Clevis, Tang/NBDE, cryptsetup LUKS2 (above). Talos-native encryption:
  [[CONCEPT-TALOS_OS_K8S]]; node OS: [[CONCEPT-UBUNTU_24_04_K8S]]; storage backend:
  [[CONCEPT-ADDON_ROOK_CEPH]].

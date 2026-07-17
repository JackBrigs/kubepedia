---
id: CONCEPT-TALOS_PROVISIONING
type: concept
title: "Talos provisioning — Image Factory, ISO/PXE, maintenance mode"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: "1.13.6"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - talos bare metal provisioning
  - talos pxe ipxe netboot
  - talos iso install
  - talos maintenance mode install
  - sidero metal omni
tags:
  - os
  - talos
  - provisioning
  - bare-metal
  - documentation
sources:
  - type: docs
    path: Talos bare-metal / installation
    url: https://www.talos.dev/latest/talos-guides/install/bare-metal-platforms/
    note: "ISO, PXE/iPXE, disk images, maintenance mode"
  - type: docs
    path: Sidero Omni / Metal
    url: https://www.siderolabs.com/platform/saas-for-kubernetes/
    note: "managed bare-metal / cluster lifecycle (optional)"
relations:
  - type: see_also
    target: CONCEPT-TALOS_OS_K8S
  - type: see_also
    target: CONCEPT-TALOS_SYSTEM_EXTENSIONS
  - type: see_also
    target: CONCEPT-TALOS_MACHINE_CONFIG
---

# Talos provisioning — Image Factory, ISO/PXE, maintenance mode

## Summary

Getting Talos onto machines has three parts: **build an image** (with the extensions/kernel
args you need), **boot** it (ISO, PXE/iPXE, or a cloud disk image), and **apply the config** —
a freshly-booted node sits in **maintenance mode** until you do.

## Context

- Applies to Talos **1.13.x** ([[CONCEPT-TALOS_OS_K8S]]). Image content comes from the Factory /
  extensions ([[CONCEPT-TALOS_SYSTEM_EXTENSIONS]]); the config from
  [[CONCEPT-TALOS_MACHINE_CONFIG]].

## Implementation

**Build the boot media.**

- **Image Factory** (factory.talos.dev) or `imager` produces, per **schematic**: an **ISO**, an
  **installer image**, **PXE/iPXE** assets (kernel + initramfs + boot script), disk images
  (cloud), and SecureBoot variants.

**Boot methods.**

- **ISO / USB / virtual media** — good for a few machines or labs.
- **PXE / iPXE (netboot)** — for fleets: a DHCP + TFTP/HTTP setup (or **matchbox**) serves the
  Talos kernel/initramfs; the node boots into Talos and you then apply config. Scales to many
  machines.
- **Cloud** — use the platform disk image; pass config via user-data/metadata.
- **Managed metal** — **Sidero Metal** / **Omni** provide full bare-metal + cluster lifecycle
  (Cluster API, PXE, config management) if you don't want to run your own netboot stack.

**Apply config (maintenance mode).**

1. A node with no config boots into **maintenance mode** (only apid, no cluster PKI).
2. `talosctl apply-config --insecure --nodes <maint-ip> --file controlplane.yaml|worker.yaml`.
3. Talos **installs to the disk** (`machine.install.disk`) and reboots into the installed
   system; from then on it uses the cluster PKI (no more `--insecure`).
4. First control-plane node: run **`talosctl bootstrap`** once ([[TROUBLE-TALOS_CP_BOOTSTRAP]]).

## Compatibility

- **Immutable install:** the install disk must be correct and persistent; changing extensions
  or kernel args later means booting/upgrading to a **new image** ([[CONCEPT-TALOS_SYSTEM_EXTENSIONS]]),
  not editing the running node.
- SecureBoot + TPM disk encryption require the matching SecureBoot image from the Factory.

## References

- Talos bare-metal install docs + Sidero (above); extensions:
  [[CONCEPT-TALOS_SYSTEM_EXTENSIONS]]; config: [[CONCEPT-TALOS_MACHINE_CONFIG]]; overview:
  [[CONCEPT-TALOS_OS_K8S]].

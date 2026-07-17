---
id: CONCEPT-TALOS_SYSTEM_EXTENSIONS
type: concept
title: "Talos system extensions — drivers/agents on an immutable OS"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: "1.13.6"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - talos system extensions
  - talos image factory
  - talos nvidia extension
  - talos extensionserviceconfig
  - talos schematic
tags:
  - os
  - talos
  - extensions
  - documentation
sources:
  - type: docs
    path: Talos system extensions
    url: https://www.talos.dev/latest/talos-guides/configuration/system-extensions/
    note: "extensions baked at image build; ExtensionServiceConfig"
  - type: docs
    path: Talos Image Factory
    url: https://factory.talos.dev/
    note: "build custom images/ISO/PXE with chosen extensions (schematic ID)"
relations:
  - type: see_also
    target: CONCEPT-TALOS_OS_K8S
  - type: see_also
    target: CONCEPT-TALOS_PROVISIONING
  - type: see_also
    target: CONCEPT-TALOS_UPGRADES
---

# Talos system extensions — drivers/agents on an immutable OS

## Summary

Because Talos has **no package manager**, extra drivers, tools and agents are added as **system
extensions** — baked into the OS **image at build time**, not installed at runtime. You select
them via the **Image Factory** (or `imager`) which produces a custom image identified by a
**schematic ID**.

## Context

- Applies to Talos **1.13.x** ([[CONCEPT-TALOS_OS_K8S]]). Extensions are how you get things a
  Kubespray node would `apt install` (GPU drivers, iSCSI, guest agents).

## Implementation

**Building an image with extensions.**

- Use **factory.talos.dev** (Image Factory): pick base + extensions (+ kernel args/SecureBoot);
  it returns an **installer image / ISO / PXE assets** tied to a **schematic ID**. Or run the
  `imager` container locally.
- Common extensions (`siderolabs/*`): `nonfree-kmod-nvidia` + `nvidia-container-toolkit` (GPU),
  `iscsi-tools` (iSCSI/Longhorn), `util-linux-tools`, `qemu-guest-agent` (VMs), `gvisor`,
  `tailscale`, `drbd`, `zfs`.

**Applying / changing extensions.**

- A node runs the extensions present in its **image** — to add/remove one you build a new image
  and **`talosctl upgrade --image <factory-image-for-new-schematic>`** ([[CONCEPT-TALOS_UPGRADES]]).
  You can't add an extension to a running node without upgrading its image.
- Verify with `talosctl get extensions`.

**Extension services.**

- Some extensions run as **services** managed by Talos; configure them with an
  **`ExtensionServiceConfig`** document in the machine config (a typed `---` document).

## Compatibility

- Extensions are **version-matched to the Talos release** — the Factory builds them for the
  target Talos version; on upgrade, the new image carries the extensions for that version.
- GPU nodes: the NVIDIA extensions replace the traditional host driver install; pair with the
  in-cluster GPU Operator/toolkit as appropriate ([[CONCEPT-ADDON_GPU_OPERATOR]]).

## References

- Talos system-extensions guide + Image Factory (above); provisioning:
  [[CONCEPT-TALOS_PROVISIONING]]; upgrades: [[CONCEPT-TALOS_UPGRADES]]; overview:
  [[CONCEPT-TALOS_OS_K8S]].

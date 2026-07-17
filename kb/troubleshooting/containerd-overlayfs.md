---
id: TROUBLE-CONTAINERD_OVERLAYFS
type: troubleshooting
title: "containerd: overlayfs snapshotter fails to mount"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: verified
aliases:
  - failed to mount overlay operation not permitted
  - overlayfs snapshotter cannot be enabled
  - fuse-overlayfs native snapshotter
  - containerd data root overlay
tags:
  - troubleshooting
  - containerd
  - storage
  - snapshotter
sources:
  - type: docs
    path: containerd overlay mount failure
    url: https://github.com/containerd/containerd/issues/5464
    note: "overlay not permitted at data root; fuse-overlayfs/native"
  - type: docs
    path: k3s overlay on data-dir
    url: https://github.com/k3s-io/k3s/issues/12673
relations:
  - type: see_also
    target: COMPONENT-CONTAINERD
---

# containerd: overlayfs snapshotter fails to mount

## Summary

containerd won't start pods because the **overlayfs snapshotter** can't mount at its data root:
`"overlayfs" snapshotter cannot be enabled for "/var/lib/.../containerd" ... failed to mount
overlay: operation not permitted` (or `invalid argument`). The kernel is rejecting the overlay
mount there.

## Problem

- Startup/error: `failed to mount overlay: operation not permitted` / `invalid argument`;
  images won't unpack; pods stuck.

## Context

- Applies to containerd on Kubernetes **1.29–1.35** ([[COMPONENT-CONTAINERD]]); also common on
  K3s/nested/WSL2 setups.

## Diagnostics

- **Why the kernel rejects it:** an **unprivileged/user-namespaced** container or **WSL2**
  blocking overlay; the **data root itself is on overlayfs** (nested overlay `upperdir` is
  unsupported); or a **backing FS** (some ZFS/NFS) can't be an overlay `upperdir`.
- **Fixes:**
  - Move `/var/lib/containerd` (or k3s `--data-dir`) to a **native ext4/xfs** volume (not
    overlay/NFS/unsupported-ZFS).
  - Or switch snapshotter: **`--snapshotter=fuse-overlayfs`** or **`native`** (slower, but
    works without kernel overlay).
  - Ensure the overlay module is available: `modprobe overlay`.

## Known Issues

- `native` snapshotter uses far more disk/IO (full copy per layer) — a fallback, not a default.

## References

- containerd #5464, k3s #12673 (above); component: [[COMPONENT-CONTAINERD]].

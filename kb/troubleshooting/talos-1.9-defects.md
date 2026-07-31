---
id: TROUBLE-TALOS_1_9_DEFECTS
type: troubleshooting
title: "talos 1.9: defects fixed in the 1.9 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.9.0 <1.10.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - talos 1.9 known issues
  - talos 1.9 fixed in
  - is this talos bug already fixed
tags:
  - troubleshooting
  - upgrade
  - talos
sources:
  - type: docs
    path: siderolabs/talos release notes for the 1.9 line — bug-fix entries
    url: https://github.com/siderolabs/talos/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# talos 1.9: defects fixed in the 1.9 line

## Summary

**68 defects** the project fixed across **7 releases** of the 1.9 line, from 1.9.0 to
1.9.6. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.9.0

- fix: match MAC addresses case-insensitive (nocloud)
- fix: order volume config by the requested size
- fix: avoid nil-pointer-panic in `RegistriesConfigController`
- fix: power on the machine on reboot request in qemu power api
- fix: lock provisioning order of user disk partitions
- fix: don't reset health status if service doesn't support health checks
- fix: multiple small fixes for service runners
- fix: multiple issues with opening encrypted volumes
- fix: make `system_disk` condition work properly before install
- fix: nocloud network link matching on MAC addresses
- fix: make Talos META partition match more precise
- fix: properly halt installation if Talos already installed
- fix: return proper number from the `timeStampWriter`
- fix: systemd-udevd restore old naming behavior
- fix: make immage cache config apply immediately
- fix: add directory entries and filemode to tarball
- fix: make vmware platform common code build on all arches
- fix: don't activate LVM volumes in agent mode
- fix: register controlplane node with NoSchedule taint
- fix: arch linux search paths and names for QEMU provisioner
- fix: use imager incoming version for extension validation
- fix(ci): skip test if `UserNamespacesSupport` feature gate is not set
- fix: update permissions for logging directories in /var
- fix: mount /sys/kernel/security conditionally
- fix: use more correct condition to skip generating hosts files
- fix: do not trim 0 from process SELinux label
- fix: wait for udevd to be running before activating LVM
- fix: rework the 'metal-iso' config acquisition
- fix: improve error messages for invalid bridge/bond configuration
- fix: update incorrect alias for PCIDevice resource
- fix: do not use pflag csv comma reader for config-patch
- fix: wipe system partitions correctly via kernel args
- fix: do not stop udevd before unmounting volumes
- fix: prevent file descriptors leaks to child processes
- fix: filter out non-printable characters in process line
- fix: strategic merge patch delete for map keys
- fix: remove extra logging on ethtool ioctl failures
- fix: return an error on process nonzero exit code
- fix: update deprecations based on Kubernetes 1.32.0-alpha.3
- fix: add CONFIG_INTEL_MEI_GSC_PROXY as module
- feat: update systemd to 256.8, fix cpuset/cgroupsv1
- fix: do not build unneeded utilities and man for SELinux libraries
- fix: enable nvme and 2.5gbit ethernet on nanopi-r5s
- fix: libselinux: support running without /etc/selinux
- fix: systemd-udevd: search for config in /usr/etc
- fix: force LVM to use `/run` as state directory
- fix: bump gettext-tiny to the latest dev version

### 1.9.1

- fix: ignore member not found error on leave cluster
- fix: fix `Failed to initialize SELinux labeling handle` udev error
- fix: make talosctl time work with PTP time sync

### 1.9.2

- fix: add informer resync period for node status watcher
- fix: merge of VolumeConfig documents with sizes
- fix: partition alignment on disks with 4k sectors
- fix: request previous IP address in discovery
- fix: mount selinuxfs only when SELinux is enabled
- fix: update field name for bus path disk selector
- fix: exclude disks with empty transport for disk selector
- fix: adjust kernel options around ACPI/PCI/EFI
- fix: update config-arm64 to add Rasperry Pi watchdog support
- fix: dvb was missing I2C_MUX support and si2168 driver

### 1.9.3

- fix: disks with 4k sector size and systemd-boot
- fix: ignore forbidden error when waiting for pod eviction

### 1.9.4

- fix: make ingress firewall filter traffic to nodeports

### 1.9.5

- fix: handle dynamic HTTP proxy settings for discovery client
- fix: ignore digest part of images when checking version

### 1.9.6

- fix: do correct backoff for nocloud reconcile
- fix: ignore missing config (nocloud) via cidata
- fix: reconnect on SideroLink tunnel on/off change


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.9.6**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `siderolabs/talos`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/talos.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].

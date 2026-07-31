---
id: TROUBLE-TALOS_1_6_DEFECTS
type: troubleshooting
title: "talos 1.6: defects fixed in the 1.6 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.6.0 <1.7.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - talos 1.6 known issues
  - talos 1.6 fixed in
  - is this talos bug already fixed
tags:
  - troubleshooting
  - upgrade
  - talos
sources:
  - type: docs
    path: siderolabs/talos release notes for the 1.6 line — bug-fix entries
    url: https://github.com/siderolabs/talos/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# talos 1.6: defects fixed in the 1.6 line

## Summary

**76 defects** the project fixed across **9 releases** of the 1.6 line, from 1.6.0 to
1.6.8. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.6.0

- fix: leave discovery service later in the reset sequence
- fix: add a KubeSpan option to disable extra endpoint harvesting
- fix: talosctl cluster create not to enforce kubeprism always
- fix: store and execute desired action on emergency action
- fix: trim leading spaces\newlines in inline manifest contents
- fix: skip writing the file if the contents haven't changed
- fix: do not panic in `merge.Merge` if map value is nil
- fix: initialize boot assets with defaults early
- fix: pick etcd adverised addresses from 'current' addresses
- fix: support slices of enums and fix NfTablesConntrackStateMatch
- fix: ignore kernel command line in container mode
- fix: allow rootfs propagation configuration for extension services
- fix: allow extra kernel args for secureboot installer
- fix: don't validate machine.install if installed
- fix: use custom Talos/kernel version when generating UKI
- fix: when writing to META in the installer/imager, use fixed name
- fix: make Talos work on Rockpi 4c boards again
- fix: don't use runtime-specs Mount struct in machine config
- fix: handle secure boot state policy pcr digest error
- fix: use tpm2 hash algorithm constants and allow non-SHA-256 PCRs
- fix: clear the encryption config in META when STATE is reset
- fix: the node IP for kubelet shouldn't change if nothing matches
- fix: update kubernetes library to support 1.29 upgrades
- fix: generate of modules.dep when on the machine
- fix: build CPU ucode correctly for early loader
- fix: set default route priority for hcloud platform
- fix: handle correctly change of listen address for maintenance service
- fix: shorten VLAN link names to fit into the limit of 15 characters
- fix: allow network device selector to match multiple links
- fix: update kubernetes library for 1.28 upgrade pre-checks
- fix: set correct (1 year) talosconfig expiration
- fix: set proper timeouts for KubePrism loadbalancer
- fix: use a mount prefix when installing a bootloader
- fix: properly calculate overal of node address with subnet filters
- fix: prevent dashboard crashes when process info is not available
- fix: properly GC images supplied with both tag and digest
- fix: automatically change `rpi_4` board on upgrade
- fix: use image digest when starting a container
- fix: make encryption config provider default to `luks2` if not set
- fix: fast-wipe the system disk on talosctl reset
- fix: revert: update grub to fix loading large initramfs
- fix: update grub to fix loading large initramfs

### 1.6.1

- fix: update the way secureboot signer fetches certificate (azure)
- fix: use correct prefix when installing SBC files

### 1.6.2

- fix: strategic patch merging for audit policy
- fix: fix .der output in `talosctl gen secureboot`
- fix: support KubePrism settings in Kubernetes Discovery
- fix: merge ports and ingress configs correctly in NetworkRuleConfig
- fix: fix nodes on dashboard footer when node names are used in `--nodes`
- fix: disk UUID & WWID always empty in `talosctl disks`
- fix: replace the filemap implementation to not buffer in memory
- fix: imager should support different Talos versions
- fix: decode escape sequences while reading from kmsg

### 1.6.3

- fix: allow META encoded values to be compressed

### 1.6.4

- fix: take into account the moment seen when cleaning up CRI images
- fix: be more tolerant to error handling in Mounts API
- fix: run the interactive installer loop to report errors
- fix: always print the login URL on key renew flow
- fix: support validating signatures generated with the time in the future

### 1.6.5

- fix: use MachineStatus resource to check for boot done
- fix: ensure that Talos runs in a pod (container)
- fix: run xfs_repair on invalid argument error
- fix: use a separate cgroup for each extension service

### 1.6.6

- fix: workaround a race in CNI setup (talosctl cluster create)
- fix: provide auth when pulling images in the imager
- fix: handle errors to watch apid/trustd certs

### 1.6.7

- fix: patch correctly config in `talosctl upgrade-k8s`
- fix: remove maintenance config when maintenance service is shut down
- fix: fix nil panic on maintenance upgrade with partial config

### 1.6.8

- fix: check for `nil` machine config during installation
- fix: do not fail cli action tracker when boot id cannot be read
- fix: bump priority of OpenStack routes if IPv6 and default gateway
- fix: return proper value from Bridge.STP instead of plain nil
- fix: assign different priority to IPv6 default gateway on OpenStack
- fix: make static pods check output consistent
- fix: don't announce the VIP on acquire failure


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.6.8**, the newest release recorded here for this line.

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

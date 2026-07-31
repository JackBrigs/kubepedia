---
id: TROUBLE-TALOS_1_8_DEFECTS
type: troubleshooting
title: "talos 1.8: defects fixed in the 1.8 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.8.0 <1.9.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - talos 1.8 known issues
  - talos 1.8 fixed in
  - is this talos bug already fixed
tags:
  - troubleshooting
  - upgrade
  - talos
sources:
  - type: docs
    path: siderolabs/talos release notes for the 1.8 line — bug-fix entries
    url: https://github.com/siderolabs/talos/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# talos 1.8: defects fixed in the 1.8 line

## Summary

**80 defects** the project fixed across **5 releases** of the 1.8 line, from 1.8.0 to
1.8.4. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.8.0

- fix: filter out non-printable characters in process line
- fix: strategic merge patch delete for map keys
- fix: remove extra logging on ethtool ioctl failures
- fix: never unarchive initramfs when loading boot assets in talosctl
- fix: report internally service as unhealthy if not running
- fix: report errors correctly when pulling, fix EEXIST
- fix: merge extension service config files by `mountPath`
- fix: always handle `PermissionDenied` in dashboard resource watches
- fix: bind HostDNS to 169.254.x link-local address
- fix: retry with another upstream if the previous failed
- fix: add dns-resolve-cache to the support bundle
- fix: fix graph diffs in dashboard when node aliases are used
- fix: update containerd configuration and settings
- fix: enforce secureboot enroll option only for supported releases
- fix: be more smart when merging DNS resolver config
- fix: sort ports and merge adjacent ones in the nft rule
- fix: change the UEFI firmware search path order
- fix: remove host bind mount for `/tmp` for trustd
- fix: properly output multi-doc machine config in `get mc`
- fix: detect CD devices, fix user disks wipe test
- fix: initial assignment of Hetzner Cloud Alias IP
- fix: update the cgroups for Talos core services
- fix: add upgrade errata for arm64/zboot kernels
- fix: correct time adjustment in `time.SyncController`
- fix: replace `nslookup` with `dig` in integration tests
- fix: correctly handle dns messages in our dns implementation
- fix: produce stable order of bonds with equinix
- fix(ci): fix crons by setting up buildx always
- fix: decrease maximum negative ttl for dns responses
- fix: update go-tail library to fix 'short read' error
- fix: update github.com/siderolabs/siderolink to v0.3.7
- fix: don't enable hostDNS for versions of Talos which do not have it
- fix: check for `nil` machine config during installation
- fix: add cluster name to the worker machine config
- fix: do not fail cli action tracker when boot id cannot be read
- fix: allow more flags in `talosctl cluster create --input-dir`
- fix: wait for devices to be discovered before probing filesystems
- fix: add endpoints for "virtual" `host-dns` service
- fix: bump priority of OpenStack routes if IPv6 and default gateway
- fix: return proper value from Bridge.STP instead of plain nil
- fix: close apid inter-backend connections gracefully for real
- fix: assign different priority to IPv6 default gateway on OpenStack
- fix: generate secureboot ISO .der certificate correctly
- fix: make static pods check output consistent
- fix: validate that workers don't get cluster CA key
- fix: reconnect to the logs stream in dashboard after reboot
- fix: present all accepted CAs to the kube-apiserver
- fix: close the apid connection to other machines gracefully
- fix: pre-create nftables chain to make kubelet use nftables
- fix: account for time truncation to a second resolution
- fix: get rid of data race in the key sign interceptor
- fix: add one more removed feature gate for 1.31
- fix: stop decoding without error if EOF encountered during header read
- fix: add `dns-resolve-cache` to the list of logs gathered
- fix(kernel): array-index-out-of-bounds error on bpf
- fix: enable CONFIG_PROC_CHILDREN for amd64 kernel
- fix: disable CONFIG_EFI_DISABLE_PCI_DMA option
- fix: add missing test and proper check for `map[string]interface{}`
- fix: support pointer to structs in marshal/unmarshal
- fix: do not ever skip updates which have remove flag

### 1.8.1

- fix: wipe system partitions correctly via kernel args
- fix: prevent file descriptors leaks to child processes
- fix: force LVM to use `/run` as state directory

### 1.8.2

- fix: wait for udevd to be running before activating LVM
- fix: rework the 'metal-iso' config acquisition
- fix: improve error messages for invalid bridge/bond configuration
- fix: update incorrect alias for PCIDevice resource
- fix: do not use pflag csv comma reader for config-patch

### 1.8.3

- fix: arch linux search paths and names for QEMU provisioner
- fix: update permissions for logging directories in /var
- fix: mount /sys/kernel/security conditionally
- fix: do not trim 0 from process SELinux label
- fix: enable nvme and 2.5gbit ethernet on nanopi-r5s

### 1.8.4

- fix: order volume config by the requested size
- fix: lock provisioning order of user disk partitions
- fix: don't reset health status if service doesn't support health checks
- fix: make `system_disk` condition work properly before install
- fix: nocloud network link matching on MAC addresses
- fix: properly halt installation if Talos already installed
- fix: make vmware platform common code build on all arches


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.8.4**, the newest release recorded here for this line.

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

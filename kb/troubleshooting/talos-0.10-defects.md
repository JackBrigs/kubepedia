---
id: TROUBLE-TALOS_0_10_DEFECTS
type: troubleshooting
title: "talos 0.10: defects fixed in the 0.10 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.10.0 <0.11.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - talos 0.10 known issues
  - talos 0.10 fixed in
  - is this talos bug already fixed
tags:
  - troubleshooting
  - upgrade
  - talos
sources:
  - type: docs
    path: siderolabs/talos release notes for the 0.10 line — bug-fix entries
    url: https://github.com/siderolabs/talos/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# talos 0.10: defects fixed in the 0.10 line

## Summary

**171 defects** the project fixed across **5 releases** of the 0.10 line, from 0.10.0 to
0.10.4. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.10.0

- u-boot version was updated to fix the boot and USB issues on Raspberry Pi 4 8GiB version
- fix: update osType in OVA other3xLinux64Guest"
- fix: update etcd client errors, print etcd join failures
- fix: zero out manifest contents before setting new value
- fix: check retryable network errors by interface
- fix: trim endpoints/nodes from arguments in talosctl config
- fix: revert mark PMBR EFI partition as bootable
- fix: require leader on etcd member operations
- fix: add a check for overlay mounts in installer pre-flight checks
- fix: publish rockpi4 image to release artifacts
- fix: create rootfs for system services via /system tmpfs
- fix: retry Kubernetes API errors on cordon/uncordon/etc
- fix: ignore EOF errors from Kubernetes API when converting control plane
- fix: workaround race in containerd runner with stdin pipe
- fix: get rid of data race in encoder and fix concurrent map access
- fix: prevent panic in validate config if `machine.install` is missing
- fix: allow `convert-k8s --remove-initialized-keys` with K8s cp is down
- fix: resolve the issue with Kubernetes upgrade
- fix: resolve the issue with DHCP lease not being renewed
- fix: config validation: CNI should apply to cp nodes, encryption config
- fix: command `etcd remove-member` shouldn't remove etcd data directory
- fix: build rockpi4 metal image as part of CI build
- fix: upgrade-k8s bug with empty config values and provision script
- fix: talosctl health should not check kube-proxy when it is disabled
- fix: properly format spec comments in the resources
- fix: don't touch any partitions on upgrade with --preserve
- fix: move containerd CRI config files under `/var/`
- fix: revert mark the EFI partition in PMBR as bootable
- fix: mark the EFI partition in PMBR as bootable

### 0.10.1

- u-boot version was updated to fix the boot and USB issues on Raspberry Pi 4 8GiB version
- fix: bump crypto library for the CSR verification fix
- fix: use both self-signed and Kubernetes CA to verify Kubelet cert
- fix: update osType in OVA other3xLinux64Guest"
- fix: update etcd client errors, print etcd join failures
- fix: zero out manifest contents before setting new value
- fix: check retryable network errors by interface
- fix: trim endpoints/nodes from arguments in talosctl config
- fix: revert mark PMBR EFI partition as bootable
- fix: require leader on etcd member operations
- fix: add a check for overlay mounts in installer pre-flight checks
- fix: publish rockpi4 image to release artifacts
- fix: create rootfs for system services via /system tmpfs
- fix: retry Kubernetes API errors on cordon/uncordon/etc
- fix: ignore EOF errors from Kubernetes API when converting control plane
- fix: workaround race in containerd runner with stdin pipe
- fix: get rid of data race in encoder and fix concurrent map access
- fix: prevent panic in validate config if `machine.install` is missing
- fix: allow `convert-k8s --remove-initialized-keys` with K8s cp is down
- fix: resolve the issue with Kubernetes upgrade
- fix: resolve the issue with DHCP lease not being renewed
- fix: config validation: CNI should apply to cp nodes, encryption config
- fix: command `etcd remove-member` shouldn't remove etcd data directory
- fix: build rockpi4 metal image as part of CI build
- fix: upgrade-k8s bug with empty config values and provision script
- fix: talosctl health should not check kube-proxy when it is disabled
- fix: properly format spec comments in the resources
- fix: don't touch any partitions on upgrade with --preserve
- fix: move containerd CRI config files under `/var/`
- fix: verify CSR signature before issuing a certificate
- fix: revert mark the EFI partition in PMBR as bootable
- fix: mark the EFI partition in PMBR as bootable

### 0.10.2

- u-boot version was updated to fix the boot and USB issues on Raspberry Pi 4 8GiB version
- fix: stop networkd before leaving etcd on 'reset' path
- fix: update the way NTP sync uses `adjtimex` syscall
- fix: bump crypto library for the CSR verification fix
- fix: use both self-signed and Kubernetes CA to verify Kubelet cert
- fix: update osType in OVA other3xLinux64Guest"
- fix: update etcd client errors, print etcd join failures
- fix: zero out manifest contents before setting new value
- fix: check retryable network errors by interface
- fix: trim endpoints/nodes from arguments in talosctl config
- fix: revert mark PMBR EFI partition as bootable
- fix: require leader on etcd member operations
- fix: add a check for overlay mounts in installer pre-flight checks
- fix: publish rockpi4 image to release artifacts
- fix: create rootfs for system services via /system tmpfs
- fix: retry Kubernetes API errors on cordon/uncordon/etc
- fix: ignore EOF errors from Kubernetes API when converting control plane
- fix: workaround race in containerd runner with stdin pipe
- fix: get rid of data race in encoder and fix concurrent map access
- fix: prevent panic in validate config if `machine.install` is missing
- fix: allow `convert-k8s --remove-initialized-keys` with K8s cp is down
- fix: resolve the issue with Kubernetes upgrade
- fix: resolve the issue with DHCP lease not being renewed
- fix: config validation: CNI should apply to cp nodes, encryption config
- fix: command `etcd remove-member` shouldn't remove etcd data directory
- fix: build rockpi4 metal image as part of CI build
- fix: upgrade-k8s bug with empty config values and provision script
- fix: talosctl health should not check kube-proxy when it is disabled
- fix: properly format spec comments in the resources
- fix: don't touch any partitions on upgrade with --preserve
- fix: move containerd CRI config files under `/var/`
- fix: verify CSR signature before issuing a certificate
- fix: revert mark the EFI partition in PMBR as bootable
- fix: mark the EFI partition in PMBR as bootable
- fix: return UUID in middle endian only on SMBIOS >= 2.6

### 0.10.3

- u-boot version was updated to fix the boot and USB issues on Raspberry Pi 4 8GiB version
- fix: stop networkd and pods before leaving etcd on upgrade
- fix: properly populate AllowSchedulingOnMasters option in gen config RPC
- fix: stop networkd before leaving etcd on 'reset' path
- fix: update the way NTP sync uses `adjtimex` syscall
- fix: bump crypto library for the CSR verification fix
- fix: use both self-signed and Kubernetes CA to verify Kubelet cert
- fix: update osType in OVA other3xLinux64Guest"
- fix: update etcd client errors, print etcd join failures
- fix: zero out manifest contents before setting new value
- fix: check retryable network errors by interface
- fix: trim endpoints/nodes from arguments in talosctl config
- fix: revert mark PMBR EFI partition as bootable
- fix: require leader on etcd member operations
- fix: add a check for overlay mounts in installer pre-flight checks
- fix: publish rockpi4 image to release artifacts
- fix: create rootfs for system services via /system tmpfs
- fix: retry Kubernetes API errors on cordon/uncordon/etc
- fix: ignore EOF errors from Kubernetes API when converting control plane
- fix: workaround race in containerd runner with stdin pipe
- fix: get rid of data race in encoder and fix concurrent map access
- fix: prevent panic in validate config if `machine.install` is missing
- fix: allow `convert-k8s --remove-initialized-keys` with K8s cp is down
- fix: resolve the issue with Kubernetes upgrade
- fix: resolve the issue with DHCP lease not being renewed
- fix: config validation: CNI should apply to cp nodes, encryption config
- fix: command `etcd remove-member` shouldn't remove etcd data directory
- fix: build rockpi4 metal image as part of CI build
- fix: upgrade-k8s bug with empty config values and provision script
- fix: talosctl health should not check kube-proxy when it is disabled
- fix: properly format spec comments in the resources
- fix: don't touch any partitions on upgrade with --preserve
- fix: move containerd CRI config files under `/var/`
- fix: verify CSR signature before issuing a certificate
- fix: revert mark the EFI partition in PMBR as bootable
- fix: mark the EFI partition in PMBR as bootable
- fix: return UUID in middle endian only on SMBIOS >= 2.6

### 0.10.4

- u-boot version was updated to fix the boot and USB issues on Raspberry Pi 4 8GiB version
- fix: prefer extraConfig over OVF env, skip empty config
- fix: stop networkd and pods before leaving etcd on upgrade
- fix: properly populate AllowSchedulingOnMasters option in gen config RPC
- fix: stop networkd before leaving etcd on 'reset' path
- fix: update the way NTP sync uses `adjtimex` syscall
- fix: bump crypto library for the CSR verification fix
- fix: use both self-signed and Kubernetes CA to verify Kubelet cert
- fix: update osType in OVA other3xLinux64Guest"
- fix: update etcd client errors, print etcd join failures
- fix: zero out manifest contents before setting new value
- fix: check retryable network errors by interface
- fix: trim endpoints/nodes from arguments in talosctl config
- fix: revert mark PMBR EFI partition as bootable
- fix: require leader on etcd member operations
- fix: add a check for overlay mounts in installer pre-flight checks
- fix: publish rockpi4 image to release artifacts
- fix: create rootfs for system services via /system tmpfs
- fix: retry Kubernetes API errors on cordon/uncordon/etc
- fix: ignore EOF errors from Kubernetes API when converting control plane
- fix: workaround race in containerd runner with stdin pipe
- fix: get rid of data race in encoder and fix concurrent map access
- fix: prevent panic in validate config if `machine.install` is missing
- fix: allow `convert-k8s --remove-initialized-keys` with K8s cp is down
- fix: resolve the issue with Kubernetes upgrade
- fix: resolve the issue with DHCP lease not being renewed
- fix: config validation: CNI should apply to cp nodes, encryption config
- fix: command `etcd remove-member` shouldn't remove etcd data directory
- fix: build rockpi4 metal image as part of CI build
- fix: upgrade-k8s bug with empty config values and provision script
- fix: talosctl health should not check kube-proxy when it is disabled
- fix: properly format spec comments in the resources
- fix: don't touch any partitions on upgrade with --preserve
- fix: move containerd CRI config files under `/var/`
- fix: verify CSR signature before issuing a certificate
- fix: revert mark the EFI partition in PMBR as bootable
- fix: mark the EFI partition in PMBR as bootable
- fix: return UUID in middle endian only on SMBIOS >= 2.6


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **0.10.4**, the newest release recorded here for this line.

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

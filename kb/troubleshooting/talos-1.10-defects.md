---
id: TROUBLE-TALOS_1_10_DEFECTS
type: troubleshooting
title: "talos 1.10: defects fixed in the 1.10 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.10.0 <1.11.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - talos 1.10 known issues
  - talos 1.10 fixed in
  - is this talos bug already fixed
tags:
  - troubleshooting
  - upgrade
  - talos
sources:
  - type: docs
    path: siderolabs/talos release notes for the 1.10 line — bug-fix entries
    url: https://github.com/siderolabs/talos/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# talos 1.10: defects fixed in the 1.10 line

## Summary

**79 defects** the project fixed across **10 releases** of the 1.10 line, from 1.10.0 to
1.10.9. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.10.0

- fix: handle correctly changing platform network config
- fix: set media type to OCI for image cache layer
- fix: sync PCR extension with volume provisioning lifecycle
- fix: skip lvm activation if meta is not found
- fix: handle override path for registry mirrors correctly
- fix: avoid printing terminating null byte in SELinux context
- fix: race in the volume mount status handling
- fix: use proper read-only bind mounts in init
- fix: pass /usr/etc/in-container to apid, trustd and extension containers
- fix: add missing TOOLS_PREFIX for WITH_DEBUG_SHELL builds
- fix: ignore missing config (nocloud) via cidata
- fix: reconnect on SideroLink tunnel on/off change
- fix: qemu: archive cluster logs only after stopping VMs
- fix: ensure no goroutines escape in dns controller
- fix: block NodePort services with ingress firewall
- fix: handle dynamic HTTP proxy settings for discovery client
- fix: correctly map link names/aliases when using VIP operator
- fix: ignore digest part of images when checking version
- fix: make ingress firewall filter traffic to nodeports
- fix: make image cache volume management less strict
- fix: installer with SecureBoot should contain UKIs
- fix: do not close client.Client.conn with finalizer
- fix: ensure proper closure of client.Client.conn with finalizer
- fix: handle of PE sections with duplicate names
- fix(ci): k8s integration suite wait for resource
- fix: disks with 4k sector size and systemd-boot
- fix: ignore forbidden error when waiting for pod eviction
- fix: add informer resync period for node status watcher
- fix: merge of VolumeConfig documents with sizes
- fix: partition alignment on disks with 4k sectors
- fix: request previous IP address in discovery
- fix: mount selinuxfs only when SELinux is enabled
- fix: update field name for bus path disk selector
- fix: exclude disks with empty transport for disk selector
- fix: build of talosctl on non-Linux platforms
- fix: ignore member not found error on leave cluster
- fix: get next rule number for IPv6 in the appropriate chain
- fix: fix `Failed to initialize SELinux labeling handle` udev error
- fix: make talosctl time work with PTP time sync
- fix: match MAC addresses case-insensitive (nocloud)
- fix: order volume config by the requested size
- fix: avoid nil-pointer-panic in `RegistriesConfigController`
- fix: power on the machine on reboot request in qemu power api
- fix: lock provisioning order of user disk partitions
- fix: replace static buffer allocation on growth
- fix: remove patches and other files from copy-only packages
- fix: adjust kernel options around ACPI/PCI/EFI
- fix: update config-arm64 to add Rasperry Pi watchdog support
- fix: dvb was missing I2C_MUX support and si2168 driver
- fix: add CONFIG_INTEL_MEI_GSC_PROXY as module
- fix: do not install man and locale for exported packages
- fix: install policycoreutils under correct prefix

### 1.10.1

- fix: multiple logic issues in platform network config controller
- fix: deny apply config requests without v1alpha1 in "normal" mode
- fix: suppress duplicate platform config updates
- fix: do correct backoff for nocloud reconcile

### 1.10.2

- fix: disable automatic MAC assignment to bridge interfaces
- fix: consistently apply dynamic grpc proxy dialer
- fix: remove DynamicResourceAllocation feature gate

### 1.10.3

- fix(ci): iso reproducibility file permissions
- fix: add generic CSR generator and OpenSSL interop

### 1.10.4

- fix: update siderolink library for wgtunnel panic fix
- fix: rework the way CRI config generation is waited for
- fix: use correct FUSE magic for IMA `fsmagic` matching
- fix: upgrade grpc library to the latest 1.71.x

### 1.10.5

- fix: add limited retries for not found images
- fix: hold user volume mount point across kubelet restarts
- fix: etcd recover with multiple advertised addresses
- fix: treat context canceled as expected error on image pull

### 1.10.6

- fix: issue with volume remount on service restart
- fix: add more bootloader probe logs on upgrade
- fix: talos endpoint might not be created in Kubernetes

### 1.10.7

- fix: live reload of TLS client config for discovery client
- fix: enforce minimum size on user volumes if not set explicitly
- fix: allow TLS config to be passed as a function

### 1.10.8

- fix: reserve the apid and trustd ports from the ephemeral port range
- fix: trim zero bytes in the DHCP host & domain response

### 1.10.9

- fix: adapt SELinuxSuite.TestNoPtrace to new strace version
- fix: clear provisioning data on SideroLink config change


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.10.9**, the newest release recorded here for this line.

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

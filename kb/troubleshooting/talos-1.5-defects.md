---
id: TROUBLE-TALOS_1_5_DEFECTS
type: troubleshooting
title: "talos 1.5: defects fixed in the 1.5 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.5.0 <1.6.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - talos 1.5 known issues
  - talos 1.5 fixed in
  - is this talos bug already fixed
tags:
  - troubleshooting
  - upgrade
  - talos
sources:
  - type: docs
    path: siderolabs/talos release notes for the 1.5 line — bug-fix entries
    url: https://github.com/siderolabs/talos/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# talos 1.5: defects fixed in the 1.5 line

## Summary

**62 defects** the project fixed across **7 releases** of the 1.5 line, from 1.5.0 to
1.5.6. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.5.0

- fix: make encryption config provider default to `luks2` if not set
- fix: fast-wipe the system disk on talosctl reset
- fix: terminate dashboard gracefully on & switch back to tty1
- fix: log explicitly when kubelet has no nodeIP match
- fix: enable compression and bump gRPC max msg size
- fix: retry CRI pod removal, fix upgrade flow in the tests
- fix: rewrite encryption system information flow
- fix: disable dashboard on Azure, GCP and Scaleway
- fix: properly handle YAML comment stripping for multi-doc
- fix: capabilities including `ALL` should be uppercase
- fix: provide stashed META values before installation
- fix: compare only basename of `os.Args[0]` in machined
- fix: allow time skew for generated kubeconfig
- fix: don't load RDMA over Ethernet driver by default
- fix: do not probe kernel args in dashboard if not needed
- fix: skip DHCP RENEW if server IP in the lease is all zeroes
- fix: upgrade-k8s use internal IP first, external IP fallback
- fix: fail quickly if upgrade-k8s is used with multiple nodes
- fix: fall back to external IP when discovering nodes in upgrade-k8s
- fix: refresh kubelet self-issued serving certificates
- fix: revert: set rlimit explicitly in wrapperd
- fix: properly skip/cleanup controlplane configs for workers
- fix: don't reload control plane pods on cert SANs changes
- fix: enforce nolock option for all NFS mounts by default
- fix: add back required TARGETARCH for installer
- feat: update Linux to 6.1.25, fix virtio on arm64
- fix: display correct number of machines on dashboard
- fix: allow `talosctl cp` to handle special files in `/proc`
- fix: do not show control plane status for workers on dashboard
- fix: fix dashboard crash when a non-existent node is specified
- fix: respect BROWSER=echo in client auth interceptor
- fix: use SO_LINGER option when doing TCP healthchecks
- fix: pass context to the key handler in the server wrapper
- fix: enable USB attached SCSI driver on x86 systems

### 1.5.1

- fix: prevent dashboard crashes when process info is not available
- fix: properly GC images supplied with both tag and digest
- fix: automatically change `rpi_4` board on upgrade
- fix: use image digest when starting a container
- fix: restore compatibility with Kubernetes 1.26

### 1.5.2

- fix: update kubernetes library for 1.28 upgrade pre-checks
- fix: shorten VLAN link names to fit into the limit of 15 characters
- fix: set correct (1 year) talosconfig expiration
- fix: set proper timeouts for KubePrism loadbalancer
- fix: properly calculate overal of node address with subnet filters

### 1.5.3

- fix: generate of modules.dep when on the machine
- fix: build CPU ucode correctly for early loader
- fix: set default route priority for hcloud platform
- fix: handle correctly change of listen address for maintenance service

### 1.5.4

- fix: handle secure boot state policy pcr digest error
- fix: use tpm2 hash algorithm constants and allow non-SHA-256 PCRs
- fix: clear the encryption config in META when STATE is reset
- fix: the node IP for kubelet shouldn't change if nothing matches

### 1.5.5

- fix: don't validate machine.install if installed
- fix: when writing to META in the installer/imager, use fixed name
- fix: make Talos work on Rockpi 4c boards again

### 1.5.6

- fix: take into account the moment seen when cleaning up CRI images
- fix: disk UUID & WWID always empty in `talosctl disks`
- fix: skip writing the file if the contents haven't changed
- fix: be more tolerant to error handling in Mounts API
- fix: ignore kernel command line in container mode
- fix: allow extra kernel args for secureboot installer
- fix: decode escape sequences while reading from kmsg


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.5.6**, the newest release recorded here for this line.

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

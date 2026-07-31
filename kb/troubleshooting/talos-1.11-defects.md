---
id: TROUBLE-TALOS_1_11_DEFECTS
type: troubleshooting
title: "talos 1.11: defects fixed in the 1.11 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.11.0 <1.12.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - talos 1.11 known issues
  - talos 1.11 fixed in
  - is this talos bug already fixed
tags:
  - troubleshooting
  - upgrade
  - talos
sources:
  - type: docs
    path: siderolabs/talos release notes for the 1.11 line — bug-fix entries
    url: https://github.com/siderolabs/talos/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# talos 1.11: defects fixed in the 1.11 line

## Summary

**53 defects** the project fixed across **5 releases** of the 1.11 line, from 1.11.0 to
1.11.6. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.11.0

- fix: bring back linux/armv7 build and update xz
- fix: actually use SIDEROV1_KEYS_DIR env var if it's provided
- fix: one more attempt to fix volume mount race on restart
- fix: live reload of TLS client config for discovery client
- fix: enforce minimum size on user volumes if not set explicitly
- fix: issue with volume remount on service restart
- fix: do not download artifacts for cron Grype scan
- fix: add more bootloader probe logs on upgrade
- fix: talos endpoint might not be created in Kubernetes
- fix: add limited retries for not found images
- fix: hold user volume mount point across kubelet restarts
- fix: etcd recover with multiple advertised addresses
- fix: treat context canceled as expected error on image pull
- fix: update siderolink library for wgtunnel panic fix
- fix: correctly predict interface name on darwin
- fix: mashal resource byte slices as strings in YAML
- fix: rework the way CRI config generation is waited for
- fix(talosctl): correct --help output for dashboard command
- fix(ci): iso reproducibility file permissions
- fix: use vmdk-convert istead of qemu-img to create VMDK for OVA files
- fix: disable automatic MAC assignment to bridge interfaces
- fix: consistently apply dynamic grpc proxy dialer
- fix: multiple logic issues in platform network config controller
- fix: deny apply config requests without v1alpha1 in "normal" mode
- fix: suppress duplicate platform config updates
- fix: replace downloaded asset paths correctly in cluster create cmd
- fix: do correct backoff for nocloud reconcile
- fix: sync PCR extension with volume provisioning lifecycle
- fix: handle correctly changing platform network config
- fix: set media type to OCI for image cache layer
- fix: update TLS config, add tests for TLS interactions
- fix: remove code duplication and fix Ed255119 CA generation
- fix: add generic CSR generator and OpenSSL interop
- fix: allow TLS config to be passed as a function
- fix: do not log error if chunk zero was never written
- fix: remove DynamicResourceAllocation feature gate
- fix: bring back updated containerd gvisor patch

### 1.11.2

- fix: use correct order to determine SideroV1 keys directory path
- fix: trim zero bytes in the DHCP host & domain response
- fix: re-create cgroups when restarting runners

### 1.11.3

- fix: cherry-pick of commit `0fbb0b0` from #11959
- fix: cherry-pick of commit `cd9fb27` from #11943
- fix: provide nocloud metadata with missing network config
- fix: support secure HTTP proxy with gRPC dial
- fix: don't set broadcast for /31 and /32 addresses

### 1.11.4

- fix: race between VolumeConfigController and UserVolumeConfigController
- fix: provide minimal platform metadata always
- fix: set a timeout for SideroLink provision API call
- fix: reserve the apid and trustd ports from the ephemeral port range

### 1.11.6

- fix: disable kexec in talosctl cluster create on arm64
- fix: adapt SELinuxSuite.TestNoPtrace to new strace version
- fix: clear provisioning data on SideroLink config change
- fix: stop attaching to tearing down mount parents


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.11.6**, the newest release recorded here for this line.

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

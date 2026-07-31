---
id: TROUBLE-TALOS_0_14_DEFECTS
type: troubleshooting
title: "talos 0.14: defects fixed in the 0.14 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.14.0 <0.15.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - talos 0.14 known issues
  - talos 0.14 fixed in
  - is this talos bug already fixed
tags:
  - troubleshooting
  - upgrade
  - talos
sources:
  - type: docs
    path: siderolabs/talos release notes for the 0.14 line — bug-fix entries
    url: https://github.com/siderolabs/talos/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# talos 0.14: defects fixed in the 0.14 line

## Summary

**27 defects** the project fixed across **3 releases** of the 0.14 line, from 0.14.0 to
0.14.2. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.14.0

- fix: use default time servers in time API if none are configured
- fix: make `apply-config` work reliably in any Talos state
- fix: relax validation for wireguard endpoints
- fix: drop unpacked layers from containerd image store
- fix: leave only a single IPv4/IPv6 address as kubelet's node IP
- fix: update blockdevice library to properly handle absent GPT
- fix: allow add_key and request_key in kubelet seccomp profile
- fix: don't run kexec prepare on shutdown and reset
- fix: wait for follow reader to start before writing to the file
- fix: clear time adjustment error when setting time to specific value
- fix: endpoints and nodes in generated talosconfig
- fix: remove listening socket to fix Talos in a container restart
- fix: skip generating empty `.machine.logging`
- fix: don't drop ability to use ambient capabilities
- fix: treat literal 'unknown' as a valid machine type
- fix: attempt to clean up tasks in containerd runner
- fix: delete expired affiliates from the discovery service
- fix: use ECDSA-SHA512 when generating certs for Talos < 0.13
- fix: allow overriding `audit-policy-file` in `kube-apiserver` static pod
- fix: use ECDSA-SHA256 signature algorithm for Kubernetes certs
- fix: add interface route if DHCP4 router is not directly routeable
- fix: don't enable 'no new privs' on the system level
- fix: return partition table not exist when trying to read an empty dev
- fix: remove useless (?) goroutines leading to data race error

### 0.14.1

- fix: pass path to conformance retrieve results

### 0.14.2

- fix: use leaf certificate in the apid RBAC check
- fix: pass path to conformance retrieve results


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **0.14.2**, the newest release recorded here for this line.

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

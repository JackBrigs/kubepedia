---
id: TROUBLE-TALOS_0_13_DEFECTS
type: troubleshooting
title: "talos 0.13: defects fixed in the 0.13 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.13.0 <0.14.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - talos 0.13 known issues
  - talos 0.13 fixed in
  - is this talos bug already fixed
tags:
  - troubleshooting
  - upgrade
  - talos
sources:
  - type: docs
    path: siderolabs/talos release notes for the 0.13 line — bug-fix entries
    url: https://github.com/siderolabs/talos/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# talos 0.13: defects fixed in the 0.13 line

## Summary

**41 defects** the project fixed across **5 releases** of the 0.13 line, from 0.13.0 to
0.13.4. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.13.0

- fix: allow overriding `audit-policy-file` in `kube-apiserver` static pod
- fix: use ECDSA-SHA512 when generating certs for Talos < 0.13
- fix: use ECDSA-SHA256 signature algorithm for Kubernetes certs
- fix: revert use ECDSA-SHA256 signature algorithm for Kubernetes certs
- fix: add interface route if DHCP4 router is not directly routeable
- fix: don't enable 'no new privs' on the system level
- fix: reset inputs back to initial state in secrets.APIController
- fix: use readonly mode when probing devices with `All` lookup
- fix: make probe open blockdevice in readonly mode
- fix: add node address to the list of allowed IPs (kubespan)
- fix: skip bad cloud-config in OpenStack platform
- fix: tear down control plane static pods when etcd is stopped
- fix: completely prevent editing resources other than mc
- fix: write KubernetesCACert chmodded 0400 instead of 0500
- fix: update the way results are retrieved for certified conformance
- fix: multiple fixes for KubeSpan and Wireguard implementation
- fix: suppress spurious Kubernetes API server cert updates
- fix: correctly parse multiple pod/service CIDRs
- fix: correctly define example for `extraMounts`
- fix: ignore error on duplicate for `MountStatus`
- fix: don't extract nil IPs in the GCP platform
- fix: properly handle omitempty fields in the validator
- fix: validate IP address returned as HTTP response in platform code
- fix: don't allow bootstrap if etcd data directory is not empty
- fix: do not set KSPP kernel params in container mode
- fix: don't support cgroups nesting in process runner
- fix: extramount should have `yaml:",inline"` tag
- fix: don't panic if the machine config doesn't have network (EM)
- fix: make sure file mode is same (reproducibility issue)
- fix: add back support for generating ECDSA keys with P-256 and SHA512
- fix: enable connections to endpoints with public certs
- fix: also open in readonly mode when running `All` lookup method

### 0.13.1

- fix: treat literal 'unknown' as a valid machine type
- fix: delete expired affiliates from the discovery service
- fix: update affiliate state correctly when they get deleted
- fix: cluster with some subscriptions isn't empty

### 0.13.2

- fix: remove listening socket to fix Talos in a container restart
- fix: don't drop ability to use ambient capabilities

### 0.13.3

- fix: don't run kexec prepare on shutdown and reset

### 0.13.4

- fix: leave only a single IPv4/IPv6 address as kubelet's node IP
- fix: allow add_key and request_key in kubelet seccomp profile


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **0.13.4**, the newest release recorded here for this line.

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

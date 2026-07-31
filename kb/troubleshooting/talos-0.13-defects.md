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

**74 defects** the project fixed across **5 releases** of the 0.13 line, from 0.13.0 to
0.13.4. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.13.0

- talos-systems/talos@d50728580 fix: allow overriding `audit-policy-file` in `kube-apiserver` static pod
- talos-systems/talos@98759512e fix: use ECDSA-SHA512 when generating certs for Talos < 0.13
- talos-systems/talos@fd5c47771 fix: use ECDSA-SHA256 signature algorithm for Kubernetes certs
- talos-systems/talos@ccc210ead chore: fix integration-qemu-race
- talos-systems/talos@250529e19 fix: revert use ECDSA-SHA256 signature algorithm for Kubernetes certs
- talos-systems/talos@a3ac9bfd8 fix: sort output of the argument builder
- talos-systems/talos@81c389926 fix: use ECDSA-SHA256 signature algorithm for Kubernetes certs
- talos-systems/talos@27a695be5 fix: add interface route if DHCP4 router is not directly routeable
- talos-systems/talos@c55b4a5ee fix: don't enable 'no new privs' on the system level
- talos-systems/talos@d52befd1a fix: ignore 404 for AWS external IPs
- talos-systems/talos@0f60ef6d3 fix: reset inputs back to initial state in secrets.APIController
- talos-systems/talos@62acd6251 fix: check trustd API CA on worker nodes
- talos-systems/talos@cddcb9622 fix: find devices without partition table
- talos-systems/talos@b1b6d6136 fix: check for existence of dhcp6 FQDN first
- talos-systems/talos@519999b84 fix: use readonly mode when probing devices with `All` lookup
- talos-systems/talos@452893c26 fix: make probe open blockdevice in readonly mode
- talos-systems/talos@d9eb18bfd fix: containerd log symlink
- talos-systems/talos@1cb9f282b fix: don't marshal clock with SecretsBundle
- talos-systems/talos@21cdd8540 fix: add node address to the list of allowed IPs (kubespan)
- talos-systems/talos@ed12379f2 fix: patch multi nodes support
- talos-systems/talos@3de505c89 fix: skip bad cloud-config in OpenStack platform
- talos-systems/talos@a394d1e20 fix: tear down control plane static pods when etcd is stopped
- talos-systems/talos@ec7f44efe fix: completely prevent editing resources other than mc
- talos-systems/talos@0ff4c7cdb fix: write KubernetesCACert chmodded 0400 instead of 0500
- talos-systems/talos@a1c9d6490 fix: update the way results are retrieved for certified conformance
- talos-systems/talos@ef0229592 fix: print etcd member ID in hex
- talos-systems/talos@5ca1fb822 fix: multiple fixes for KubeSpan and Wireguard implementation
- talos-systems/talos@b1bd64250 fix: build platform images
- talos-systems/talos@c3b2429ce fix: suppress spurious Kubernetes API server cert updates
- talos-systems/talos@14c69df50 fix: correctly parse multiple pod/service CIDRs
- talos-systems/talos@bd5b9c96e fix: correctly define example for `extraMounts`
- talos-systems/talos@f8bebba2d fix: ignore error on duplicate for `MountStatus`
- talos-systems/talos@da0f6e7e1 fix: allow updating diskSelector option
- talos-systems/talos@97da354cc fix: do not panic on invalid machine configs
- talos-systems/talos@c4048e263 fix: don't extract nil IPs in the GCP platform
- talos-systems/talos@6312f473e fix: properly handle omitempty fields in the validator
- talos-systems/talos@80b5f0e7f fix: validate IP address returned as HTTP response in platform code
- talos-systems/talos@5f5ac12f1 fix: properly case the VMware name
- talos-systems/talos@0a6048f46 fix: don't allow bootstrap if etcd data directory is not empty
- talos-systems/talos@e24b93b4e fix: cgroup delegate
- talos-systems/talos@576ba1957 fix: do not set KSPP kernel params in container mode
- talos-systems/talos@b8c92ede5 fix: don't support cgroups nesting in process runner
- talos-systems/talos@1abc12be1 fix: extramount should have `yaml:",inline"` tag
- talos-systems/talos@0b86edab8 fix: don't panic if the machine config doesn't have network (EM)
- talos-systems/talos@8bef41e4b fix: make sure file mode is same (reproducibility issue)
- talos-systems/crypto@9a63cba fix: add back support for generating ECDSA keys with P-256 and SHA512
- talos-systems/crypto@893bc66 fix: use SHA256 for ECDSA-P256
- talos-systems/discovery-service@ee4b2a4 fix: retry on Hello failures
- talos-systems/discovery-service@b2e2079 fix: properly encrypt IPv6 endpoints
- talos-systems/discovery-service@e9d5dfa fix: enable connections to endpoints with public certs
- talos-systems/discovery-service@6454cfc refactor: kresify, fix linter and rename to Kubespan manager
- talos-systems/discovery-service@3437ff2 fixes from testing
- talos-systems/go-blockdevice@70d2865 fix: try to find cdrom disks
- talos-systems/go-blockdevice@667bf53 fix: revert gpt partition not found
- talos-systems/go-blockdevice@d7d4cdd fix: gpt partition not found
- talos-systems/go-blockdevice@33afba3 fix: also open in readonly mode when running `All` lookup method
- talos-systems/go-blockdevice@d981156 fix: allow Build for Windows
- talos-systems/tools@5b9d214 fix: restore static library for ncurses

### 0.13.1

- talos-systems/talos@a770bbef7 fix: handle skipped mounts correctly
- talos-systems/talos@cdf9a5ee6 fix: treat literal 'unknown' as a valid machine type
- talos-systems/talos@4aa988507 fix: delete expired affiliates from the discovery service
- talos-systems/discovery-service@b579076 fix: update affiliate state correctly when they get deleted
- talos-systems/discovery-service@49e53b1 fix: cluster with some subscriptions isn't empty

### 0.13.2

- talos-systems/talos@a937e6f7d fix: remove listening socket to fix Talos in a container restart
- talos-systems/talos@c873dc5d0 fix: don't drop ability to use ambient capabilities
- talos-systems/talos@2226a9924 fix: hcloud network config changes

### 0.13.3

- talos-systems/talos@f375ba1d3 fix: unblock events watch on context cancel
- talos-systems/talos@8b5fcb1cc fix: ignore not existing nodes on cordoning
- talos-systems/talos@f303a8c3f fix: ignore virtual IP as kubelet node IPs
- talos-systems/talos@0018fbf66 fix: don't run kexec prepare on shutdown and reset

### 0.13.4

- talos-systems/talos@58560a02d fix: leave only a single IPv4/IPv6 address as kubelet's node IP
- talos-systems/talos@de4aeaf4e fix: catch panics in network operator runs
- talos-systems/talos@774d3a92c fix: ignore EBUSY from `kexec_file_load`
- talos-systems/talos@7d6334982 fix: allow add_key and request_key in kubelet seccomp profile


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

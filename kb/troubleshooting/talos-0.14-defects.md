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

**66 defects** the project fixed across **3 releases** of the 0.14 line, from 0.14.0 to
0.14.2. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.14.0

- talos-systems/talos@5bf3a1519 fix: update DHCP library with the panic fix
- talos-systems/talos@02796f889 fix: allow kubelet to be started via the API
- talos-systems/talos@e69eacae1 fix: use default time servers in time API if none are configured
- talos-systems/talos@c60e153a1 fix: cleanup affiliates
- talos-systems/talos@1d6f140d7 fix: make `apply-config` work reliably in any Talos state
- talos-systems/talos@fc5ec5007 fix: relax validation for wireguard endpoints
- talos-systems/talos@149ffa977 fix: increase boot and etcd join timeouts
- talos-systems/talos@d225cf91e fix: tmpfs default permissions
- talos-systems/talos@8f3e1a4ad fix: drop unpacked layers from containerd image store
- talos-systems/talos@8370dde1f docs: fix typos
- talos-systems/talos@400225c88 docs: fix GCP docs
- talos-systems/talos@b824909d6 fix: disable kexec on RPi4
- talos-systems/talos@3257751bc fix: initialize Drainer properly
- talos-systems/talos@e4bc68bf0 fix: leave only a single IPv4/IPv6 address as kubelet's node IP
- talos-systems/talos@9427e78dc fix: catch panics in network operator runs
- talos-systems/talos@d1f55f901 fix: update blockdevice library to properly handle absent GPT
- talos-systems/talos@6bb75150a fix: allow add_key and request_key in kubelet seccomp profile
- talos-systems/talos@58892cd69 fix: unblock events watch on context cancel
- talos-systems/talos@caa76be2c fix: containerd failed to load plugin
- talos-systems/talos@c6a67b866 fix: ignore not existing nodes on cordoning
- talos-systems/talos@750e31c4a fix: ignore EBUSY from `kexec_file_load`
- talos-systems/talos@2d11b5955 fix: ignore virtual IP as kubelet node IPs
- talos-systems/talos@030fd349b fix: don't run kexec prepare on shutdown and reset
- talos-systems/talos@95105071d chore: fix simple issues found by golangci-lint
- talos-systems/talos@8e8687d75 fix: use temporary sonobuoy version
- talos-systems/talos@a2233bfe4 fix: improve NTP sync process
- talos-systems/talos@7efc1238e fix: parse partition size correctly
- talos-systems/talos@efbae7857 fix: use etc folder for du cli tests
- talos-systems/talos@198eea51a fix: wait for follow reader to start before writing to the file
- talos-systems/talos@e8fccbf53 fix: clear time adjustment error when setting time to specific value
- talos-systems/talos@fe228d7c8 fix: do not use yaml.v2 in the support cmd
- talos-systems/talos@9b48ca217 fix: endpoints and nodes in generated talosconfig
- talos-systems/talos@f6110f803 fix: remove listening socket to fix Talos in a container restart
- talos-systems/talos@728164e25 docs: fix kexec_load_disabled param name in release notes
- talos-systems/talos@f6328f09a fix: fix filename typo
- talos-systems/talos@8b6206537 fix: skip generating empty `.machine.logging`
- talos-systems/talos@60ad00636 fix: don't drop ability to use ambient capabilities
- talos-systems/talos@97d64d160 fix: hcloud network config changes
- talos-systems/talos@1d1e1df64 fix: handle skipped mounts correctly
- talos-systems/talos@0a964d921 test: fix openstack unit-test stability
- talos-systems/talos@9c48ebe8f fix: gcp fetching externalIP
- talos-systems/talos@6c297268c test: fix e2e k8s version
- talos-systems/talos@cff20ec78 fix: change services OOM score
- talos-systems/talos@e77d81fff fix: treat literal 'unknown' as a valid machine type
- talos-systems/talos@6ad459519 docs: fix field names for bonding configuration
- talos-systems/talos@c0fda6436 fix: attempt to clean up tasks in containerd runner
- talos-systems/talos@d92c98e19 docs: fix discovery service documentation link
- talos-systems/talos@31b6e39e5 fix: delete expired affiliates from the discovery service
- talos-systems/talos@997873b6d fix: use ECDSA-SHA512 when generating certs for Talos < 0.13
- talos-systems/talos@7137166d1 fix: allow overriding `audit-policy-file` in `kube-apiserver` static pod
- talos-systems/talos@8fcd42196 chore: fix integration-qemu-race
- talos-systems/talos@91a858b53 fix: sort output of the argument builder
- talos-systems/talos@657f7a56b fix: use ECDSA-SHA256 signature algorithm for Kubernetes certs
- talos-systems/talos@022c7335f fix: add interface route if DHCP4 router is not directly routeable
- talos-systems/talos@66a1579ea fix: don't enable 'no new privs' on the system level
- talos-systems/talos@facc8c38a docs: fix documentation for cluster discovery
- talos-systems/go-blockdevice@15b182d fix: return partition table not exist when trying to read an empty dev
- talos-systems/go-blockdevice@b9517d5 fix: resize partition
- talos-systems/go-smbios@fd5ec8c fix: remove useless (?) goroutines leading to data race error
- talos-systems/pkgs@832dae4 fix: enable CONFIG_DM_SNAPSHOT
- talos-systems/pkgs@b4cdb99 fix: update containerd shas
- talos-systems/siderolink@f7cadbc fix: handle duplicate peer updates

### 0.14.1

- talos-systems/talos@c1c5d9e8e fix: pass path to conformance retrieve results

### 0.14.2

- talos-systems/talos@2eeb91d18 fix: use leaf certificate in the apid RBAC check
- talos-systems/talos@5dd813a85 chore: fix golangci-lint install
- talos-systems/talos@c1c5d9e8e fix: pass path to conformance retrieve results


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

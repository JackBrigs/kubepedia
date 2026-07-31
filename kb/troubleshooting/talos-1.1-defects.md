---
id: TROUBLE-TALOS_1_1_DEFECTS
type: troubleshooting
title: "talos 1.1: defects fixed in the 1.1 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.1.0 <1.2.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - talos 1.1 known issues
  - talos 1.1 fixed in
  - is this talos bug already fixed
tags:
  - troubleshooting
  - upgrade
  - talos
sources:
  - type: docs
    path: siderolabs/talos release notes for the 1.1 line — bug-fix entries
    url: https://github.com/siderolabs/talos/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# talos 1.1: defects fixed in the 1.1 line

## Summary

**53 defects** the project fixed across **3 releases** of the 1.1 line, from 1.1.0 to
1.1.2. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.1.0

- fix: make `talosctl bootstrap` accept only single node
- fix: support SideroLink "secure" gRPC connection
- fix: wait for `/var` to be mounted in kubelet service controller
- fix: introduce more route protocols as constants
- fix: unmarshal HardwareAddr without stdlib help
- fix: implement unmarshaling from YAML for LinkStatus
- fix: correctly parse empty route flags from YAML
- fix: cluster creation error message formatting
- fix: improve error message when creating cluster
- fix: match for WSL platform in case-insentive way
- fix: ignore completed pods in cluster health check
- fix: detect WSL for `talosctl cluster create` on Docker
- fix: append hostname to cluster SANs when port is not specified
- fix: ignore failures to dial wireguard client
- fix: properly set `allowSchedulingOnMasters` in the interactive install
- fix: load kubelet system service in StartAllServices task
- fix: remove D-Bus sockets before listen attempts
- fix: use json.Unmarshal instead of yaml.Unmarshal
- fix: talosctl throws error if gen option and --input-dir flags are combined
- fix: return an error if there is no byte slice in ReadonlyProvider
- fix: allow graceful node shutdown to be overridden
- fix: include Go primitive types into unstructured deepcopy
- fix: don't mount D-Bus socket via mount under recursive bind mount
- fix: trigger CRI config merge on correct resource update
- fix: strip 'v' prefix from versions on Kubernetes upgrade
- fix: run the 'post' stage of the service always
- fix: correctly handle stopping services with reverse dependencies
- fix: detect lingering mounts in the installer correctly
- fix: provide logger to the etcd snapshot restore
- fix: avoid panic in DHCPv6 operator on nil dereference
- fix: enable IPv6 in Docker-based Talos clusters
- fix: validate empty TLS config for registries
- fix: enable etcd consistency on check startup
- fix: correctly find partitions with config data (`metal-iso`)
- fix: give up virtual IPs before the kubelet workloads are shut down
- fix: use 'localhost' endpoint in docker provisioner on Windows
- fix: increase intiial window and connection window sizes
- fix: trigger properly `udevd` on types and actions
- fix: clean up custom udev rules if the config is cleared
- fix: ignore connection reset errors on k8s upgrade
- fix: split regular network operation configuration and virtual IP
- fix: ignore terminated pods in pod health checks
- fix: invert the condition to skip kubelet kernel checks
- fix: check for IPv6 before applying accept_ra
- fix: align partition to 1M boundary by default
- fix: use correct method to generate Wireguard private key

### 1.1.1

- fix: stabilize etcd join and promote sequences
- fix: siderlink api assume port 443 with https schema
- fix: provide CA certificates in `/etc/ssl/certs/ca-certificates.crt`
- fix: generate correct bootstrap manifests when only IPv6 CIDR is used

### 1.1.2

- fix: folder permissions of overlay mounted folders
- fix: use masks and different firewall mark for KubeSpan
- fix: skip bond itself when matching interface (Equinix Metal)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.1.2**, the newest release recorded here for this line.

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

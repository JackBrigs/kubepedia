---
id: TROUBLE-TALOS_1_0_DEFECTS
type: troubleshooting
title: "talos 1.0: defects fixed in the 1.0 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.0.0 <1.1.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - talos 1.0 known issues
  - talos 1.0 fixed in
  - is this talos bug already fixed
tags:
  - troubleshooting
  - upgrade
  - talos
sources:
  - type: docs
    path: siderolabs/talos release notes for the 1.0 line — bug-fix entries
    url: https://github.com/siderolabs/talos/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# talos 1.0: defects fixed in the 1.0 line

## Summary

**54 defects** the project fixed across **7 releases** of the 1.0 line, from 1.0.0 to
1.0.6. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.0.0

- fix: correctly find partitions with config data (`metal-iso`)
- fix: give up virtual IPs before the kubelet workloads are shut down
- fix: use 'localhost' endpoint in docker provisioner on Windows
- fix: trigger properly `udevd` on types and actions
- fix: clean up custom udev rules if the config is cleared
- fix: ignore connection reset errors on k8s upgrade
- fix: split regular network operation configuration and virtual IP
- fix: ignore terminated pods in pod health checks
- fix: invert the condition to skip kubelet kernel checks
- fix: check for IPv6 before applying accept_ra
- fix: align list and diskusage command flags with their Linux analogs
- fix: set route to metaserver for scaleway platform
- fix: avoid replacing default gRPC codec in machinery
- fix: determine openstack interface IP correctly
- fix: parse properly IPv6 address in the cmdline `ip=` arg
- fix: validate kubelet node IP subnets correctly
- fix: pass proper sequence to shutdown sequence on ACPI shutdown
- fix: use leaf certificate in the apid RBAC check
- fix: clean up containerd state on installer run/validate
- fix: handle 404 errors from AWS IMDS correctly
- fix: use #!/usr/bin/env bash as shebang instead of #!/bin/bash
- fix: qemu: always use runtime.GOARCH for CNI bundle
- fix: enforce reasonable TLS min tls-min-version
- fix: use correct error in `kernel_param_spec` Modify call handling
- fix: avoid panic in config loading/validation
- fix: filter down nameservers for docker-based cluster create
- fix: ignore missing init.yaml for cluster create
- fix: pass path to conformance retrieve results
- fix: use default time servers in time API if none are configured
- fix: lookup filesystem labels on the actual device path
- fix: use io.EOF error when no backend connections are available

### 1.0.1

- fix: enable IPv6 in Docker-based Talos clusters
- fix: validate empty TLS config for registries
- fix: enable etcd consistency on check startup

### 1.0.2

- fix: avoid panic in DHCPv6 operator on nil dereference

### 1.0.3

- fix: provide logger to the etcd snapshot restore

### 1.0.4

- fix: allow graceful node shutdown to be overridden
- fix: include Go primitive types into unstructured deepcopy
- fix: don't mount D-Bus socket via mount under recursive bind mount
- fix: trigger CRI config merge on correct resource update
- fix: strip 'v' prefix from versions on Kubernetes upgrade
- fix: run the 'post' stage of the service always
- fix: correctly handle stopping services with reverse dependencies
- fix: detect lingering mounts in the installer correctly

### 1.0.5

- fix: detect WSL for `talosctl cluster create` on Docker
- fix: append hostname to cluster SANs when port is not specified
- fix: ignore failures to dial wireguard client
- fix: properly set `allowSchedulingOnMasters` in the interactive install
- fix: load kubelet system service in StartAllServices task
- fix: remove D-Bus sockets before listen attempts
- fix: use json.Unmarshal instead of yaml.Unmarshal

### 1.0.6

- fix: wait for `/var` to be mounted in kubelet service controller
- fix: match for WSL platform in case-insentive way
- fix: ignore completed pods in cluster health check


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.0.6**, the newest release recorded here for this line.

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

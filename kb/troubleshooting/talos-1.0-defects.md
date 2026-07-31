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

**96 defects** the project fixed across **7 releases** of the 1.0 line, from 1.0.0 to
1.0.6. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.0.0

- siderolabs/talos@7bcd15c08 fix: correctly find partitions with config data (`metal-iso`)
- siderolabs/talos@9cf5d3e48 fix: correctly escape '.' in volume names
- siderolabs/talos@f822f6896 fix: give up virtual IPs before the kubelet workloads are shut down
- siderolabs/talos@5ded170a1 fix: use 'localhost' endpoint in docker provisioner on Windows
- siderolabs/talos@7ad030a0b fix: the etcd recovery client and tests
- siderolabs/talos@4adae5e4a fix: trigger properly `udevd` on types and actions
- siderolabs/talos@6c0f8c704 fix: clean up custom udev rules if the config is cleared
- siderolabs/talos@b6d71d49e fix: ignore connection reset errors on k8s upgrade
- siderolabs/talos@5bfc16cfe fix: ignore pod CIDRs for kubelet node IPs
- siderolabs/talos@cb97369e5 fix: split regular network operation configuration and virtual IP
- siderolabs/talos@cb61e5953 fix: ignore terminated pods in pod health checks
- siderolabs/talos@426921a6b fix: invert the condition to skip kubelet kernel checks
- siderolabs/talos@eb16019eb fix: refresh etcd certs on startup/join
- siderolabs/talos@06647da34 chore: fix equinixMetal platform name
- siderolabs/talos@83d7aebe1 fix: check for IPv6 before applying accept_ra
- siderolabs/talos@a50747a64 fix: align list and diskusage command flags with their Linux analogs
- siderolabs/talos@8975a56eb docs: fix typo in release notes
- siderolabs/talos@de69ab790 fix: scaleway network config
- siderolabs/talos@79d9720a3 fix: set route to metaserver for scaleway platform
- siderolabs/talos@1800b4c70 chore: fix kernel reference errata
- siderolabs/talos@6ccfdbaf1 fix: avoid replacing default gRPC codec in machinery
- siderolabs/talos@95a564ba2 fix: prefer logical on merging link specs
- siderolabs/talos@8b7091a06 fix: correct vultr interface IP calculation
- siderolabs/talos@5a0fd63c8 fix: determine openstack interface IP correctly
- siderolabs/talos@47619f832 docs: update system extensions guide with grammar fixes
- siderolabs/talos@6fadfa8db fix: parse properly IPv6 address in the cmdline `ip=` arg
- siderolabs/talos@8b6d6220d fix: parse interface ip correctly (nocloud)
- siderolabs/talos@54632b1be docs: fix developing Talos docs
- siderolabs/talos@1e3f2f952 fix: validate kubelet node IP subnets correctly
- siderolabs/talos@c34768367 fix: disable auto-tls for etcd
- siderolabs/talos@9bffc7e8d fix: pass proper sequence to shutdown sequence on ACPI shutdown
- siderolabs/talos@949464e4b fix: use leaf certificate in the apid RBAC check
- siderolabs/talos@7f9790912 fix: clean up containerd state on installer run/validate
- siderolabs/talos@831f65a07 fix: close client provider instead of Talos client in the upgrade module
- siderolabs/talos@7b3962745 fix: handle 404 errors from AWS IMDS correctly
- siderolabs/talos@a0889600f chore: fix golangci-lint install
- siderolabs/talos@a50c42980 fix: use #!/usr/bin/env bash as shebang instead of #!/bin/bash
- siderolabs/talos@4464b725c fix: qemu: always use runtime.GOARCH for CNI bundle
- siderolabs/talos@58eb3600f fix: enforce reasonable TLS min tls-min-version
- siderolabs/talos@b8d4c5dfa fix: use correct error in `kernel_param_spec` Modify call handling
- siderolabs/talos@907f8cbfb docs: fix patch flag
- siderolabs/talos@6af83afd5 fix: handle multiple-IP cluster nodes
- siderolabs/talos@af440919b fix: avoid panic in config loading/validation
- siderolabs/talos@f3ec24beb fix: vmware documentation typo
- siderolabs/talos@59437d6d8 fix: filter down nameservers for docker-based cluster create
- siderolabs/talos@2e735714d fix: derive machine-id from node identity
- siderolabs/talos@7dff8a53e fix: ignore missing init.yaml for cluster create
- siderolabs/talos@944f13221 chore: fix release pipeline
- siderolabs/talos@35bc2940e fix: kexec on RPI4
- siderolabs/talos@f235cfbae fix: multiple usability fixes
- siderolabs/talos@dac550a50 docs: fix troubleshooting guide
- siderolabs/talos@f49f40a33 fix: pass path to conformance retrieve results
- siderolabs/talos@773496935 fix: config apply immediate
- siderolabs/talos@4175396a8 refactor: use update go-blockdevice library with allocation fixes
- siderolabs/talos@936b4c4ce fix: update DHCP library with the panic fix
- siderolabs/talos@ab42886bf fix: allow kubelet to be started via the API
- siderolabs/talos@ec641f729 fix: use default time servers in time API if none are configured
- siderolabs/talos@79f213eec fix: cleanup affiliates
- siderolabs/pkgs@0505e01 chore: fix `=m` kernel build options
- talos-systems/crypto@6fa2d93 fix: deepcopy nil fields as `nil`
- talos-systems/go-blockdevice@ec428fe fix: lookup filesystem labels on the actual device path
- talos-systems/grpc-proxy@b076302 fix: use io.EOF error when no backend connections are available
- talos-systems/grpc-proxy@fa6843a chore: fix spelling
- talos-systems/net@409926a fix: parse correctly some IPv6 CIDRs

### 1.0.1

- siderolabs/talos@4d9baa450 fix: enable IPv6 in Docker-based Talos clusters
- siderolabs/talos@3bad0e5a4 fix: retry manifest updates in upgrade-k8s
- siderolabs/talos@119eecfe7 fix: validate empty TLS config for registries
- siderolabs/talos@41c48a68e fix: enable etcd consistency on check startup

### 1.0.2

- siderolabs/talos@aae68c92f fix: avoid panic in DHCPv6 operator on nil dereference
- siderolabs/talos@36f60ea70 fix: correctly parse tags out of images

### 1.0.3

- siderolabs/talos@989367f93 fix: provide logger to the etcd snapshot restore
- siderolabs/talos@ac50a42c8 fix: correct cri package import path

### 1.0.4

- siderolabs/talos@39979ac90 fix: allow graceful node shutdown to be overridden
- siderolabs/talos@78dab0182 fix: include Go primitive types into unstructured deepcopy
- siderolabs/talos@2a359d243 fix: don't mount D-Bus socket via mount under recursive bind mount
- siderolabs/talos@ebcf50442 fix: trigger CRI config merge on correct resource update
- siderolabs/talos@84c10017b fix: strip 'v' prefix from versions on Kubernetes upgrade
- siderolabs/talos@d5a823ab6 fix: run the 'post' stage of the service always
- siderolabs/talos@71991a9f6 fix: correctly handle stopping services with reverse dependencies
- siderolabs/talos@f881f2f11 fix: detect lingering mounts in the installer correctly

### 1.0.5

- siderolabs/talos@07729c402 fix: detect WSL for `talosctl cluster create` on Docker
- siderolabs/talos@23274efe6 fix: dhcpv6 leasetime segfault loop
- siderolabs/talos@0523c63ba fix: reset certificate SANs on update
- siderolabs/talos@89d928516 fix: append hostname to cluster SANs when port is not specified
- siderolabs/talos@a73fccb79 fix: ignore failures to dial wireguard client
- siderolabs/talos@cfb5572d7 fix: properly set `allowSchedulingOnMasters` in the interactive install
- siderolabs/talos@ad84c2137 fix: load kubelet system service in StartAllServices task
- siderolabs/talos@c32946212 fix: openstack unable to parseIP
- siderolabs/talos@c91205e1f fix: remove D-Bus sockets before listen attempts
- siderolabs/talos@a5cda5df8 fix: use json.Unmarshal instead of yaml.Unmarshal
- siderolabs/talos@20c10a470 fix: add source path for ovmf flash image

### 1.0.6

- siderolabs/talos@e65638ef4 fix: wait for `/var` to be mounted in kubelet service controller
- siderolabs/talos@8e4f58f3e fix: improve vip operator shutdown sequence
- siderolabs/talos@ed4147b60 docs: fix "double-base64-encode" in cert/key examples
- siderolabs/talos@71ddb2ee2 fix: match for WSL platform in case-insentive way
- siderolabs/talos@9f476c47f fix: ignore completed pods in cluster health check


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

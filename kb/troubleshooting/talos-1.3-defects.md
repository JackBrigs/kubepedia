---
id: TROUBLE-TALOS_1_3_DEFECTS
type: troubleshooting
title: "talos 1.3: defects fixed in the 1.3 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.3.0 <1.4.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - talos 1.3 known issues
  - talos 1.3 fixed in
  - is this talos bug already fixed
tags:
  - troubleshooting
  - upgrade
  - talos
sources:
  - type: docs
    path: siderolabs/talos release notes for the 1.3 line — bug-fix entries
    url: https://github.com/siderolabs/talos/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# talos 1.3: defects fixed in the 1.3 line

## Summary

**100 defects** the project fixed across **7 releases** of the 1.3 line, from 1.3.0 to
1.3.7. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.3.0

- fix: don't report link name in route statuses
- fix: fix nil pointer panic and incorrect error output
- fix: workaround panic in the kubelet service controller
- fix: report errors to Equinix Metal event API
- fix: use only kube-apiserver endpoints for Talos API access endpoints
- fix: introduce 'overridePath' setting and fix Talos resolver
- fix: disable kexec on upgrades from pre-BTF kernel
- fix: parse and apply DHCP settings properly from cmdline
- fix: don't publish external IPs as affiliate addresses
- fix: limit SideroLink Wireguard link MTU to 1280
- fix: filter up duplicate IPs out of NodeAddresses
- fix: check if processes is nil to avoid panic
- fix: generate correct Flannel config for IPv6-only clusters
- fix: properly cleanup legacy static pod manifests directory
- fix: support serving config for qemu launcher on IPv6
- fix: serve static pod files on 127.0.0.1 instead of localhost
- fix: skip protobuf full unmarshaling for some talosctl commands
- fix: skip hostname via DHCP on OpenStack platform
- fix: lookup Equinix Metal bond slaves using 'permanent addr'
- fix: continue applying bootstrap manifests on some errors
- fix: update discovery client with the redirect fix
- fix: fix protoenc encoding for enums and types with custom encoders
- fix: stop worker nodes from acting as apid routers
- fix: never sign client certificate requests in trustd
- fix: kill the task processes when cleaning up stale task
- fix: use different username for Talos Kubernetes API access
- fix: include all node addresses into etcd cert SANs
- fix: list COSI APIs for the apid authenticator
- fix: pass a pointer to specs.Mount into protoenc.Marshal
- fix: automatically discard VIPs for etcd advertised addresses
- fix: prevent panic on health check if a member has no IPs
- fix: properly handle `configContext` being `nil` in Talos client
- fix: change the type of returned gRPC connection object from the client
- fix: expose Talos client gRPC connection via the function `Conn`
- fix: update COSI to the version with gRPC Wait fix
- fix: get command in the case 'nodes' are not set in the context
- fix: correctly render hosts.toml with multiple endpoints
- fix: update etcd certificates when node addresses changes
- fix: don't wait for the hostname in maintenance mode
- fix: make 'ca', 'crt' and 'key' flags optional for 'talosctl config add'
- fix: handle grub config being empty in the `Revert` function
- fix: clean up `cancelCtxMu` leftovers in PriorityLock
- fix: add back support for generating ECDSA keys with P-256 and SHA512
- fix: verify CSR signature before issuing a certificate
- fix: function NewKeyPair should create certificate with proper subject
- fix: fix Copy documentation and implementation
- fix: rename tuples.go to pair.go and set proper package name
- fix: align partition to 1M boundary by default
- fix: lookup filesystem labels on the actual device path
- fix: return partition table not exist when trying to read an empty dev
- fix: also open in readonly mode when running `All` lookup method
- fix: perform correct PMBR partition calculations
- fix: preserve the PMBR bootable flag when opening GPT partition
- fix: make disk type matcher parser case insensitive
- fix: properly detect nvme and sd card disk types
- fix: revert mark the EFI partition in PMBR as bootable
- fix: mark the EFI partition in PMBR as bootable
- fix: align partition start to physical sector size
- fix: properly handle no child processes error from cmd.Wait
- fix: blockdevice reset should read partition table from disk
- fix: correctly build paths for `mmcblk` devices
- fix: return proper disk size from GetDisks function
- fix: sync kernel partition table incrementally
- fix: return correct error value from blkpg functions
- fix: properly inform kernel about partition deletion
- fix: calculate last lba of partition correctly
- fix: update cmdline.Set() to drop the value being overwritten
- fix: implement `errors.Is` for all errors in the set
- fix: correctly implement error interfaces on wrapped errors
- fix: remove useless (?) goroutines leading to data race error
- fix: return UUID in middle endian only on SMBIOS >= 2.6
- fix: ignore errors on duplicate `SetHeader` calls
- fix: use io.EOF error when no backend connections are available
- fix: ignore some errors so that we don't spam the logs
- fix: allow mode to be set for each request being proxied
- Break StreamDirector interface, fix metadata propagation for gRPC-Go>1.5. (#20)
- bugfix: fix gRPC Java deadlock, due to different dispatch logic
- fix: include MachineStatusEvent into the list of supported events
- fix: ignore 'exist' error on interface managmeent
- fix: use correct method to generate Wireguard private key

### 1.3.1

- fix: send diagnostic output to stderr consistently
- fix: default the manifest namespace if not set
- fix: use proper key usage for apid client certificate
- fix: redact service account key in config in RedactSecrets method

### 1.3.3

- fix: mark DigitalOcean anchor IP as scope link
- fix: unwrap gRPC errors on stop/remove pods check
- fix: build correctly etcd initial cluster URL
- fix: bump COSI runtime with the panic controller restart fix
- fix: service restart (including extension services)

### 1.3.4

- fix: default dns domain to 'cluster.local' in local case
- fix: return proper error if download attempts time out
- fix: correctly quote and unquote strings in GRUB config

### 1.3.5

- fix: docker talosctl cluster create provisioner
- fix: quote the ampersand character in GRUB config
- fix: talosctl reboot command passing mode in wait mode
- fix: blockdevice size is reported by Linux in 512 blocks always

### 1.3.6

- fix: successful ACPI shutdown in maintenance mode
- fix: update go-smbios library with Hyper-V data fix

### 1.3.7

- fix: output of `talosctl logs` might be corruped
- fix: use 'no block' etcd dial with multiple endpoints


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.3.7**, the newest release recorded here for this line.

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

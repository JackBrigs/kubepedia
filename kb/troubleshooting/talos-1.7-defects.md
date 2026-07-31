---
id: TROUBLE-TALOS_1_7_DEFECTS
type: troubleshooting
title: "talos 1.7: defects fixed in the 1.7 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.7.0 <1.8.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - talos 1.7 known issues
  - talos 1.7 fixed in
  - is this talos bug already fixed
tags:
  - troubleshooting
  - upgrade
  - talos
sources:
  - type: docs
    path: siderolabs/talos release notes for the 1.7 line — bug-fix entries
    url: https://github.com/siderolabs/talos/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# talos 1.7: defects fixed in the 1.7 line

## Summary

**85 defects** the project fixed across **8 releases** of the 1.7 line, from 1.7.0 to
1.7.7. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.7.0

- fix: close apid inter-backend connections gracefully for real
- fix: assign different priority to IPv6 default gateway on OpenStack
- fix: generate secureboot ISO .der certificate correctly
- fix: reconnect to the logs stream in dashboard after reboot
- fix: present all accepted CAs to the kube-apiserver
- fix: validate that workers don't get cluster CA key
- fix: make static pods check output consistent
- fix: close the apid connection to other machines gracefully
- fix: pre-create nftables chain to make kubelet use nftables
- fix: make safeReset truly safe to call multiple times
- fix: don't announce the VIP on acquire failure
- fix: report unsupported x86_64 microarchitecture level
- fix: retry in the fixed amount of time if grpc relay failed
- fix: force Flannel CNI to use KubePrism Kubernetes API endpoint
- fix: allow platform cmdline args to be platform-specific
- fix: don't set default endpoints on gen config
- fix: populate routes to BGP neighbors (Equinix Metal)
- fix: patch correctly config in `talosctl upgrade-k8s`
- fix: remove maintenance config when maintenance service is shut down
- fix: update discovery client with the fix for keepalive interval
- fix: fix nil panic on maintenance upgrade with partial config
- fix: do not fail cluster create when input dir does not contain talosconfig
- fix: workaround a race in CNI setup (talosctl cluster create)
- fix: provide auth when pulling images in the imager
- fix: ignore 'no such device' in addition to 'no such file'
- fix: handle errors to watch apid/trustd certs
- fix: only set gateway if set in context (opennebula)
- fix: ensure that Talos runs in a pod (container)
- fix: disable KubeSpan endpoint harvesting by default
- fix: correctly handle partial configs in `DNSUpstreamController`
- fix: use MachineStatus resource to check for boot done
- fix: run xfs_repair on invalid argument error
- fix: error with decoding config document with wrong apiVersion
- fix: pass TTL when generating client certificate
- fix: add log line about controller runtime failing
- fix: use a separate cgroup for each extension service
- fix: take into account the moment seen when cleaning up CRI images
- fix: run the interactive installer loop to report errors
- fix: be more tolerant to error handling in Mounts API
- fix: allow META encoded values to be compressed
- fix: use correct TTL for talosconfig in `talosctl config new`
- fix: strategic patch merging for audit policy
- fix: fix .der output in `talosctl gen secureboot`
- fix: update discovery service client to v0.1.6
- fix: support KubePrism settings in Kubernetes Discovery
- fix: fix nodes on dashboard footer when node names are used in `--nodes`
- fix: merge ports and ingress configs correctly in NetworkRuleConfig
- fix: disk UUID & WWID always empty in `talosctl disks`
- fix: replace the filemap implementation to not buffer in memory
- fix: pick correctly base installer image layers
- fix: imager should support different Talos versions
- fix: update the way secureboot signer fetches certificate (azure)
- fix: use correct prefix when installing SBC files
- fix: leave discovery service later in the reset sequence
- fix: add a KubeSpan option to disable extra endpoint harvesting
- fix: talosctl cluster create not to enforce kubeprism always
- fix: store and execute desired action on emergency action
- fix: trim leading spaces\newlines in inline manifest contents
- fix: skip writing the file if the contents haven't changed
- fix: do not panic in `merge.Merge` if map value is nil
- fix: always print the login URL on key renew flow
- fix: support validating signatures generated with the time in the future
- fix: decode escape sequences while reading from kmsg
- fix: use musl 1.2.4 in tools, revert kmod back to 32

### 1.7.1

- fix: wait for devices to be discovered before probing filesystems
- fix: bump priority of OpenStack routes if IPv6 and default gateway
- fix: add endpoints for "virtual" `host-dns` service
- fix: return proper value from Bridge.STP instead of plain nil

### 1.7.2

- fix: don't enable hostDNS for versions of Talos which do not have it
- fix: check for `nil` machine config during installation
- fix: do not fail cli action tracker when boot id cannot be read
- fix: disable CONFIG_EFI_DISABLE_PCI_DMA option

### 1.7.3

- fix: correctly handle dns messages in our dns implementation
- fix: update go-tail library to fix 'short read' error

### 1.7.4

- fix: correct time adjustment in `time.SyncController`

### 1.7.5

- fix: initial assignment of Hetzner Cloud Alias IP
- fix: decrease maximum negative ttl for dns responses

### 1.7.6

- fix: sort ports and merge adjacent ones in the nft rule
- fix: enable CONFIG_PROC_CHILDREN for amd64 kernel

### 1.7.7

- fix: report internally service as unhealthy if not running
- fix: report errors correctly when pulling, fix EEXIST
- fix: merge extension service config files by `mountPath`
- fix: retry with another upstream if the previous failed
- fix: fix graph diffs in dashboard when node aliases are used
- fix: stop decoding without error if EOF encountered during header read


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.7.7**, the newest release recorded here for this line.

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

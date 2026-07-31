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

**139 defects** the project fixed across **8 releases** of the 1.7 line, from 1.7.0 to
1.7.7. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.7.0

- siderolabs/talos@b72f0d7f9 fix: overlay installer operations
- siderolabs/talos@81cd2b16e fix: mark overlay installer executable
- siderolabs/talos@fa5c7ee70 fix: close apid inter-backend connections gracefully for real
- siderolabs/talos@eea41cdae fix: assign different priority to IPv6 default gateway on OpenStack
- siderolabs/talos@eca03b03c fix: don't modify a global map of profiles
- siderolabs/talos@7d24ddd73 fix: generate secureboot ISO .der certificate correctly
- siderolabs/talos@028a5b4b1 fix: reconnect to the logs stream in dashboard after reboot
- siderolabs/talos@5019c9fa7 fix: present all accepted CAs to the kube-apiserver
- siderolabs/talos@09ef5b3c9 fix: validate that workers don't get cluster CA key
- siderolabs/talos@4f7cb9c3a fix: make static pods check output consistent
- siderolabs/talos@dd7d8d3aa fix: close the apid connection to other machines gracefully
- siderolabs/talos@41a54e8a0 fix: pre-create nftables chain to make kubelet use nftables
- siderolabs/talos@01d8b897c fix: make safeReset truly safe to call multiple times
- siderolabs/talos@5c0f74b37 fix: don't announce the VIP on acquire failure
- siderolabs/talos@1b17008e9 fix: handle more OpenStack link types
- siderolabs/talos@e7d804140 fix: always update firewall rules (kubespan)
- siderolabs/talos@78b9bd927 fix: report unsupported x86_64 microarchitecture level
- siderolabs/talos@71d90ba5f fix: retry in the fixed amount of time if grpc relay failed
- siderolabs/talos@3195e5d15 fix: force Flannel CNI to use KubePrism Kubernetes API endpoint
- siderolabs/talos@090143b03 fix: allow platform cmdline args to be platform-specific
- siderolabs/talos@fac3dd043 fix: don't set default endpoints on gen config
- siderolabs/talos@f737e6495 fix: populate routes to BGP neighbors (Equinix Metal)
- siderolabs/talos@89fc68b45 fix: service lifecycle issues
- siderolabs/talos@9afa70baf fix: patch correctly config in `talosctl upgrade-k8s`
- siderolabs/talos@7376f34e8 fix: remove maintenance config when maintenance service is shut down
- siderolabs/talos@952801d8b fix: handle overlay partition options
- siderolabs/talos@465b9a4e6 fix: update discovery client with the fix for keepalive interval
- siderolabs/talos@e89d755c5 fix: etcd config validation for worker
- siderolabs/talos@1bb6027cc fix: fix nil panic on maintenance upgrade with partial config
- siderolabs/talos@f02aeec92 fix: do not fail cluster create when input dir does not contain talosconfig
- siderolabs/talos@f23bd8144 fix: syslog parser
- siderolabs/talos@3a764029e docs: fix typo in word governor
- siderolabs/talos@b2ad5dc5f fix: workaround a race in CNI setup (talosctl cluster create)
- siderolabs/talos@457507803 fix: provide auth when pulling images in the imager
- siderolabs/talos@8872a7a21 fix: ignore 'no such device' in addition to 'no such file'
- siderolabs/talos@67ac6933d fix: handle errors to watch apid/trustd certs
- siderolabs/talos@c79d69c2e fix: only set gateway if set in context (opennebula)
- siderolabs/talos@66f3ffdd4 fix: ensure that Talos runs in a pod (container)
- siderolabs/talos@7ee999f8a fix: disable KubeSpan endpoint harvesting by default
- siderolabs/talos@493bb60f8 fix: correctly handle partial configs in `DNSUpstreamController`
- siderolabs/talos@559308ef7 fix: use MachineStatus resource to check for boot done
- siderolabs/talos@2f0421b40 fix: run xfs_repair on invalid argument error
- siderolabs/talos@013e13070 fix: error with decoding config document with wrong apiVersion
- siderolabs/talos@3f8a85f1b fix: unlock the upgrade mutex properly
- siderolabs/talos@a04cc8015 fix: pass TTL when generating client certificate
- siderolabs/talos@3fe8c12ca fix: add log line about controller runtime failing
- siderolabs/talos@ddbabc7e5 fix: use a separate cgroup for each extension service
- siderolabs/talos@6ccdd2c09 chore: fix markdown-lint call
- siderolabs/talos@17567f19b fix: take into account the moment seen when cleaning up CRI images
- siderolabs/talos@a5e13c696 fix: retry blockdevice open in the installer
- siderolabs/talos@593afeea3 fix: run the interactive installer loop to report errors
- siderolabs/talos@87be76b87 fix: be more tolerant to error handling in Mounts API
- siderolabs/talos@4a3691a27 docs: fix broken links in metal-network-configuration.md
- siderolabs/talos@d1a79b845 docs: fix small typo in etcd maintenance guide
- siderolabs/talos@e0dfbb8fb fix: allow META encoded values to be compressed
- siderolabs/talos@8a1732bcb fix: pull in `mptspi` driver
- siderolabs/talos@4e9b688d3 fix: use correct TTL for talosconfig in `talosctl config new`
- siderolabs/talos@b0ee0bfba fix: strategic patch merging for audit policy
- siderolabs/talos@474eccdc4 fix: watch bufer overrun for RouteStatus
- siderolabs/talos@cc06b5d7a fix: fix .der output in `talosctl gen secureboot`
- siderolabs/talos@1dbb4abf4 fix: update discovery service client to v0.1.6
- siderolabs/talos@9782319c3 fix: support KubePrism settings in Kubernetes Discovery
- siderolabs/talos@f70b47ddd fix: force KubePrism to connect using IPv4
- siderolabs/talos@d5321e085 fix: update kmsg with utf-8 fix
- siderolabs/talos@7fa7362dd fix: fix nodes on dashboard footer when node names are used in `--nodes`
- siderolabs/talos@ba88678f1 fix: merge ports and ingress configs correctly in NetworkRuleConfig
- siderolabs/talos@dea9bda2d fix: disk UUID & WWID always empty in `talosctl disks`
- siderolabs/talos@f6926faab fix: default priority for ipv6
- siderolabs/talos@265f21be0 fix: replace the filemap implementation to not buffer in memory
- siderolabs/talos@8db3c5b3c fix: pick correctly base installer image layers
- siderolabs/talos@0a30ef784 fix: imager should support different Talos versions
- siderolabs/talos@5a19d078a fix: properly overwrite files on install
- siderolabs/talos@241bc9312 fix: update the way secureboot signer fetches certificate (azure)
- siderolabs/talos@760f793d5 fix: use correct prefix when installing SBC files
- siderolabs/talos@0b94550c4 chore: fix the gvisor test
- siderolabs/talos@10c59a6b9 fix: leave discovery service later in the reset sequence
- siderolabs/talos@131a1b167 fix: add a KubeSpan option to disable extra endpoint harvesting
- siderolabs/talos@e128d3c82 fix: talosctl cluster create not to enforce kubeprism always
- siderolabs/talos@270604bea fix: support user disks via symlinks
- siderolabs/talos@4f195dd27 chore: fix the release.toml
- siderolabs/talos@474fa0480 fix: store and execute desired action on emergency action
- siderolabs/talos@eecc4dbd5 fix: trim leading spaces\newlines in inline manifest contents
- siderolabs/talos@dbf274ddf fix: skip writing the file if the contents haven't changed
- siderolabs/talos@6329222bd fix: do not panic in `merge.Merge` if map value is nil
- siderolabs/discovery-client@fbb1cea fix: keepalive interval calculation
- siderolabs/discovery-client@ff8f4be fix: enable gRPC keepalives
- siderolabs/go-api-signature@370cebf fix: always print the login URL on key renew flow
- siderolabs/go-api-signature@cfd21b6 fix: support validating signatures generated with the time in the future
- siderolabs/go-api-signature@63d4da3 fix: limit clock skew for short-lived keys
- siderolabs/go-kmsg@e358d13 fix: decode escape sequences while reading from kmsg
- siderolabs/pkgs@d57b0ad fix: revert musl to 1.2.4
- siderolabs/pkgs@dd71e02 fix: xz vulnerability
- siderolabs/pkgs@5861223 fix: kernel boot on arm64 metal
- siderolabs/pkgs@f4335dc fix: kernel hardening check script
- siderolabs/pkgs@65006ed fix: enable KFD support in kernel
- siderolabs/pkgs@2358efe fix: enable FUSION_SPI driver
- siderolabs/pkgs@4c59641 fix: zfs module build
- siderolabs/pkgs@dd71790 chore: rekres to fix 'failed' build on main
- siderolabs/siderolink@5422b1c chore: quick fixes
- siderolabs/tools@71eba29 fix: xz vulnerability
- siderolabs/tools@14bf457 fix: use musl 1.2.4 in tools, revert kmod back to 32
- siderolabs/tools@6c1f73d fix: revert kmod to version 31

### 1.7.1

- siderolabs/talos@50023bc4e fix: wait for devices to be discovered before probing filesystems
- siderolabs/talos@41024e17a fix: bump priority of OpenStack routes if IPv6 and default gateway
- siderolabs/talos@bd41fee8c fix: add endpoints for "virtual" `host-dns` service
- siderolabs/talos@2db54c779 fix: return proper value from Bridge.STP instead of plain nil

### 1.7.2

- siderolabs/talos@abaff6084 fix: increase host dns packet ttl for pods
- siderolabs/talos@172569f56 fix: don't enable hostDNS for versions of Talos which do not have it
- siderolabs/talos@5e1544432 fix: check for `nil` machine config during installation
- siderolabs/talos@24c353235 fix: do not fail cli action tracker when boot id cannot be read
- siderolabs/talos@4aeb22f76 fix: use a fresh context for etcd unlock
- siderolabs/pkgs@9caa8be fix: disable CONFIG_EFI_DISABLE_PCI_DMA option

### 1.7.3

- siderolabs/talos@92ec41c22 fix: mount `tracefs` filesystem
- siderolabs/talos@1b3ac2ca6 fix: workaround problems with udevd races
- siderolabs/talos@1f2a870a7 fix: time sync over NTP from future era
- siderolabs/talos@4e9aa3007 fix: correctly handle dns messages in our dns implementation
- siderolabs/talos@8159a0057 fix: panic in osroot controller
- siderolabs/talos@b78fb4fea fix: update go-tail library to fix 'short read' error
- siderolabs/go-tail@7cb7294 fix: remove unexpected short read error

### 1.7.4

- siderolabs/talos@b0ad5904c fix: correct time adjustment in `time.SyncController`

### 1.7.5

- siderolabs/talos@2c4aa7342 chore: fix our dns server implementation
- siderolabs/talos@8ad20a6c1 fix: initial assignment of Hetzner Cloud Alias IP
- siderolabs/talos@b14fe3973 fix: downgrade Azure IMDS required version
- siderolabs/talos@fa6c85259 fix: decrease maximum negative ttl for dns responses

### 1.7.6

- siderolabs/talos@08fbf0896 fix: panic on shutdown
- siderolabs/talos@44827e43b fix: sort ports and merge adjacent ones in the nft rule
- siderolabs/pkgs@fb24a28 fix: enable TPROXY for nftables
- siderolabs/pkgs@a302e94 fix: enable CONFIG_PROC_CHILDREN for amd64 kernel

### 1.7.7

- siderolabs/talos@e53eff902 fix: ignore invalid NTP responses
- siderolabs/talos@28b81b2b0 fix: report internally service as unhealthy if not running
- siderolabs/talos@da5b526e5 fix: report errors correctly when pulling, fix EEXIST
- siderolabs/talos@e6fd4e078 fix: merge extension service config files by `mountPath`
- siderolabs/talos@c95d1fee6 fix: add missing host/nvme-rdma
- siderolabs/talos@0bd287838 fix: bump go-smbios for broken SMIOS tables
- siderolabs/talos@63b59ebe4 fix: add NVMe target kernel modules
- siderolabs/talos@d7b713679 fix: retry with another upstream if the previous failed
- siderolabs/talos@c7f2da147 fix: fix graph diffs in dashboard when node aliases are used
- siderolabs/go-smbios@e781237 fix: stop decoding without error if EOF encountered during header read
- siderolabs/pkgs@ed36e2e fix: add mpt3sas UBSAN patches


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

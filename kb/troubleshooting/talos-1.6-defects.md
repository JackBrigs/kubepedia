---
id: TROUBLE-TALOS_1_6_DEFECTS
type: troubleshooting
title: "talos 1.6: defects fixed in the 1.6 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.6.0 <1.7.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - talos 1.6 known issues
  - talos 1.6 fixed in
  - is this talos bug already fixed
tags:
  - troubleshooting
  - upgrade
  - talos
sources:
  - type: docs
    path: siderolabs/talos release notes for the 1.6 line — bug-fix entries
    url: https://github.com/siderolabs/talos/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# talos 1.6: defects fixed in the 1.6 line

## Summary

**135 defects** the project fixed across **9 releases** of the 1.6 line, from 1.6.0 to
1.6.8. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.6.0

- siderolabs/talos@d42fd10c0 chore: fix the gvisor test
- siderolabs/talos@61e6df169 fix: leave discovery service later in the reset sequence
- siderolabs/talos@c155602ca fix: add a KubeSpan option to disable extra endpoint harvesting
- siderolabs/talos@fe6661128 fix: talosctl cluster create not to enforce kubeprism always
- siderolabs/talos@41fc05438 fix: support user disks via symlinks
- siderolabs/talos@e45794064 chore: fix the release.toml
- siderolabs/talos@591cfb456 fix: store and execute desired action on emergency action
- siderolabs/talos@fee63ac26 fix: trim leading spaces\newlines in inline manifest contents
- siderolabs/talos@cc16b9689 fix: skip writing the file if the contents haven't changed
- siderolabs/talos@ecee92c90 fix: do not panic in `merge.Merge` if map value is nil
- siderolabs/talos@d8a435f0e fix: initialize boot assets with defaults early
- siderolabs/talos@c6835de17 fix: pick etcd adverised addresses from 'current' addresses
- siderolabs/talos@0b111ecb8 fix: support slices of enums and fix NfTablesConntrackStateMatch
- siderolabs/talos@8e2307466 docs: fix talosctl pcap argument
- siderolabs/talos@e4a050cb1 docs: fix talosctl inspect dependencies example indentation
- siderolabs/talos@fbcf4264f docs: fix talosctl dashboard cli docs
- siderolabs/talos@aca8b5e17 fix: ignore kernel command line in container mode
- siderolabs/talos@020a0eb63 docs: fix table formatting for bootstraprequest
- siderolabs/talos@0eb245e04 docs: fix talosctl pcap example indentation
- siderolabs/talos@de6caf534 docs: fix table formatting for machineservice api
- siderolabs/talos@95a252cfc docs: fix link in what is new page
- siderolabs/talos@06941b7e5 fix: allow rootfs propagation configuration for extension services
- siderolabs/talos@71a3bf0e3 fix: allow extra kernel args for secureboot installer
- siderolabs/talos@e9c7ac17a fix: set max msg recv size when proxying
- siderolabs/talos@87c40da6c fix: proper logging in machined on startup
- siderolabs/talos@a54da5f64 fix: image build for nanopi_4s
- siderolabs/talos@813442dd7 fix: don't validate machine.install if installed
- siderolabs/talos@807a9950a fix: use custom Talos/kernel version when generating UKI
- siderolabs/talos@6dc776b8a fix: when writing to META in the installer/imager, use fixed name
- siderolabs/talos@cbe6e7622 fix: generate images for SBCs using imager
- siderolabs/talos@5dff164f1 fix: fix error output of cli action tracker
- siderolabs/talos@ffa5e05cb fix: make Talos work on Rockpi 4c boards again
- siderolabs/talos@a009f5c60 fix: accept sysctl paths with dots
- siderolabs/talos@154bbd70f docs: fix talos version in guide for docker
- siderolabs/talos@0ff7350ab fix: oracle integration fixes
- siderolabs/talos@f9639fb53 test: fix 'talosctl gen' tests
- siderolabs/talos@7bb205ebe fix: don't use runtime-specs Mount struct in machine config
- siderolabs/talos@b87092ab6 fix: handle secure boot state policy pcr digest error
- siderolabs/talos@498aeb8c3 docs: fix incorrect image suffix
- siderolabs/talos@336aee0fd fix: use tpm2 hash algorithm constants and allow non-SHA-256 PCRs
- siderolabs/talos@ef7be16c8 fix: clear the encryption config in META when STATE is reset
- siderolabs/talos@159f45bde docs: fix typos in CLI calls to endpoints
- siderolabs/talos@10ed13067 fix: the node IP for kubelet shouldn't change if nothing matches
- siderolabs/talos@62dcfe81e fix: update kubernetes library to support 1.29 upgrades
- siderolabs/talos@5ca4d58dc fix: generate of modules.dep when on the machine
- siderolabs/talos@e3b494058 fix: build CPU ucode correctly for early loader
- siderolabs/talos@a7edd0523 fix: set default route priority for hcloud platform
- siderolabs/talos@87c1b3ddd fix: calculate UKI ISO size dynamically
- siderolabs/talos@9698e4547 fix: handle correctly change of listen address for maintenance service
- siderolabs/talos@5e11f08a6 fix: trim file path in the container image
- siderolabs/talos@6058c3602 fix: shorten VLAN link names to fit into the limit of 15 characters
- siderolabs/talos@9c2f765c8 fix: allow network device selector to match multiple links
- siderolabs/talos@a04b98637 fix: update kubernetes library for 1.28 upgrade pre-checks
- siderolabs/talos@d693604a1 chore: fix default image list in the release notes
- siderolabs/talos@c918c0855 fix: set correct (1 year) talosconfig expiration
- siderolabs/talos@79bbdf454 fix: set proper timeouts for KubePrism loadbalancer
- siderolabs/talos@b8fb55d5c fix: use a mount prefix when installing a bootloader
- siderolabs/talos@a28d72e9c fix: ova contents to be named `disk.*`
- siderolabs/talos@c0ea4d7ba fix: properly calculate overal of node address with subnet filters
- siderolabs/talos@c99316457 docs: fix the installing system extensions doc
- siderolabs/talos@cb468c41c fix: copy proper modules to arm64 squashfs
- siderolabs/talos@ea0d6e8c6 fix: prevent dashboard crashes when process info is not available
- siderolabs/talos@dc8361c1d fix: properly GC images supplied with both tag and digest
- siderolabs/talos@ccfa8de11 fix: automatically change `rpi_4` board on upgrade
- siderolabs/talos@b56e8b7d9 fix: support 'List' type manifests
- siderolabs/talos@574d48e54 fix: use image digest when starting a container
- siderolabs/talos@175747cea fix: ntp query error with bare IPv6 address
- siderolabs/talos@c8b507fb2 docs: fix kubeprism typo
- siderolabs/talos@92ad18c18 fix: write correct capacity to the ovf
- siderolabs/talos@dc873df9b chore: fix the filenames of openstack images
- siderolabs/talos@bc198e98e docs: retain cilium autoMount pending upstream hostPath fix
- siderolabs/talos@ee6d639f6 fix: match routes on the priority properly
- siderolabs/talos@bff0d8f32 chore: fix dependencies in the release pipeline
- siderolabs/talos@7d688ccfe fix: make encryption config provider default to `luks2` if not set
- siderolabs/talos@4eab3017b fix: calculate log2i properly
- siderolabs/talos@bcf284530 fix: update providerid prefix for aws
- siderolabs/talos@ac2aff5cc fix: fix azure portion of cloud uploader
- siderolabs/talos@793dcedc9 fix: fast-wipe the system disk on talosctl reset
- siderolabs/go-blockdevice@d9313ea fix: define softraid partition
- siderolabs/go-kubernetes@09fa006 fix: retry Windows connection errors
- siderolabs/go-retry@23b6fc2 fix: provider modern error unwrapping
- siderolabs/pkgs@3ae2450 chore: rekres to fix 'failed' build on merge
- siderolabs/pkgs@617d342 fix: revert: update grub to fix loading large initramfs
- siderolabs/pkgs@70919d8 fix: update grub to fix loading large initramfs
- siderolabs/pkgs@f57b0a9 chore: fix kernel target to honor `PLATFORM`
- siderolabs/pkgs@3b70656 chore: fix cacert perms
- siderolabs/pkgs@2e1c0b9 fix: nonfree kmod pkg name

### 1.6.1

- siderolabs/talos@8355c9eef fix: properly overwrite files on install
- siderolabs/talos@2e9901751 fix: update the way secureboot signer fetches certificate (azure)
- siderolabs/talos@4caffd383 fix: use correct prefix when installing SBC files

### 1.6.2

- siderolabs/talos@f87a0468b fix: strategic patch merging for audit policy
- siderolabs/talos@36b913dba fix: watch bufer overrun for RouteStatus
- siderolabs/talos@3576d113c fix: fix .der output in `talosctl gen secureboot`
- siderolabs/talos@0191c3b2c fix: support KubePrism settings in Kubernetes Discovery
- siderolabs/talos@8fa6e93f0 fix: force KubePrism to connect using IPv4
- siderolabs/talos@e05eebca1 fix: update kmsg with utf-8 fix
- siderolabs/talos@37bfa60dd fix: merge ports and ingress configs correctly in NetworkRuleConfig
- siderolabs/talos@306c5cad2 fix: fix nodes on dashboard footer when node names are used in `--nodes`
- siderolabs/talos@530332d24 fix: disk UUID & WWID always empty in `talosctl disks`
- siderolabs/talos@3ebdbabaf fix: default priority for ipv6
- siderolabs/talos@b47619543 fix: replace the filemap implementation to not buffer in memory
- siderolabs/talos@0ec551597 fix: imager should support different Talos versions
- siderolabs/go-kmsg@e358d13 fix: decode escape sequences while reading from kmsg

### 1.6.3

- siderolabs/talos@815fef8c3 fix: allow META encoded values to be compressed
- siderolabs/pkgs@f51aedb fix: disable nct6883 on arm64
- siderolabs/pkgs@7ddbdb4 fix: enable FUSION_SPI driver

### 1.6.4

- siderolabs/talos@040c535c6 fix: retry blockdevice open in the installer
- siderolabs/talos@00b34b254 fix: take into account the moment seen when cleaning up CRI images
- siderolabs/talos@c5ad166be fix: be more tolerant to error handling in Mounts API
- siderolabs/talos@b438f8a9b fix: run the interactive installer loop to report errors
- siderolabs/go-api-signature@370cebf fix: always print the login URL on key renew flow
- siderolabs/go-api-signature@cfd21b6 fix: support validating signatures generated with the time in the future
- siderolabs/go-api-signature@63d4da3 fix: limit clock skew for short-lived keys

### 1.6.5

- siderolabs/talos@c7f5ff73e fix: use MachineStatus resource to check for boot done
- siderolabs/talos@0f5e946f4 fix: ensure that Talos runs in a pod (container)
- siderolabs/talos@36836878f fix: run xfs_repair on invalid argument error
- siderolabs/talos@e993215fe fix: unlock the upgrade mutex properly
- siderolabs/talos@5515a6bab fix: use a separate cgroup for each extension service
- siderolabs/pkgs@b849795 fix: enable KFD support in kernel

### 1.6.6

- siderolabs/talos@e4f712689 fix: workaround a race in CNI setup (talosctl cluster create)
- siderolabs/talos@38b5aed50 fix: provide auth when pulling images in the imager
- siderolabs/talos@4af77b5fd fix: handle errors to watch apid/trustd certs

### 1.6.7

- siderolabs/talos@9ef06f60f fix: service lifecycle issues
- siderolabs/talos@2c9159977 fix: patch correctly config in `talosctl upgrade-k8s`
- siderolabs/talos@16691dfd5 fix: remove maintenance config when maintenance service is shut down
- siderolabs/talos@5cbbbfa68 fix: fix nil panic on maintenance upgrade with partial config
- siderolabs/talos@3c942fe9d fix: etcd config validation for worker

### 1.6.8

- siderolabs/talos@390b29d1a fix: check for `nil` machine config during installation
- siderolabs/talos@3ec9b8d6f fix: do not fail cli action tracker when boot id cannot be read
- siderolabs/talos@f686e7102 fix: bump priority of OpenStack routes if IPv6 and default gateway
- siderolabs/talos@745257f1e fix: return proper value from Bridge.STP instead of plain nil
- siderolabs/talos@968eb5ac8 fix: assign different priority to IPv6 default gateway on OpenStack
- siderolabs/talos@b222d5062 fix: make static pods check output consistent
- siderolabs/talos@dd241d705 fix: don't announce the VIP on acquire failure
- siderolabs/talos@67c76e816 fix: always update firewall rules (kubespan)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.6.8**, the newest release recorded here for this line.

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

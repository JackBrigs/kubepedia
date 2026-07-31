---
id: TROUBLE-TALOS_1_9_DEFECTS
type: troubleshooting
title: "talos 1.9: defects fixed in the 1.9 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.9.0 <1.10.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - talos 1.9 known issues
  - talos 1.9 fixed in
  - is this talos bug already fixed
tags:
  - troubleshooting
  - upgrade
  - talos
sources:
  - type: docs
    path: siderolabs/talos release notes for the 1.9 line — bug-fix entries
    url: https://github.com/siderolabs/talos/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# talos 1.9: defects fixed in the 1.9 line

## Summary

**180 defects** the project fixed across **7 releases** of the 1.9 line, from 1.9.0 to
1.9.6. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.9.0

- siderolabs/talos@55d45bf7e docs: fix 'containter' typo
- siderolabs/talos@c41ec53ba fix: renovate typo
- siderolabs/talos@2e73fdb41 fix: renovate config
- siderolabs/talos@cfe54c4ff fix: match MAC addresses case-insensitive (nocloud)
- siderolabs/talos@39458050b fix: generate and serve registries with port
- siderolabs/talos@234d8cb58 fix: node identity flip
- siderolabs/talos@5a192c375 test: fix flaky test NodeAddressSort
- siderolabs/talos@a38588d2c fix: image cache integration test
- siderolabs/talos@a497e23c4 fix: support image cache on VFAT USB stick
- siderolabs/talos@aa88ad992 fix: authorization config gen
- siderolabs/talos@10fa5b74b fix: order volume config by the requested size
- siderolabs/talos@f3a9b578b fix: use mtu network option for podman
- siderolabs/talos@4b1c59dab fix: avoid nil-pointer-panic in `RegistriesConfigController`
- siderolabs/talos@454164a15 fix: power on the machine on reboot request in qemu power api
- siderolabs/talos@c715695c6 test: fix user namespace test, TPM2 fixes
- siderolabs/talos@3a0c34538 fix: install iptables-nft to the host
- siderolabs/talos@50ea58813 docs: fix a few mistakes in release notes
- siderolabs/talos@2c71086ba fix: lock provisioning order of user disk partitions
- siderolabs/talos@8fb567dd1 docs: fix typo in virtualbox docs
- siderolabs/talos@95c695880 fix: don't reset health status if service doesn't support health checks
- siderolabs/talos@c7b25430b fix: multiple small fixes for service runners
- siderolabs/talos@c254f261f fix: do not extract xattrs in unsquashfs
- siderolabs/talos@fc3b31575 fix: multiple issues with opening encrypted volumes
- siderolabs/talos@c735d1492 fix: wait for udevd before starting sync
- siderolabs/talos@bef4d5150 fix: make `system_disk` condition work properly before install
- siderolabs/talos@e10e90b05 fix: nocloud network link matching on MAC addresses
- siderolabs/talos@2a9130a2e fix: make Talos META partition match more precise
- siderolabs/talos@f1d1628c8 fix: properly halt installation if Talos already installed
- siderolabs/talos@177df62a0 fix: small logrus fixes
- siderolabs/talos@a9875b770 fix: return proper number from the `timeStampWriter`
- siderolabs/talos@e8a262490 fix: systemd-udevd restore old naming behavior
- siderolabs/talos@939c555f9 fix: imager disk image-cache generator
- siderolabs/talos@84459d902 fix: make immage cache config apply immediately
- siderolabs/talos@af5d6b8c4 fix: show SELinux labels on pseudo-fs
- siderolabs/talos@f46922fa9 chore: fix dockerfile warnings
- siderolabs/talos@61b9129e0 fix: add directory entries and filemode to tarball
- siderolabs/talos@c4c1a0d7c fix: make vmware platform common code build on all arches
- siderolabs/talos@6fb518ae5 fix: don't activate LVM volumes in agent mode
- siderolabs/talos@0e3ed3072 fix: no longer leak `Close` reader
- siderolabs/talos@4dc58cfdf chore: small fixes
- siderolabs/talos@f400ae911 fix: small fixes for image cache generation
- siderolabs/talos@93754b7de fix: config and platform manifest generation
- siderolabs/talos@3a5b55fd2 fix: allow CEL expressions config merge
- siderolabs/talos@f9697a9a0 fix: register controlplane node with NoSchedule taint
- siderolabs/talos@30f8b5a9f fix: registry mirror fallback handling
- siderolabs/talos@8a7476c3a fix: install on non-empty disk
- siderolabs/talos@aea98940b fix: arch linux search paths and names for QEMU provisioner
- siderolabs/talos@682718d4c fix: use imager incoming version for extension validation
- siderolabs/talos@a07f66c91 docs: gcp: fix controlplane nodes tags
- siderolabs/talos@a309f6aa5 chore: fix nil pointer dereference in AWS uploader
- siderolabs/talos@333737f17 test: fix unpriviliged process runner test
- siderolabs/talos@fb72e4b7b fix(ci): skip test if `UserNamespacesSupport` feature gate is not set
- siderolabs/talos@aa9311f3d fix: install disk matcher error
- siderolabs/talos@1800f8104 fix: selinux handling and apparmor tests
- siderolabs/talos@7f3aaa21c fix: update permissions for logging directories in /var
- siderolabs/talos@0e6c983b8 fix: mount /sys/kernel/security conditionally
- siderolabs/talos@74b0e8c37 fix: make route normalization keep family
- siderolabs/talos@0a3761c22 fix: talosctl windows arm64
- siderolabs/talos@b54d26c2c fix: mount pseudo sub-mountpoints in init
- siderolabs/talos@b37950625 fix: use more correct condition to skip generating hosts files
- siderolabs/talos@423b1e5fb fix: do not trim 0 from process SELinux label
- siderolabs/talos@3a0a17ae6 fix: prevent panic in nocloud platform code
- siderolabs/talos@9db7a36bf fix: generation of SecureBoot iso
- siderolabs/talos@c755b6d7e fix: update the CRI sandbox image reference
- siderolabs/talos@b7801df82 fix: wait for udevd to be running before activating LVM
- siderolabs/talos@62d185473 fix: talosctl process null character
- siderolabs/talos@d39393879 fix: rework the 'metal-iso' config acquisition
- siderolabs/talos@217253523 docs: fix image factory links
- siderolabs/talos@9e6f64df0 fix: improve error messages for invalid bridge/bond configuration
- siderolabs/talos@7c8c72c2b fix: correct error message for invalid ip=
- siderolabs/talos@867c4b812 docs: fix typo in prodnotes.md
- siderolabs/talos@3d342af44 fix: update incorrect alias for PCIDevice resource
- siderolabs/talos@fc89dc216 fix: support `extra-disks` when using iso
- siderolabs/talos@5853bb0ea fix: json logging panic
- siderolabs/talos@39fe285e6 fix: skip ram disks
- siderolabs/talos@4d902021b fix: do not use pflag csv comma reader for config-patch
- siderolabs/talos@5371788ce fix: typo in documentation
- siderolabs/talos@519a48302 fix: wipe system partitions correctly via kernel args
- siderolabs/talos@0a2b4556c fix: volume encryption with failing keyslots
- siderolabs/talos@6affbd318 fix: update grpc-go the latest patch release
- siderolabs/talos@77a4a4adc fix: scaleway metadata
- siderolabs/talos@7acadc0c8 fix: do not stop udevd before unmounting volumes
- siderolabs/talos@2362f6d3e fix: improve container detection
- siderolabs/talos@b67bc73fd fix: fix mdadm system extension
- siderolabs/talos@f711907e0 fix: make /var/run empty on reboots
- siderolabs/talos@7d02eb60f docs: fix typo in CloudStack docs
- siderolabs/talos@74861573a fix: multiple fixes for LVM activation
- siderolabs/talos@0a4df4ef8 docs: fix nvidia CRI config example
- siderolabs/talos@afc1e1a46 docs: fix typo in extraMounts directory
- siderolabs/talos@a341bdb06 fix: prevent file descriptors leaks to child processes
- siderolabs/talos@4ab8dee69 fix: build talosctl without `tcell_minimal`
- siderolabs/talos@d498f647c docs: fix Kernel Self Protection Project (KSPP) references
- siderolabs/talos@9b77698cf fix: update blockdevice library to v2.0.2
- siderolabs/talos@e46227ab9 docs: fix kubespan name inconsistency
- siderolabs/talos@6b15ca19c fix: audit and fix cgroup reservations
- siderolabs/talos@8166a58b3 fix: filter out non-printable characters in process line
- siderolabs/talos@18daedb51 fix: strategic merge patch delete for map keys
- siderolabs/talos@d4a6d017d fix: ignore invalid NTP responses
- siderolabs/talos@780a1f198 fix: update CoreDNS health check
- siderolabs/talos@a294b366f fix: parse SideroLink API endpoint correctly
- siderolabs/talos@a9269ac7b fix: remove extra logging on ethtool ioctl failures
- siderolabs/discovery-client@b74fb90 fix: allow custom TLS config for the client
- siderolabs/go-blockdevice@134c41b fix: fast wipe also last 1MB of the device
- siderolabs/go-circular@9a0f7b0 fix: multiple data race issues
- siderolabs/go-cmd@d735250 fix: return an error on process nonzero exit code
- siderolabs/go-kubernetes@e56a7f6 fix: update deprecations based on Kubernetes 1.32.0-alpha.3
- siderolabs/grpc-proxy@de1c628 fix: copy data from big frame msg
- siderolabs/pkgs@c01baba fix: add CONFIG_INTEL_MEI_GSC_PROXY as module
- siderolabs/pkgs@0272ad4 fix: enable memory cgroups v1
- siderolabs/pkgs@452298e feat: update systemd to 256.8, fix cpuset/cgroupsv1
- siderolabs/pkgs@bfd88f5 chore: fix make kernel-menuconfig completely
- siderolabs/pkgs@cee356e chore: fix menuconfig build
- siderolabs/pkgs@567a14a fix: do not build unneeded utilities and man for SELinux libraries
- siderolabs/pkgs@c92e123 fix: enable nvme and 2.5gbit ethernet on nanopi-r5s
- siderolabs/pkgs@38ad08e fix: default IOMMU mode to 'lazy'
- siderolabs/pkgs@f474a55 fix: libselinux: support running without /etc/selinux
- siderolabs/pkgs@ba0341e fix: systemd-udevd: search for config in /usr/etc
- siderolabs/pkgs@e2a561f fix: drop the LVM2 udev lvm rule
- siderolabs/pkgs@ae205aa fix: force LVM to use `/run` as state directory
- siderolabs/pkgs@ca2e8c8 fix: lvm2 modprobe path
- siderolabs/pkgs@126b6a4 fix: add mpt3sas UBSAN patches
- siderolabs/siderolink@1893385 fix: initialize tls listener properly
- siderolabs/tools@3750064 fix: update for musl with close_range
- siderolabs/tools@9f2189b fix: bump gettext-tiny to the latest dev version

### 1.9.1

- siderolabs/talos@e702542d1 fix: ignore member not found error on leave cluster
- siderolabs/talos@73c25ee8d fix: talosctl support and race tests
- siderolabs/talos@edd78441b fix: update go-blockdevice to v2.0.9
- siderolabs/talos@c1f975c0b fix: use correct default search domain
- siderolabs/talos@ff91a754f fix: reduce installer image
- siderolabs/talos@9cebe5e28 fix: fix `Failed to initialize SELinux labeling handle` udev error
- siderolabs/talos@3f872860f fix: dashboard crash on CPU data
- siderolabs/talos@f84ba2a9b docs: fix several typos
- siderolabs/talos@7908c9382 fix: make talosctl time work with PTP time sync
- siderolabs/talos@48cb3a6e6 fix: restore previous disk serial fetching
- siderolabs/go-talos-support@0f784bd fix: avoid deadlock on context cancel
- siderolabs/pkgs@45c4ba4 fix: patch containerd with CNI deadlock fix

### 1.9.2

- siderolabs/talos@582064d9c fix: add informer resync period for node status watcher
- siderolabs/talos@28327e001 fix: kube-apiserver authorizers order
- siderolabs/talos@ff9aa806a fix: a couple of imager panics/crashes
- siderolabs/talos@9fd295b5f fix: detect GPT before ZFS
- siderolabs/talos@7b59573de fix: extfs repair and resize
- siderolabs/talos@5f6bfe02a fix: merge of VolumeConfig documents with sizes
- siderolabs/talos@b61ab0a3d fix: partition alignment on disks with 4k sectors
- siderolabs/talos@c4a69d386 fix: yet another dashboard panic
- siderolabs/talos@dec3c6e5b fix: disable NRI plugin in a different way
- siderolabs/talos@dfb54c872 fix: request previous IP address in discovery
- siderolabs/talos@6b1fe3df3 fix: mount selinuxfs only when SELinux is enabled
- siderolabs/talos@5e893e1f5 fix: update field name for bus path disk selector
- siderolabs/talos@9219fc017 fix: exclude disks with empty transport for disk selector
- siderolabs/pkgs@a7487d6 fix: adjust kernel options around ACPI/PCI/EFI
- siderolabs/pkgs@8e435cd fix: update config-arm64 to add Rasperry Pi watchdog support
- siderolabs/pkgs@daabb47 fix: dvb was missing I2C_MUX support and si2168 driver

### 1.9.3

- siderolabs/talos@e3bd08b0a fix: bring back disk UUID
- siderolabs/talos@8fadd042d fix: disks with 4k sector size and systemd-boot
- siderolabs/talos@b854ea97f fix: abort node watch on hostname change
- siderolabs/talos@f72a155c8 fix: ignore forbidden error when waiting for pod eviction
- siderolabs/talos@885cb4cb0 fix: make etc binds read-only

### 1.9.4

- siderolabs/talos@81164efd7 chore: fix spurious generate failures
- siderolabs/talos@7639cf7ef fix: path for ca-certificates
- siderolabs/talos@e3bfb238f fix: make ingress firewall filter traffic to nodeports
- siderolabs/talos@6d0db5185 fix: blockdevice transport detection
- siderolabs/talos@2ca0d5993 fix: fix diff printing
- siderolabs/talos@c8a7a2c68 fix: ignore errors to stop pods
- siderolabs/talos@cfc43b0ac fix: handle empty registry config

### 1.9.5

- siderolabs/talos@dd629ad5f chore: fix the mount cache ids in the Dockerfile
- siderolabs/talos@7f8923452 fix: handle dynamic HTTP proxy settings for discovery client
- siderolabs/talos@9a293327a fix: multiple fixes for dashboard/no data
- siderolabs/talos@9d3a2c8df fix: ignore digest part of images when checking version
- siderolabs/pkgs@9a21d6c fix: backport MGLRU patch from Linux 6.13
- siderolabs/pkgs@3ff0ab6 fix: patch Linux with blackhole patch

### 1.9.6

- siderolabs/talos@d11e6b3be fix: do correct backoff for nocloud reconcile
- siderolabs/talos@2785ab9eb fix: fix Gvisor tests with containerd patch
- siderolabs/talos@c932d4c51 fix: extension services logging to console
- siderolabs/talos@7c8b1fd15 fix: relax etcd APIs RBAC requirements
- siderolabs/talos@b03ad9d86 fix: preserve kubelet image suffix
- siderolabs/talos@b9dd6d8d3 fix: handle encryption type mismatch
- siderolabs/talos@757a369cf fix: containerd auth hostname in the config
- siderolabs/talos@3355c2001 fix: image cache generation on Windows
- siderolabs/talos@9b0604af7 fix: ignore missing config (nocloud) via cidata
- siderolabs/talos@9efea0603 fix: reconnect on SideroLink tunnel on/off change


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.9.6**, the newest release recorded here for this line.

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

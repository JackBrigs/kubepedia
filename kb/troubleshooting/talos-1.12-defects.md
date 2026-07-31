---
id: TROUBLE-TALOS_1_12_DEFECTS
type: troubleshooting
title: "talos 1.12: defects fixed in the 1.12 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.12.0 <1.13.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - talos 1.12 known issues
  - talos 1.12 fixed in
  - is this talos bug already fixed
tags:
  - troubleshooting
  - upgrade
  - talos
sources:
  - type: docs
    path: siderolabs/talos release notes for the 1.12 line — bug-fix entries
    url: https://github.com/siderolabs/talos/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# talos 1.12: defects fixed in the 1.12 line

## Summary

**255 defects** the project fixed across **11 releases** of the 1.12 line, from 1.12.0 to
1.12.10. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.12.0

- siderolabs/talos@82553b2a1 fix: mount volume mount/unmount race
- siderolabs/talos@33f6e22ec fix: bond setting change detection
- siderolabs/talos@ce286825a fix: drop the Omni API URL check on IP address
- siderolabs/talos@e195427c1 docs: fix the talosctl cluster create help output
- siderolabs/talos@21a914a1d fix: exclude new Virtual IPs configured with new config
- siderolabs/talos@ca645777d fix: provide json support in `nft` binary
- siderolabs/talos@47198780b fix: bond configuration with new settings
- siderolabs/talos@03a424bdf fix: disable kexec on arm64
- siderolabs/talos@66e67fd13 fix: discard better klog message from Kubernetes client
- siderolabs/talos@d8403498c fix: disable kexec in talosctl cluster create on arm64
- siderolabs/talos@5ced4258c fix: do not override DNS on MacOS
- siderolabs/talos@fabf3f0e7 fix: selection of boot entry
- siderolabs/talos@93cec4b9d fix: update CNI plugins to 1.9.0
- siderolabs/talos@964098d96 fix: update KubeSpan MSS clamping
- siderolabs/talos@bc4de5b79 fix: constants file
- siderolabs/talos@297336549 fix: correct condition to use UKI cmdline in GRUB
- siderolabs/talos@e79a94d57 fix: adapt SELinuxSuite.TestNoPtrace to new strace version
- siderolabs/talos@7a1bb4c26 fix: mark secureboot as supported for metal
- siderolabs/talos@5c6ee6ace fix: clear provisioning data on SideroLink config change
- siderolabs/talos@6dc8e82b3 fix: add a timeout for DNS resolving for NTP
- siderolabs/talos@a7dbbbd4d fix: don't disable LACP by default
- siderolabs/talos@3ca342c09 chore: fix longhorn test
- siderolabs/talos@364ebb6ba fix: selection of boot entry
- siderolabs/talos@7531fcbc7 test: fix flaky LinkSpec/Wireguard test
- siderolabs/talos@1dbc64d69 fix: simplify OOM expression
- siderolabs/talos@0ffb1d857 fix: trim trailing dots from certificate SANs
- siderolabs/talos@9a2f6d9c9 fix: support specifying patch file without '@' symbol
- siderolabs/talos@582b0feab fix: assign value of multicast setting properly
- siderolabs/talos@139cce3b4 fix: add CA subject to generated certificate
- siderolabs/talos@15465f0c5 fix: add more resilient move
- siderolabs/talos@36152d278 fix: add riscv64 talosctl to release artifacts
- siderolabs/talos@e62384ba3 fix: re-creating STATE after partition drop
- siderolabs/talos@68560b53a fix: split volume/disk locators
- siderolabs/talos@2c3d30e94 docs: fix image-cache-path flag description
- siderolabs/talos@00fe50d86 fix: uefi bootorder setting
- siderolabs/talos@43f4e317f fix: race between VolumeConfigController and UserVolumeConfigController
- siderolabs/talos@cf014cb5d fix: only set default bootloader if none is set
- siderolabs/talos@e9b016f80 fix: use strict platform match when pulling images
- siderolabs/talos@75fe47582 fix: stop attaching to tearing down mount parents
- siderolabs/talos@c93a9c6b4 fix: improve OOM controller stability and make test strict on false positives
- siderolabs/talos@2af69ff35 fix: provide minimal platform metadata always
- siderolabs/talos@92eeaa482 fix: update YAML library
- siderolabs/talos@aa24da9aa fix: bump kubelet credendial provider config to v1
- siderolabs/talos@4c095281b fix: set a timeout for SideroLink provision API call
- siderolabs/talos@75e4c4a59 fix: log duplication on log senders
- siderolabs/talos@e3cbc92c0 fix: add video kernel module to arm
- siderolabs/talos@d69305a67 fix: userspace wireguard handling
- siderolabs/talos@ee5fee7c8 fix: image-signer commands
- siderolabs/talos@fb4bfe851 chore: fix LVM test
- siderolabs/talos@43b1d7537 fix: validate provisioner when destroying local clusters
- siderolabs/talos@b494c54c8 fix: talos import on non-linux
- siderolabs/talos@d11072726 fix: provide offset for partitions in discovered volumes
- siderolabs/talos@9890a9a31 test: fix OOM test
- siderolabs/talos@ac60a9e27 fix: update test for PCI driver rebind/IOMMU
- siderolabs/talos@da92a756d fix: drop 'ro' falg from defaults
- siderolabs/talos@28fd2390c fix: imager build on arm64
- siderolabs/talos@37e4c40c6 fix: skip module signature tests on docker provisioner only
- siderolabs/talos@4adcda0f5 fix: reserve the apid and trustd ports from the ephemeral port range
- siderolabs/talos@1e5c4ed64 fix: build talosctl image cache-serve non-linux
- siderolabs/talos@2f23fedeb fix: file leak in reading cgroups
- siderolabs/talos@4ca58aeb8 fix: make Akamai platform usable
- siderolabs/talos@8d1468209 fix: stop populating apiserver cert SANs
- siderolabs/talos@02473244c fix: wait for mount status to be proper mode
- siderolabs/talos@825622d90 fix: resource proto definitions
- siderolabs/talos@33fb48f8f fix: add dashboard spinner
- siderolabs/talos@34e107e1b docs: fix broken link
- siderolabs/talos@435dcbf82 fix: provide nocloud metadata with missing network config
- siderolabs/talos@33544bde9 fix: minor improvements to fs
- siderolabs/talos@eadbdda94 fix: uefi boot order setting
- siderolabs/talos@cd9fb2743 fix: support secure HTTP proxy with gRPC dial
- siderolabs/talos@5ca841804 fix: nftables flaky test
- siderolabs/talos@3472d6e79 fix: revert "chore: use new mount/v3 package in efivarfs"
- siderolabs/talos@362a8e63b fix: change the compression format
- siderolabs/talos@6e58f58aa fix: mkdir artifacts path
- siderolabs/talos@fe36b3d32 fix: stop returning EINVAL on remount of detached mounts
- siderolabs/talos@1e604cbf5 fix: don't set broadcast for /31 and /32 addresses
- siderolabs/talos@ab847310e fix: provide refreshing CA pool (resolvers)
- siderolabs/talos@724857dec fix(ci): skip netbird extension for tests
- siderolabs/talos@e06a08698 fix: default gateway as string
- siderolabs/talos@7ed07412e fix: uefi boot entry handling logic
- siderolabs/talos@51db5279c fix: bump trustd memory limit
- siderolabs/talos@25204dc8a fix(machined): change `constants.MinimumGOAMD64Level` using build tag
- siderolabs/talos@1cde53d01 test: fix several issues with tests
- siderolabs/talos@c3ae92b14 fix: build kernel checks only on linux
- siderolabs/talos@07acb3bd2 fix: use correct order to determine SideroV1 keys directory path
- siderolabs/talos@2d57fa002 fix: trim zero bytes in the DHCP host & domain response
- siderolabs/talos@69ab076b4 fix: re-create cgroups when restarting runners
- siderolabs/talos@e168512dd fix: apply 'ro' flag to iso9660 filesystems
- siderolabs/talos@7f7acfbb9 docs: fix typo in doc
- siderolabs/talos@f85f82f32 test: fix flakiness in RawVolumes test
- siderolabs/talos@2fd2ab4e4 fix: remove CoreDNS cpu limit
- siderolabs/talos@c1360103b docs: fix command for uploading image on Hetzner
- siderolabs/talos@43b5b9d89 fix: correctly handle status-code 204
- siderolabs/talos@3000d9e43 fix: don't bootstrap talos cluster if there's no config present
- siderolabs/talos@53f18c2f6 fix: enable support for VMWare arm64
- siderolabs/talos@e8f1ec1c5 docs: fix broken create qemu command v1.11 docs
- siderolabs/talos@8aa7b3933 fix: bring back linux/armv7 build and update xz
- siderolabs/talos@cfef3ad45 fix: drop linux/armv7 build
- siderolabs/talos@42ea2ac50 fix: update xz module (security)
- siderolabs/talos@4fcfd35b9 docs: fix module name example
- siderolabs/talos@07eb4d7ec fix: set default ram unit to MiB instead of MB
- siderolabs/talos@558e0b09a test: fix the Image Factory PXE boot test
- siderolabs/talos@2f5a16f5e fix: make --with-uuid-hostnames functionality available to qemu provider
- siderolabs/talos@99674ef20 docs: apply fixes for what is new
- siderolabs/talos@92db677b5 fix: image cache lockup on a missing volume
- siderolabs/talos@9c97ed886 fix: version contract parsing in encryption keys handling
- siderolabs/talos@1fc670a08 fix: dial with proxy
- siderolabs/talos@8817cc60c fix: actually use SIDEROV1_KEYS_DIR env var if it's provided
- siderolabs/talos@7a52d7489 fix: kubernetes upgrade options for kubelet
- siderolabs/talos@b5d5ef79e fix: set secs field in DHCPv4 packets
- siderolabs/talos@b967c587d docs: fix clone URL to include `.git`
- siderolabs/talos@701fe774b docs: fix cilium links and bump to 1.18.0
- siderolabs/talos@06a6c0fe3 refactor: fix deadcode elimination with godbus
- siderolabs/talos@ada51ff69 fix: unmarshal encryption STATE from META
- siderolabs/talos@53055bdf4 docs: fix typo in kubevirt page
- siderolabs/talos@8d12db480 fix: one more attempt to fix volume mount race on restart
- siderolabs/talos@7ad439ac3 fix: enforce minimum size on user volumes if not set explicitly
- siderolabs/talos@50e37aefd fix: live reload of TLS client config for discovery client
- siderolabs/talos@727101926 fix(ci): use a random suffix for ami names
- siderolabs/talos@d62e255c2 fix: issues with reading GPT
- siderolabs/talos@2bc37bd2c docs: fix error in kernel module guide
- siderolabs/talos@06ef7108a fix: issue with volume remount on service restart
- siderolabs/talos@af8a2869d fix: do not download artifacts for cron Grype scan
- siderolabs/talos@38e176e59 chore(ci): fix datasource versioning
- siderolabs/talos@136a899aa chore: regenerate release step with signing fixes
- siderolabs/go-api-signature@8b046e5 fix: do not decode the signature in the plain key from base64
- siderolabs/go-api-signature@68478e2 fix: return `invalid signature` error when a signature is required
- siderolabs/go-talos-support@e0738a9 fix: set pod name in k8s kube-system log filenames
- siderolabs/pkgs@25f8db7 fix: add json support to nftables binary
- siderolabs/pkgs@8b594c4 fix: drop containerd cgroups patch
- siderolabs/pkgs@1fc8435 fix: patch containerd 2.1.5 with cgroups fix patch
- siderolabs/pkgs@cd63cf9 fix: regenerate configs
- siderolabs/pkgs@ce742ba fix: add missing kernel config entries
- siderolabs/pkgs@332303e fix: rollback libseccomp version
- siderolabs/pkgs@20b1849 fix: revert "feat" support adding extra trusted certificates in the kernel"
- siderolabs/pkgs@61d8b44 chore: fix renovate config for urcu & hailort
- siderolabs/pkgs@7fe686d fix: build nftables with embedded gmp
- siderolabs/pkgs@e3b2094 fix: fix build for new NVIDIA drivers
- siderolabs/pkgs@0edf426 fix: backport CVE kernel patches to 6.12
- siderolabs/pkgs@16b5fac fix: re-enable CPUSETS_V1 cgroups controller
- siderolabs/pkgs@895a86b fix: enable ISCSI IBFT
- siderolabs/tools@916b464 fix: add pkgconf for ncurses, fix Renovate configs, bump deps
- siderolabs/tools@7c7328b fix: set regex in renovate config directly
- siderolabs/tools@3ab353b fix: modify renovate regex on ca_certificates

### 1.12.1

- siderolabs/talos@c31067173 fix: disable swap for system services
- siderolabs/talos@943984167 fix: probe small images correctly
- siderolabs/talos@42df71637 fix: invalid versions check in talos-bundle
- siderolabs/talos@a3e90e445 fix: make upgrade work with SELinux enforcing=1

### 1.12.2

- siderolabs/talos@30da0bc19 fix: oracle platform file format
- siderolabs/talos@7ddb37b1f fix: make OOM expression a bit less sensitive
- siderolabs/talos@e438ec23e fix: marshal of FailOverMac property
- siderolabs/talos@717ed7265 fix: check if the device is not mounted when wiping
- siderolabs/talos@c95c9fd06 fix: wipe the first/last 1MiB in addition to wiping by signatures
- siderolabs/talos@52bed358d fix: add talos version to Hetzner Cloud client user agent
- siderolabs/talos@0e447a431 fix: make OOM controller more precise by considering separate cgroup PSI
- siderolabs/talos@3b974b99e fix: sort mirrors and tls configs when generating the machine config
- siderolabs/talos@eb8480c4c fix: panic in configpatcher when the whole section is missing
- siderolabs/talos@4d44306dd fix: wipe disk by signatures
- siderolabs/talos@d9480eef2 fix: resolve SideroLink Wireguard endpoint on reconnect
- siderolabs/talos@e16c2d5bb fix: handle correctly incomplete RegistryTLSConfig
- siderolabs/talos@dedd273df fix: bond config via platform
- siderolabs/talos@f527cff23 fix: allow HostnameConfig to be used with incomplete machine config
- siderolabs/talos@10918136c fix: lock down etcd listen address to IPv4 localhost
- siderolabs/talos@9f8d938db fix: print talosctl images to release notes
- siderolabs/talos@95433c167 fix: update VIP config example
- siderolabs/pkgs@4f8efaf fix: enable pinctrl for Raspberry Pi 5

### 1.12.3

- siderolabs/talos@b8f824525 fix: add hostname to endpoints
- siderolabs/talos@3aa153992 fix: implement merger for PercentageSize
- siderolabs/talos@4a3385dfb fix: undo CRLF on Windows (talosctl edit)
- siderolabs/talos@b8cdb6100 fix(talosctl): pass --k8s-endpoint flag to rotate-ca kubernetes rotation
- siderolabs/talos@27cbe29cc fix: skip empty documents on config decoding
- siderolabs/talos@8f49dd220 fix: open the filesystem as read-only
- siderolabs/talos@b2a83d12a fix: always set advertised peer URLs
- siderolabs/talos@249acdbb5 fix: fallback to /proc/meminfo for memory modules
- siderolabs/talos@bc56bdff7 fix: add warnings to 802.3ad bond

### 1.12.4

- siderolabs/talos@c277d0119 fix: ignore volumes in wave calculation without provisioning
- siderolabs/talos@f90af88d8 fix: use node podCIDRs for kubespan advertiseKubernetesNetworks
- siderolabs/talos@924125420 fix: typo with rpi_5 profile name
- siderolabs/talos@64f49851a fix: swap volume configuration for min/max size
- siderolabs/talos@639c1c928 fix: mismerge of nft with json support

### 1.12.5

- siderolabs/talos@4f978a747 fix: correctly calculate end ranges for nftables sets
- siderolabs/talos@628487715 fix: use correct dhcp option for unicast dhcp renewal
- siderolabs/talos@dcf23be4f fix: ignore image digest when doing upgrade-k8s
- siderolabs/talos@f8a2a9b7a fix(machined): opennebula: process ETH*_ vars regardless of NETWORK context flag
- siderolabs/talos@db9ff23ae fix: patch with delete for LinkConfigs
- siderolabs/talos@e0c38e2ae fix: update path handling on talosctl cgroups
- siderolabs/talos@ca2d4c146 fix: stop Kubernetes client from dynamically reloading the certs
- siderolabs/talos@c3b04844e fix: hold user volumes root mountpoint
- siderolabs/talos@d935420b2 fix: handle raw encryption keys with `\n` properly
- siderolabs/talos@7fe1a47af fix: remove stale endpoints
- siderolabs/talos@3ea08888a fix: allow static hosts in `/etc/hosts` without hostname
- siderolabs/talos@5ebb00fdc fix: switch to better Myers algorithm implementation
- siderolabs/talos@1ce9328e4 fix: disks flag parsing and handling in create qemu command
- siderolabs/talos@1f989dfb0 fix: read multi-doc machine config with newer talosctl

### 1.12.6

- siderolabs/talos@9d5638f4c fix: accept image cache volume encryption config
- siderolabs/talos@0f018bf80 fix: panic in hardware.SystemInfoController
- siderolabs/talos@c46b89807 fix: validate missing apiVersion in config document decoder
- siderolabs/talos@c47cad9ec fix: pull in a fix for dmesg timestamps
- siderolabs/talos@190336a66 fix: prevent stale discovered volumes reads
- siderolabs/talos@217e9bb02 fix: bring in new version of go-cmd and go-blockdevice
- siderolabs/talos@d7779a5ba fix: stop pulling wrong platform for images
- siderolabs/talos@eb6eb664a fix(machined): support USERDATA legacy fallback in OpenNebula driver
- siderolabs/talos@93878c079 fix(machined): align OpenNebula hostname precedence with reference
- siderolabs/talos@501924e5a fix(machined): use ParseFQDN for hostname parsing in OpenNebula

### 1.12.7

- siderolabs/talos@c1ea8dbc7 test: fix OOM test flake
- siderolabs/talos@d5b691b8f fix: watch kubelet's kubeconfig and time out for cache sync
- siderolabs/talos@27655c5bc fix: propagate route table down to the resource
- siderolabs/talos@fcda84bc4 fix: boot entry detection
- siderolabs/talos@330561c87 fix: do not flip machine stage to rebooting during shutdown
- siderolabs/talos@8ef448884 fix: zfs extensions test
- siderolabs/talos@8bc593d17 fix: wrong slot of encryption key was logged
- siderolabs/talos@89f561593 fix: panic in reading PCR values
- siderolabs/talos@0654a7f7e fix: handle ISOs with zeroes in volume labels
- siderolabs/talos@e16007b44 fix: unseal with "slow" TPM
- siderolabs/talos@388a56b79 fix: incorrect route source for on-link routes
- siderolabs/talos@7e42474c5 test: fix the flakes in tests with trusted roots
- siderolabs/pkgs@86d6af1 fix: install apparmor parser require config files
- siderolabs/pkgs@34de6db fix: support disabling module signature verification

### 1.12.8

- siderolabs/talos@faff61707 fix: update containerd to 2.2.4
- siderolabs/talos@99a1aabb8 test: fix flaky tests
- siderolabs/talos@d4a83c8f6 fix: provide proper AWS platform metadata
- siderolabs/talos@ad7bfb641 fix: add missing kernel modules in rootfs
- siderolabs/talos@55cd11acc fix: stale discovered volume children
- siderolabs/talos@fbfe83f60 fix: do not pick up a system disk from a loop device
- siderolabs/talos@7e035bcb6 fix: bump go-kmsg to fix the timestamp drift
- siderolabs/talos@0f23c2c4f fix: make lacp active nilable
- siderolabs/talos@c00250f8f fix: reset the ticker when the KubeSpan is disabled/enabled
- siderolabs/talos@07a0e935d fix: replace Canal manifest with a more recent one
- siderolabs/go-kmsg@65e97cb fix: boot time offset calculation
- siderolabs/pkgs@9a77690 fix: macb silent TX stall on BCM2712/RP1 (v2 patches from netdev)
- siderolabs/pkgs@dc3a7c1 feat(kernel): backport two PCI bridge realloc fixes from v6.19
- siderolabs/pkgs@dd845d1 docs: list net macb silent TX stall fixes in kernel/build/patches/README.md
- siderolabs/pkgs@df2aee2 fix: macb silent TX stall on BCM2712/RP1 (RFC patches from netdev)
- siderolabs/tools@2584442 fix: renovate configs

### 1.12.9

- siderolabs/talos@cba53b450 fix: revert coredns to 1.14.2
- siderolabs/talos@70a9d61d1 fix: bump number of open files for etcd
- siderolabs/talos@045146c1d fix: guard apply config API call
- siderolabs/talos@6593d3b00 fix: honor FailurePauseTimeout when pausing before reboot
- siderolabs/talos@cd429e9e4 fix: relax LUKS header validation
- siderolabs/talos@4c288caf2 fix: mark more resources as sensitive
- siderolabs/talos@3c576021e fix: etcd client leak in the (legacy) Upgrade API
- siderolabs/talos@e002e470c fix: recreate dns server and listeners on host DNS runner restart
- siderolabs/talos@9b12c5178 fix: bring in a change to BCM2712_MIP
- siderolabs/talos@dd4926f31 fix: touch rootfs files with SOURCE_DATE_EPOCH
- siderolabs/talos@d040a7d84 fix: relax hostname config validation
- siderolabs/talos@b63a69bc6 fix: memorymodules resource reporting
- siderolabs/pkgs@435044b fix: avoid page_table_check BUG on time namespace VVAR page
- siderolabs/pkgs@a909a84 fix: disable PAGE_TABLE_CHECK_ENFORCED in kernel config
- siderolabs/pkgs@af985d6 fix: enable CONFIG_BCM2712_MIP as built-in in arm64 kernel config
- siderolabs/tools@3841297 chore: bump openssl, libcap, fakeroot; fix texinfo

### 1.12.10

- siderolabs/talos@40caeece8 fix: provide cooldown period for the QoS trigger
- siderolabs/talos@36b7dc2da fix: align documented image cache partition label
- siderolabs/talos@b4bb3f1a2 fix: kubelet stuck restarting
- siderolabs/pkgs@2befe8b fix: patch Linux kernel for tunnel metadata buffer overflow
- siderolabs/pkgs@59392e8 fix: enable CONFIG_IFB as a module


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.12.10**, the newest release recorded here for this line.

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

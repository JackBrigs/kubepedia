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

**108 defects** the project fixed across **11 releases** of the 1.12 line, from 1.12.0 to
1.12.10. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.12.0

- fix: drop the Omni API URL check on IP address
- fix: exclude new Virtual IPs configured with new config
- fix: discard better klog message from Kubernetes client
- fix: disable kexec in talosctl cluster create on arm64
- fix: correct condition to use UKI cmdline in GRUB
- fix: adapt SELinuxSuite.TestNoPtrace to new strace version
- fix: clear provisioning data on SideroLink config change
- fix: trim trailing dots from certificate SANs
- fix: support specifying patch file without '@' symbol
- fix: assign value of multicast setting properly
- fix: add riscv64 talosctl to release artifacts
- fix: race between VolumeConfigController and UserVolumeConfigController
- fix: only set default bootloader if none is set
- fix: use strict platform match when pulling images
- fix: stop attaching to tearing down mount parents
- fix: improve OOM controller stability and make test strict on false positives
- fix: provide minimal platform metadata always
- fix: bump kubelet credendial provider config to v1
- fix: set a timeout for SideroLink provision API call
- fix: validate provisioner when destroying local clusters
- fix: provide offset for partitions in discovered volumes
- fix: skip module signature tests on docker provisioner only
- fix: reserve the apid and trustd ports from the ephemeral port range
- fix: build talosctl image cache-serve non-linux
- fix: provide nocloud metadata with missing network config
- fix: support secure HTTP proxy with gRPC dial
- fix: revert "chore: use new mount/v3 package in efivarfs"
- fix: stop returning EINVAL on remount of detached mounts
- fix: don't set broadcast for /31 and /32 addresses
- fix(machined): change `constants.MinimumGOAMD64Level` using build tag
- fix: use correct order to determine SideroV1 keys directory path
- fix: trim zero bytes in the DHCP host & domain response
- fix: re-create cgroups when restarting runners
- fix: don't bootstrap talos cluster if there's no config present
- fix: bring back linux/armv7 build and update xz
- fix: set default ram unit to MiB instead of MB
- fix: make --with-uuid-hostnames functionality available to qemu provider
- fix: version contract parsing in encryption keys handling
- fix: actually use SIDEROV1_KEYS_DIR env var if it's provided
- fix: one more attempt to fix volume mount race on restart
- fix: enforce minimum size on user volumes if not set explicitly
- fix: live reload of TLS client config for discovery client
- fix: issue with volume remount on service restart
- fix: do not download artifacts for cron Grype scan
- fix: do not decode the signature in the plain key from base64
- fix: return `invalid signature` error when a signature is required
- fix: set pod name in k8s kube-system log filenames
- fix: patch containerd 2.1.5 with cgroups fix patch
- fix: revert "feat" support adding extra trusted certificates in the kernel"
- fix: add pkgconf for ncurses, fix Renovate configs, bump deps
- fix: modify renovate regex on ca_certificates

### 1.12.1

- fix: make upgrade work with SELinux enforcing=1

### 1.12.2

- fix: make OOM expression a bit less sensitive
- fix: check if the device is not mounted when wiping
- fix: wipe the first/last 1MiB in addition to wiping by signatures
- fix: add talos version to Hetzner Cloud client user agent
- fix: make OOM controller more precise by considering separate cgroup PSI
- fix: sort mirrors and tls configs when generating the machine config
- fix: panic in configpatcher when the whole section is missing
- fix: resolve SideroLink Wireguard endpoint on reconnect
- fix: handle correctly incomplete RegistryTLSConfig
- fix: allow HostnameConfig to be used with incomplete machine config
- fix: lock down etcd listen address to IPv4 localhost

### 1.12.3

- fix(talosctl): pass --k8s-endpoint flag to rotate-ca kubernetes rotation
- fix: fallback to /proc/meminfo for memory modules

### 1.12.4

- fix: ignore volumes in wave calculation without provisioning
- fix: use node podCIDRs for kubespan advertiseKubernetesNetworks
- fix: swap volume configuration for min/max size

### 1.12.5

- fix: correctly calculate end ranges for nftables sets
- fix: use correct dhcp option for unicast dhcp renewal
- fix: ignore image digest when doing upgrade-k8s
- fix(machined): opennebula: process ETH*_ vars regardless of NETWORK context flag
- fix: update path handling on talosctl cgroups
- fix: stop Kubernetes client from dynamically reloading the certs
- fix: handle raw encryption keys with `\n` properly
- fix: allow static hosts in `/etc/hosts` without hostname
- fix: switch to better Myers algorithm implementation
- fix: disks flag parsing and handling in create qemu command
- fix: read multi-doc machine config with newer talosctl

### 1.12.6

- fix: accept image cache volume encryption config
- fix: validate missing apiVersion in config document decoder
- fix: bring in new version of go-cmd and go-blockdevice
- fix(machined): support USERDATA legacy fallback in OpenNebula driver
- fix(machined): align OpenNebula hostname precedence with reference
- fix(machined): use ParseFQDN for hostname parsing in OpenNebula

### 1.12.7

- fix: watch kubelet's kubeconfig and time out for cache sync
- fix: propagate route table down to the resource
- fix: do not flip machine stage to rebooting during shutdown
- fix: handle ISOs with zeroes in volume labels
- fix: incorrect route source for on-link routes
- fix: install apparmor parser require config files
- fix: support disabling module signature verification

### 1.12.8

- fix: do not pick up a system disk from a loop device
- fix: reset the ticker when the KubeSpan is disabled/enabled
- fix: replace Canal manifest with a more recent one
- fix: macb silent TX stall on BCM2712/RP1 (v2 patches from netdev)
- feat(kernel): backport two PCI bridge realloc fixes from v6.19
- fix: macb silent TX stall on BCM2712/RP1 (RFC patches from netdev)

### 1.12.9

- fix: honor FailurePauseTimeout when pausing before reboot
- fix: etcd client leak in the (legacy) Upgrade API
- fix: recreate dns server and listeners on host DNS runner restart
- fix: touch rootfs files with SOURCE_DATE_EPOCH
- fix: avoid page_table_check BUG on time namespace VVAR page
- fix: disable PAGE_TABLE_CHECK_ENFORCED in kernel config
- fix: enable CONFIG_BCM2712_MIP as built-in in arm64 kernel config

### 1.12.10

- fix: provide cooldown period for the QoS trigger
- fix: align documented image cache partition label
- fix: patch Linux kernel for tunnel metadata buffer overflow


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

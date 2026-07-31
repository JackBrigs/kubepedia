---
id: TROUBLE-TALOS_1_13_DEFECTS
type: troubleshooting
title: "talos 1.13: defects fixed in the 1.13 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.13.0 <1.14.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - talos 1.13 known issues
  - talos 1.13 fixed in
  - is this talos bug already fixed
tags:
  - troubleshooting
  - upgrade
  - talos
sources:
  - type: docs
    path: siderolabs/talos release notes for the 1.13 line — bug-fix entries
    url: https://github.com/siderolabs/talos/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# talos 1.13: defects fixed in the 1.13 line

## Summary

**109 defects** the project fixed across **6 releases** of the 1.13 line, from 1.13.0 to
1.13.7. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.13.0

- fix: revert add extraArgs from service-account-issuer
- fix: revert use append instead of prepend in service-account-issuer
- fix(talosctl): ensure uncordon runs after reboot/upgrade errors
- fix: watch kubelet's kubeconfig and time out for cache sync
- fix: propagate route table down to the resource
- fix: do not flip machine stage to rebooting during shutdown
- fix: return failed precondition on upgrade when not installed
- fix(machined): clear stale bond ARP/NS targets on decode
- fix: encode extra args fields in resources with new id
- fix: upgrade API in maintenance mode (legacy)
- fix: validate hostDNS forwarding requires hostDNS to be enabled
- fix(talosctl): always use default GRPC dial options
- fix: create correct blackhole routes for IPv4
- fix: don't set xattrs while decompressing extensions
- fix: handle ISOs with zeroes in volume labels
- fix: add os:meta:writer role to the dashboard
- fix: drop unused type from ExternalVolume schema
- fix: add metal-agent mode to runtime capabilities
- fix: incorrect route source for on-link routes
- fix: allow blockdevice wipe in maintenance mode
- fix: add symlinks nvidia-ctk and nvidia-cdi-hook in /usr/bin
- fix: drop aws & azure KMS APIs from the machined build
- fix: accept image cache volume encryption config
- fix: validate missing apiVersion in config document decoder
- fix(machined): support USERDATA legacy fallback in OpenNebula driver
- fix(machined): align OpenNebula hostname precedence with reference
- fix(machined): use ParseFQDN for hostname parsing in OpenNebula
- fix: use non-sensitive resource for health check precondition
- fix: skip some readiness checks when the CNI is disabled
- fix: correctly calculate end ranges for nftables sets
- fix: use correct dhcp option for unicast dhcp renewal
- fix: ignore image digest when doing upgrade-k8s
- fix(machined): opennebula: process ETH*_ vars regardless of NETWORK context flag
- fix: image cache test fails with 'no space left on device'
- fix: bring in new version of go-cmd and go-blockdevice
- fix: update path handling on talosctl cgroups
- fix: add owning inventory annotation to talos manifests
- fix: stop Kubernetes client from dynamically reloading the certs
- fix: handle raw encryption keys with `\n` properly
- fix: improve OpenStack bare metal network configuration reliability
- fix: allow static hosts in `/etc/hosts` without hostname
- fix: switch to better Myers algorithm implementation
- fix: use mcopy instead of diskfs to populate VFAT
- fix: disks flag parsing and handling in create qemu command
- fix: read multi-doc machine config with newer talosctl
- fix: ignore volumes in wave calculation without provisioning
- fix: swap volume configuration for min/max size
- fix: allow to expose a port multiple times in Docker
- fix(talosctl): pass --k8s-endpoint flag to rotate-ca kubernetes rotation
- fix: use node podCIDRs for kubespan advertiseKubernetesNetworks
- fix: fallback to /proc/meminfo for memory modules
- fix: overwrite resolver config with machine config
- fix: make OOM expression a bit less sensitive
- fix: wipe the first/last 1MiB in addition to wiping by signatures
- fix: make OOM controller more precise by considering separate cgroup PSI
- fix: check if the device is not mounted when wiping
- fix: add talos version to Hetzner Cloud client user agent
- fix: use append instead of prepend in service-account-issuer
- fix: sort mirrors and tls configs when generating the machine config
- fix: panic in configpatcher when the whole section is missing
- fix: resolve SideroLink Wireguard endpoint on reconnect
- fix: drop the persist config flag from gen config
- fix: handle correctly incomplete RegistryTLSConfig
- fix: allow HostnameConfig to be used with incomplete machine config
- fix: lock down etcd listen address to IPv4 localhost
- fix: skip sync test when kube-proxy is disabled
- fix: do not allocate for the actual disk image file
- fix: make upgrade work with SELinux enforcing=1
- fix: drop the Omni API URL check on IP address
- fix: exclude new Virtual IPs configured with new config
- fix: update containerd 2.2.0 with cgroups patch
- fix: discard better klog message from Kubernetes client
- fix: disable kexec in talosctl cluster create on arm64
- fix: correct condition to use UKI cmdline in GRUB
- fix: adapt SELinuxSuite.TestNoPtrace to new strace version
- fix: clear provisioning data on SideroLink config change
- fix: support specifying patch file without '@' symbol
- fix: trim trailing dots from certificate SANs
- fix: assign value of multicast setting properly
- fix: add riscv64 talosctl to release artifacts
- fix: stop using custom dialer for Kubernetes client
- fix: add trailing new line when writing to logger
- fix: support disabling module signature verification
- fix: install apparmor parser require config files
- feat: patch containerd 2.2.0 with cgroups fix patch

### 1.13.3

- fix: bump Kubernetes to 1.36.1 in one more place
- fix: rework how scheduler config is marshaled
- fix: restore some shared (and some lower tier slave) mount propagation
- fix: image verification issue with registry.k8s.io
- fix: macb silent TX stall on BCM2712/RP1 (v2 patches from netdev)

### 1.13.4

- fix: handle cluster-scoped resources with a namespace correctly
- fix: recreate dns server and listeners on host DNS runner restart
- fix: marshal kube-scheduler config correctly with int types
- fix: etcd client leak in the (legacy) Upgrade API
- fix: touch rootfs files with SOURCE_DATE_EPOCH
- fix: ignore cgroups with zero rank in OOM handler
- fix: handle cluster-scoped resources with a ns correctly
- fix: disable PAGE_TABLE_CHECK_ENFORCED in kernel config
- fix: enable CONFIG_BCM2712_MIP as built-in in arm64 kernel config

### 1.13.5

- fix: stop the log persistence and close all files on shutdown
- fix: honor FailurePauseTimeout when pausing before reboot
- fix: avoid page_table_check BUG on time namespace VVAR page

### 1.13.6

- fix: provide cooldown period for the QoS trigger
- fix: align documented image cache partition label
- fix: skip unknown-key check for types with custom YAML unmarshaler
- fix: patch Linux kernel for tunnel metadata buffer overflow

### 1.13.7

- fix: do proper backoff for NTP Kiss-of-Death responses
- fix: provide correct handler for Ctrl-Alt-Delete sequence
- fix: do not block volume lifecycle teardown on failed user volumes


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.13.7**, the newest release recorded here for this line.

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

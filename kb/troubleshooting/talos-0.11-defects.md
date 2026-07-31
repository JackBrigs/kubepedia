---
id: TROUBLE-TALOS_0_11_DEFECTS
type: troubleshooting
title: "talos 0.11: defects fixed in the 0.11 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.11.0 <0.12.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - talos 0.11 known issues
  - talos 0.11 fixed in
  - is this talos bug already fixed
tags:
  - troubleshooting
  - upgrade
  - talos
sources:
  - type: docs
    path: siderolabs/talos release notes for the 0.11 line — bug-fix entries
    url: https://github.com/siderolabs/talos/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# talos 0.11: defects fixed in the 0.11 line

## Summary

**205 defects** the project fixed across **6 releases** of the 0.11 line, from 0.11.0 to
0.11.5. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.11.0

- fix: ignore DeadlineExceeded error correctly on bootstrap
- fix: make forfeit leadership connect to the right node
- fix: ignore 'not a leader' error on forfeit leadership
- fix: workaround 'Unauthorized' errors when accessing Kubernetes API
- fix: fill uuid argument correctly in the config download URL
- fix: make output of `upgrade-k8s` command less scary
- fix: restart the merge controllers on conflict
- fix: ignore deadline exceeded errors on bootstrap
- fix: issue worker apid certs properly on renewal
- fix: don't set bond delay options if miimon is not enabled
- fix: handle cases when merged resource re-appears before being destroyed
- fix: limit apid access to COSI runtime resources
- fix: replace tabs with spaces in console output
- fix: assign source address to the DHCP default gateway routes
- fix: mark kube-proxy as system critical priority
- fix: use localhost API server endpoint for internal communication
- fix: stop etcd client logs from going to the server console
- fix: don't enable RBAC feature in the config for Talos < 0.11
- fix: do not format state partition in the initialize sequence
- fix: update networking stack after Equnix Metal testing
- fix: separate healthy and unknown flags in the service resource
- fix: update retry package with a fix for errors.Is
- fix: wait for the network to be ready in mainteancne mode
- fix: do not add bootstrap contents option if tail events is not 0
- fix: prefer extraConfig over OVF env, skip empty config
- fix: remove conflicting etcd member on rejoin with empty data directory
- fix: drop into maintenance mode if config URL is `none` (metal)
- fix: use COSI runtime DestroyReady input type
- fix: clean up stale snapshots on container start
- fix: add talos.config to the vApp Properties in VMware OVA
- fix: properly compose pattern and header in etcd members output
- fix: stop networkd and pods before leaving etcd on upgrade
- fix: properly populate AllowSchedulingOnMasters option in gen config RPC
- fix: properly pass disk type selector from config to matcher
- fix: stop networkd before leaving etcd on 'reset' path
- fix: update go-blockdevice to fix disk type detection
- fix: update the way NTP sync uses `adjtimex` syscall
- fix: bump crypto library for the CSR verification fix
- fix: use both self-signed and Kubernetes CA to verify Kubelet cert
- fix: update osType in OVA other3xLinux64Guest"
- fix: update etcd client errors, print etcd join failures
- fix: verify CSR signature before issuing a certificate
- fix: make disk type matcher parser case insensitive
- fix: properly detect nvme and sd card disk types
- fix: implement `errors.Is` for all errors in the set
- fix: return UUID in middle endian only on SMBIOS >= 2.6
- fix: build `zbin` utility for both amd64 and arm64

### 0.11.1

- fix: correctly pick route scope for link-local destination
- fix: workaround issues when IPv6 is fully or partially disabled
- fix: ignore DeadlineExceeded error correctly on bootstrap
- fix: make forfeit leadership connect to the right node
- fix: ignore 'not a leader' error on forfeit leadership
- fix: workaround 'Unauthorized' errors when accessing Kubernetes API
- fix: fill uuid argument correctly in the config download URL
- fix: make output of `upgrade-k8s` command less scary
- fix: restart the merge controllers on conflict
- fix: ignore deadline exceeded errors on bootstrap
- fix: issue worker apid certs properly on renewal
- fix: don't set bond delay options if miimon is not enabled
- fix: handle cases when merged resource re-appears before being destroyed
- fix: limit apid access to COSI runtime resources
- fix: replace tabs with spaces in console output
- fix: assign source address to the DHCP default gateway routes
- fix: mark kube-proxy as system critical priority
- fix: use localhost API server endpoint for internal communication
- fix: stop etcd client logs from going to the server console
- fix: don't enable RBAC feature in the config for Talos < 0.11
- fix: do not format state partition in the initialize sequence
- fix: update networking stack after Equnix Metal testing
- fix: separate healthy and unknown flags in the service resource
- fix: update retry package with a fix for errors.Is
- fix: wait for the network to be ready in mainteancne mode
- fix: do not add bootstrap contents option if tail events is not 0
- fix: prefer extraConfig over OVF env, skip empty config
- fix: remove conflicting etcd member on rejoin with empty data directory
- fix: drop into maintenance mode if config URL is `none` (metal)
- fix: use COSI runtime DestroyReady input type
- fix: clean up stale snapshots on container start
- fix: add talos.config to the vApp Properties in VMware OVA
- fix: properly compose pattern and header in etcd members output
- fix: stop networkd and pods before leaving etcd on upgrade
- fix: properly populate AllowSchedulingOnMasters option in gen config RPC
- fix: properly pass disk type selector from config to matcher
- fix: stop networkd before leaving etcd on 'reset' path
- fix: update go-blockdevice to fix disk type detection
- fix: update the way NTP sync uses `adjtimex` syscall
- fix: bump crypto library for the CSR verification fix
- fix: use both self-signed and Kubernetes CA to verify Kubelet cert
- fix: update osType in OVA other3xLinux64Guest"
- fix: update etcd client errors, print etcd join failures
- fix: verify CSR signature before issuing a certificate
- fix: make disk type matcher parser case insensitive
- fix: properly detect nvme and sd card disk types
- fix: implement `errors.Is` for all errors in the set
- fix: return UUID in middle endian only on SMBIOS >= 2.6
- fix: build `zbin` utility for both amd64 and arm64

### 0.11.2

- fix: make ethtool optional in link status controller
- fix: correctly pick route scope for link-local destination
- fix: workaround issues when IPv6 is fully or partially disabled
- fix: ignore DeadlineExceeded error correctly on bootstrap
- fix: make forfeit leadership connect to the right node
- fix: ignore 'not a leader' error on forfeit leadership
- fix: workaround 'Unauthorized' errors when accessing Kubernetes API
- fix: fill uuid argument correctly in the config download URL
- fix: make output of `upgrade-k8s` command less scary
- fix: restart the merge controllers on conflict
- fix: ignore deadline exceeded errors on bootstrap
- fix: issue worker apid certs properly on renewal
- fix: don't set bond delay options if miimon is not enabled
- fix: handle cases when merged resource re-appears before being destroyed
- fix: limit apid access to COSI runtime resources
- fix: replace tabs with spaces in console output
- fix: assign source address to the DHCP default gateway routes
- fix: mark kube-proxy as system critical priority
- fix: use localhost API server endpoint for internal communication
- fix: stop etcd client logs from going to the server console
- fix: don't enable RBAC feature in the config for Talos < 0.11
- fix: do not format state partition in the initialize sequence
- fix: update networking stack after Equnix Metal testing
- fix: separate healthy and unknown flags in the service resource
- fix: update retry package with a fix for errors.Is
- fix: wait for the network to be ready in mainteancne mode
- fix: do not add bootstrap contents option if tail events is not 0
- fix: prefer extraConfig over OVF env, skip empty config
- fix: remove conflicting etcd member on rejoin with empty data directory
- fix: drop into maintenance mode if config URL is `none` (metal)
- fix: use COSI runtime DestroyReady input type
- fix: clean up stale snapshots on container start
- fix: add talos.config to the vApp Properties in VMware OVA
- fix: properly compose pattern and header in etcd members output
- fix: stop networkd and pods before leaving etcd on upgrade
- fix: properly populate AllowSchedulingOnMasters option in gen config RPC
- fix: properly pass disk type selector from config to matcher
- fix: stop networkd before leaving etcd on 'reset' path
- fix: update go-blockdevice to fix disk type detection
- fix: update the way NTP sync uses `adjtimex` syscall
- fix: bump crypto library for the CSR verification fix
- fix: use both self-signed and Kubernetes CA to verify Kubelet cert
- fix: update osType in OVA other3xLinux64Guest"
- fix: update etcd client errors, print etcd join failures
- fix: verify CSR signature before issuing a certificate
- fix: make disk type matcher parser case insensitive
- fix: properly detect nvme and sd card disk types
- fix: implement `errors.Is` for all errors in the set
- fix: return UUID in middle endian only on SMBIOS >= 2.6
- fix: build `zbin` utility for both amd64 and arm64

### 0.11.3

- fix: make ethtool optional in link status controller
- fix: correctly pick route scope for link-local destination
- fix: workaround issues when IPv6 is fully or partially disabled
- fix: ignore DeadlineExceeded error correctly on bootstrap
- fix: make forfeit leadership connect to the right node
- fix: ignore 'not a leader' error on forfeit leadership
- fix: workaround 'Unauthorized' errors when accessing Kubernetes API
- fix: fill uuid argument correctly in the config download URL
- fix: make output of `upgrade-k8s` command less scary
- fix: restart the merge controllers on conflict
- fix: ignore deadline exceeded errors on bootstrap
- fix: issue worker apid certs properly on renewal
- fix: don't set bond delay options if miimon is not enabled
- fix: handle cases when merged resource re-appears before being destroyed
- fix: limit apid access to COSI runtime resources
- fix: replace tabs with spaces in console output
- fix: assign source address to the DHCP default gateway routes
- fix: mark kube-proxy as system critical priority
- fix: use localhost API server endpoint for internal communication
- fix: stop etcd client logs from going to the server console
- fix: don't enable RBAC feature in the config for Talos < 0.11
- fix: do not format state partition in the initialize sequence
- fix: update networking stack after Equnix Metal testing
- fix: separate healthy and unknown flags in the service resource
- fix: update retry package with a fix for errors.Is
- fix: wait for the network to be ready in mainteancne mode
- fix: do not add bootstrap contents option if tail events is not 0
- fix: prefer extraConfig over OVF env, skip empty config
- fix: remove conflicting etcd member on rejoin with empty data directory
- fix: drop into maintenance mode if config URL is `none` (metal)
- fix: use COSI runtime DestroyReady input type
- fix: clean up stale snapshots on container start
- fix: add talos.config to the vApp Properties in VMware OVA
- fix: properly compose pattern and header in etcd members output
- fix: stop networkd and pods before leaving etcd on upgrade
- fix: properly populate AllowSchedulingOnMasters option in gen config RPC
- fix: properly pass disk type selector from config to matcher
- fix: stop networkd before leaving etcd on 'reset' path
- fix: update go-blockdevice to fix disk type detection
- fix: update the way NTP sync uses `adjtimex` syscall
- fix: bump crypto library for the CSR verification fix
- fix: use both self-signed and Kubernetes CA to verify Kubelet cert
- fix: update osType in OVA other3xLinux64Guest"
- fix: update etcd client errors, print etcd join failures
- fix: verify CSR signature before issuing a certificate
- fix: make disk type matcher parser case insensitive
- fix: properly detect nvme and sd card disk types
- fix: implement `errors.Is` for all errors in the set
- fix: return UUID in middle endian only on SMBIOS >= 2.6
- fix: build `zbin` utility for both amd64 and arm64

### 0.11.4

- fix: preserve PMBR bootable, align partitions with minimal I/O size
- fix: verify CSR signature before issuing a certificate
- fix: preserve the PMBR bootable flag when opening GPT partition
- fix: make disk type matcher parser case insensitive
- fix: properly detect nvme and sd card disk types
- fix: implement `errors.Is` for all errors in the set
- fix: return UUID in middle endian only on SMBIOS >= 2.6
- fix: build `zbin` utility for both amd64 and arm64

### 0.11.5

- fix: perform correct PMBR partition calculations


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **0.11.5**, the newest release recorded here for this line.

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

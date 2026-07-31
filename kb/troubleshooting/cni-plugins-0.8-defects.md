---
id: TROUBLE-CNI_PLUGINS_0_8_DEFECTS
type: troubleshooting
title: "cni-plugins 0.8: defects fixed in the 0.8 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.8.0 <0.9.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cni-plugins 0.8 known issues
  - cni-plugins 0.8 fixed in
  - is this cni-plugins bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cni-plugins
sources:
  - type: docs
    path: containernetworking/plugins release notes for the 0.8 line — bug-fix entries
    url: https://github.com/containernetworking/plugins/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cni-plugins 0.8: defects fixed in the 0.8 line

## Summary

**36 defects** the project fixed across **7 releases** of the 0.8 line, from 0.8.0 to
0.8.7. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.8.0

- static - assign a fixed IP address ([#136](https://github.com/containernetworking/plugins/pull/136)), ([#165](https://github.com/containernetworking/plugins/pull/165))
- Correctly DEL on ipam failure for all plugins ([#314](https://github.com/containernetworking/plugins/pull/314))
- Fix bug on ip revert if cmdAdd fails on macvlan and host-device
- host-device: Ensure device is down before rename ([#147](https://github.com/containernetworking/plugins/pull/147))
- Fix -hostprefix option ([#268](https://github.com/containernetworking/plugins/pull/268))
- some DHCP servers expect to request for explicit router options ([#255](https://github.com/containernetworking/plugins/pull/255))
- bridge: release IP in case of error ([#129](https://github.com/containernetworking/plugins/pull/129))
- test: add coveralls support ([#288](https://github.com/containernetworking/plugins/pull/288))
- plugins: correctly output build version, cosmetic cleanups ([#295](https://github.com/containernetworking/plugins/pull/295))
- Move Windows tests to Travis ([#246](https://github.com/containernetworking/plugins/pull/246))

### 0.8.1

- bridge: fix ipMasq setup to use correct source address ([#325](https://github.com/containernetworking/plugins/pull/325))
- fix compilation error on 386 ([#324](https://github.com/containernetworking/plugins/pull/324))
- bandwidth: get bandwidth interface in host ns through container interface ([#321](https://github.com/containernetworking/plugins/pull/321)). fixes [#260](https://github.com/containernetworking/plugins/issues/260)

### 0.8.2

- bandwidth: fix collisions ([#353](https://github.com/containernetworking/plugins/pull/353))
- Fix: failed to set bridge addr: could not add IP address to \"cni0\": file exists ([#366](https://github.com/containernetworking/plugins/pull/366))
- host-device: revert name setting to make retries idempotent ([#357](https://github.com/containernetworking/plugins/pull/357))
- Vendor update go-iptables ([#358](https://github.com/containernetworking/plugins/pull/358)). Vendor update go-iptables to obtain commit f1d0510cabcb710d5c5dd284096f81444b9d8d10
- Remove link Down/Up in MAC address change to prevent route flush ([#364](https://github.com/containernetworking/plugins/pull/364))
- pkg/ip unit test: be agnostic of Linux version ([#349](https://github.com/containernetworking/plugins/pull/349)). on Linux 4.4 the syscall error message is "invalid argument" not "file exists"
- bump containernetworking/cni to v0.7.1 ([#341](https://github.com/containernetworking/plugins/pull/341))

### 0.8.3

- portmap: Fix dual-stack support ([#379](https://github.com/containernetworking/plugins/pull/379))
- integration: fix ip address collision in integration tests ([#409](https://github.com/containernetworking/plugins/pull/409))

### 0.8.5

- bridge: Fix for the case where kernel doesn't have CONFIG_BRIDGE_VLAN_FILTERING ([#434](https://github.com/containernetworking/plugins/pull/434)) fixes [#370](https://github.com/containernetworking/plugins/pull/370)
- vlan: Fix vlan plugin returning error when device is already removed ([#438](https://github.com/containernetworking/plugins/pull/438))

### 0.8.6

- plugins/meta/sbr: Adjusted ipv6 address mask to /128 ([#479](https://github.com/containernetworking/plugins/pull/479)). A /64 mask was used which routed an entire cidr based on source, not only the bound address
- check bridge's port state ([#468](https://github.com/containernetworking/plugins/pull/468)). fix #463
- Reset the route flag before moving the rule ([#472](https://github.com/containernetworking/plugins/pull/472))
- replace juju/errors because of CNCF license scan ([#458](https://github.com/containernetworking/plugins/pull/458)). ref to #457
- loopback: Fix ipv6 address checks ([#442](https://github.com/containernetworking/plugins/pull/442)). Fixes a minor bug in loopback plugin. The IPv6 address check loops over IPv4 addresses

### 0.8.7

- flannel: remove net conf file after DEL succeed ([#449](https://github.com/containernetworking/plugins/pull/449))
- portmap should not perform deletions if not portMapping config received ([#509](https://github.com/containernetworking/plugins/pull/509))
- portmap: don't use unspecified address as iptables rule destination ([#487](https://github.com/containernetworking/plugins/pull/487))
- Fix race condition in GetCurrentNS ([#523](https://github.com/containernetworking/plugins/pull/523))
- firewall: fix generate of admin chain comment ([#506](https://github.com/containernetworking/plugins/pull/506))
- Fix handling of delay in acquiring lease with stp turned on ([#501](https://github.com/containernetworking/plugins/pull/501))
- host-device: Bring interfaces down before moving ([#486](https://github.com/containernetworking/plugins/pull/486))


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **0.8.7**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `containernetworking/plugins`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/cni-plugins.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].

---
id: TROUBLE-KUBE_VIP_0_8_DEFECTS
type: troubleshooting
title: "kube-vip 0.8: defects fixed in the 0.8 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.8.0 <0.9.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kube-vip 0.8 known issues
  - kube-vip 0.8 fixed in
  - is this kube-vip bug already fixed
tags:
  - troubleshooting
  - upgrade
  - kube-vip
sources:
  - type: docs
    path: kube-vip/kube-vip release notes for the 0.8 line — bug-fix entries
    url: https://github.com/kube-vip/kube-vip/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kube-vip 0.8: defects fixed in the 0.8 line

## Summary

**31 defects** the project fixed across **9 releases** of the 0.8 line, from 0.8.0 to
0.8.10. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.8.0

- Fix netmask of ipvs to consider ipv6 case by @lubronzhan in https://github.com/kube-vip/kube-vip/pull/783
- fix: Modify the ImagePullPolicy used by cli manifest by @Bao0ne in https://github.com/kube-vip/kube-vip/pull/805
- fix: add iptables-legacy package by @starbops in https://github.com/kube-vip/kube-vip/pull/809
- fix: add ddns address as a network by @adavis10006 in https://github.com/kube-vip/kube-vip/pull/795
- Fixes on masquerade forwarding mode by @wyike in https://github.com/kube-vip/kube-vip/pull/812
- fixes to linting by @thebsdbox in https://github.com/kube-vip/kube-vip/pull/817
- Examples and fixes to annotation interface by @thebsdbox in https://github.com/kube-vip/kube-vip/pull/819

### 0.8.1

- fix: unecessary string modification by @ShivanshVij in https://github.com/kube-vip/kube-vip/pull/832
- fix: set service's uid in activeService map for inactive services by @starbops in https://github.com/kube-vip/kube-vip/pull/837
- Fixed route deletion when route is used by more than one service by @p-strusiewiczsurmacki-mobica in https://github.com/kube-vip/kube-vip/pull/838
- fix: close file by @testwill in https://github.com/kube-vip/kube-vip/pull/846
- bump golang for security fix by @thebsdbox in https://github.com/kube-vip/kube-vip/pull/884

### 0.8.2

- Manifest fix by @thebsdbox in https://github.com/kube-vip/kube-vip/pull/894

### 0.8.3

- fix: set vip_cidr default value by @M0NsTeRRR in https://github.com/kube-vip/kube-vip/pull/904
- fix: ipv6 host and port join by @M0NsTeRRR in https://github.com/kube-vip/kube-vip/pull/910

### 0.8.4

- Fixed lastKnownGoodEndpoint not being set when in non-leader-election… by @p-strusiewiczsurmacki-mobica in https://github.com/kube-vip/kube-vip/pull/955
- Added e2e tests for control-plane in routing table mode, fixed IPv6 issue by @p-strusiewiczsurmacki-mobica in https://github.com/kube-vip/kube-vip/pull/958

### 0.8.5

- Fixed NDP responder by @p-strusiewiczsurmacki-mobica in https://github.com/kube-vip/kube-vip/pull/973
- Fixed retry-watcher timeout issue by @p-strusiewiczsurmacki-mobica in https://github.com/kube-vip/kube-vip/pull/974
- Egress rules deletion fix by @p-strusiewiczsurmacki-mobica in https://github.com/kube-vip/kube-vip/pull/970

### 0.8.6

- Fixed null pointer exception when IPVS loadbalancer is used by @p-strusiewiczsurmacki-mobica in https://github.com/kube-vip/kube-vip/pull/987

### 0.8.8

- Fix linting issue by @thebsdbox in https://github.com/kube-vip/kube-vip/pull/1024
- Fixes an issue with watchers having an old reference by @thebsdbox in https://github.com/kube-vip/kube-vip/pull/1029

### 0.8.10

- Fixed ENV log level setting by @p-strusiewiczsurmacki-mobica in https://github.com/kube-vip/kube-vip/pull/1073
- Fixed logging level configuration with command line argument by @p-strusiewiczsurmacki-mobica in https://github.com/kube-vip/kube-vip/pull/1074
- Fixed network mask setting function by @p-strusiewiczsurmacki-mobica in https://github.com/kube-vip/kube-vip/pull/1072
- Fixed IPVS backend re-add by @p-strusiewiczsurmacki-mobica in https://github.com/kube-vip/kube-vip/pull/1091
- Fixed service update in BGP and ARP mode by @p-strusiewiczsurmacki-mobica in https://github.com/kube-vip/kube-vip/pull/1094
- Fixed service/endpoints discovery concurrent issue by @p-strusiewiczsurmacki-mobica in https://github.com/kube-vip/kube-vip/pull/1093
- Fixed route deletion issue when 2 services referenced same endpoint by @p-strusiewiczsurmacki-mobica in https://github.com/kube-vip/kube-vip/pull/1111
- Fixed IPVS deletion issues by @p-strusiewiczsurmacki-mobica in https://github.com/kube-vip/kube-vip/pull/1096


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **0.8.10**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `kube-vip/kube-vip`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/kube-vip.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].

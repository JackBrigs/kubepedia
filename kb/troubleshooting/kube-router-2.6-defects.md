---
id: TROUBLE-KUBE_ROUTER_2_6_DEFECTS
type: troubleshooting
title: "kube-router 2.6: defects fixed in the 2.6 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=2.6.0 <2.7.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kube-router 2.6 known issues
  - kube-router 2.6 fixed in
  - is this kube-router bug already fixed
tags:
  - troubleshooting
  - upgrade
  - kube-router
sources:
  - type: docs
    path: cloudnativelabs/kube-router release notes for the 2.6 line — bug-fix entries
    url: https://github.com/cloudnativelabs/kube-router/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kube-router 2.6: defects fixed in the 2.6 line

## Summary

**25 defects** the project fixed across **4 releases** of the 2.6 line, from 2.6.0 to
2.6.3. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 2.6.0

- [1895](https://github.com/cloudnativelabs/kube-router/issues/1895) - IPv6 NDP NA/NS dropped when using egress network policy
- [1875](https://github.com/cloudnativelabs/kube-router/issues/1875) - Collect service statistics real-time
- [1888](https://github.com/cloudnativelabs/kube-router/issues/1860) - Resilience to TCP SYN Node Loss
- [1816](https://github.com/cloudnativelabs/kube-router/issues/1816) - support change the default port of GoBGP
- [1614](https://github.com/cloudnativelabs/kube-router/issues/1614) - Fix CLI Options - --master doesn't work without --kubeconfig
- 94e72aa8 - fix(NPC): allow bi-directional ipv6 network discovery `<Aaron U'Ren>`
- 732d7a72 - fix(nsc): add loadbalancer IPs to metrics `<Aaron U'Ren>`
- c2fd6333 - fix(nsc): sync field name `<Richard Kojedzinszky>`
- b4a9ba70 - fix(nsc): rename network_services_metrics.go `<Richard Kojedzinszky>`
- 5e397e50 - fix failed message `<Anupam Ghosh>`
- 8504c52e - fix(DSR): setup source routing for all external IPs `<Aaron U'Ren>`
- e6edc853 - fix(ipAddrDel): check to see if IP exists on interface before delete `<Aaron U'Ren>`
- 94bfc0d9 - fix(ipAddrDel): check for routes before trying to delete `<Aaron U'Ren>`
- e29b6a32 - fix(NSC): pass fwmark to traffic director as an int `<Aaron U'Ren>`
- b070531e - fix: add proper nil rule src handling `<Aaron U'Ren>`
- 4795a07e - fix(ip rule): use NewRule() for all rule creations `<Aaron U'Ren>`
- 56076051 - fix(linux_networking.go): add scope to local routes `<Aaron U'Ren>`
- 80328ace - fix(linux_networking.go): filter routes to be deleted by table `<Aaron U'Ren>`
- 2836065f - fix(linux_routing.go): choose first rt_tables file `<Aaron U'Ren>`

### 2.6.1

- 92572c75ac5c4fbc0de9faf873e48f16748ab3ba fix(ipset): ignore non-kube-router ipsets

### 2.6.2

- 09239b0e - fix(ipset): don't strip inet6 prefixing of ipsets `<Aaron U'Ren>`
- 65f7f9b6 - fix(ipset): store kube-router-local-ips ipset `<Bukal, Tomáš>`

### 2.6.3

- b72910c8 - fix(service.go): rely on LabelServiceName only `<Aaron U'Ren>`
- 0155169e - fix(node.go): embed root cause errors in returned errors `<Aaron U'Ren>`
- acd0a94d - fix: do not advertise Pod IPv4 CIDR in a Cluster composed of IPv6-only Nodes) `<sunhuanran>`


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **2.6.3**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `cloudnativelabs/kube-router`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/kube-router.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].

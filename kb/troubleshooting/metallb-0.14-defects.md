---
id: TROUBLE-METALLB_0_14_DEFECTS
type: troubleshooting
title: "metallb 0.14: defects fixed in the 0.14 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.14.0 <0.15.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - metallb 0.14 known issues
  - metallb 0.14 fixed in
  - is this metallb bug already fixed
tags:
  - troubleshooting
  - upgrade
  - metallb
sources:
  - type: docs
    path: metallb/metallb release notes for the 0.14 line — bug-fix entries
    url: https://github.com/metallb/metallb/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# metallb 0.14: defects fixed in the 0.14 line

## Summary

**9 defects** the project fixed across **6 releases** of the 0.14 line, from 0.14.4 to
0.14.9. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.14.4

- Fix the non existing conversion webhook in the Helm CRDs ([PR 2269](https://github.com/metallb/metallb/pull/2269))
- Helm: fix the creation of the metrics-certs volume under the presence of the speakerMetricsTLSSecret value, regardless of FRR being enabled ([PR 2286](https://github.com/metallb/metallb/pull/2286))

### 0.14.5

- Fix the handling of readyness conditions of endpointslices: instead of looking at the serving condition first, we look at the ready condition. This allows metallb to respect the publishNotReadyAddresses field of the services. (#2337, @farodin91)

### 0.14.6

- Fix session flapping when adding / removing services and BFD is enabled. (#2454, @fedepaol)
- Fix(chart,prometheusrules): alert not matching labels for e.g. speakers (#2453, @sebastiangaiser)

### 0.14.7

- Fix the double immutable field validation in the ServiceL2Status CRD, which may make the validation of the CRD to fail. (#2461, @fedepaol)

### 0.14.8

- Fix the broken all-in-one/kustomize manifests from v0.14.7

### 0.14.9

- Fix default BGPPeer hold/keepalive timers being incompatible with FRRConfigurations. We now delegate the defaults to FRR itself instead of hard-coding them, supporting 0 timers as well. (#2537, @oribon)
- Fixed Community resources updates being denied without explanation. (#2608, @oribon)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **0.14.9**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `metallb/metallb`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/metallb.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].

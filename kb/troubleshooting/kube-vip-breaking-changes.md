---
id: TROUBLE-KUBE_VIP_BREAKING_CHANGES
type: troubleshooting
title: "kube-vip: declared breaking changes by release"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.9.0 <=0.9.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kube-vip breaking changes
  - kube-vip upgrade broke
  - kube-vip action required upgrade
tags:
  - upgrade
  - breaking-change
  - kube-vip
sources:
  - type: docs
    path: kube-vip/kube-vip release notes — "breaking changes" / "action required" entries
    url: https://github.com/kube-vip/kube-vip/releases
    note: "machine-extracted by scripts/upstream_issues.py, short and duplicate lines filtered out"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kube-vip: declared breaking changes by release

## Summary

**5 behaviour changes** the project itself marked as breaking or action-required, across
1 releases from 0.9.0 to 0.9.0. Read this before planning
an upgrade that crosses any of these versions: unlike defects, these are changes that work as
designed and still break a working configuration.

## Problem

An upgrade across a breaking change usually succeeds — the failure appears afterwards, in behaviour:
a setting silently ignored, a default flipped, an API version withdrawn.

## Context

### 0.9.0

- When you use the environment variable `vip_cidr` please rename it to `vip_subnet`
- **Drop** support of Equinix Metal Platform (Removed)
- CLI: `--metal`, ENV: `vip_packet`, YAML: `enableMetal`
- CLI: `--metalProject`, ENV: `vip_packetproject`
- CLI: `--metalProjectId`, ENV: `vip_packetprojectid`

## Diagnostics

Compare the version in use against the list above:

```bash
kubectl get nodes -o wide          # runtime versions, for node components
helm list -A                       # chart-deployed components
```

## Known Issues

Entries are verbatim from upstream release notes and filtered mechanically: lines shorter than 45
characters and duplicates were dropped, because section headings and list fragments come through the
extractor as if they were entries. If a release you care about looks empty here, read its notes
upstream before concluding nothing changed.

## References

- Upstream releases of `kube-vip/kube-vip`, read 2026-07-31 via `scripts/upstream_issues.py`;
  raw extraction in `reports/upstream/kube-vip.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].

---
id: TROUBLE-INGRESS_NGINX_BREAKING_CHANGES
type: troubleshooting
title: "ingress-nginx: declared breaking changes by release"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.10.0 <=1.10.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - ingress-nginx breaking changes
  - ingress-nginx upgrade broke
  - ingress-nginx action required upgrade
  - what breaks upgrading ingress-nginx
tags:
  - upgrade
  - breaking-change
  - ingress-nginx
sources:
  - type: docs
    path: kubernetes/ingress-nginx release notes — entries marked breaking / action required
    url: https://github.com/kubernetes/ingress-nginx/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# ingress-nginx: declared breaking changes by release

## Summary

**4 behaviour changes** the project itself marked as breaking or action-required, across
1 releases from 1.10.0 to 1.10.0. These are not defects: they work as designed and still break
a configuration that worked yesterday. An upgrade crossing any of them needs a decision, not just a
rollout.

## Problem

The upgrade itself usually succeeds. The damage shows up afterwards — a setting silently ignored, a
default flipped, an API version withdrawn, a variable that must now be set explicitly.

## Context

### 1.10.0

- This version does not support chroot image, this will be fixed on a future minor patch release
- This version dropped Opentracing and zipkin modules, just Opentelemetry is supported
- This version dropped support for PodSecurityPolicy
- This version dropped support for GeoIP (legacy). Only GeoIP2 is supported


## Diagnostics

```bash
# which version is actually deployed
kubectl get nodes -o wide
helm list -A
```

Cross the list above against the range you are moving through, not only the target version.

## Known Issues

Entries are verbatim from upstream release notes and filtered mechanically: lines shorter than
45 characters and duplicates are dropped, because section headings and list fragments reach the
extractor looking like entries. If a release you care about appears empty here, read its notes
upstream before concluding that nothing changed.

## References

- Upstream releases of `kubernetes/ingress-nginx`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/ingress-nginx.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].

---
id: TROUBLE-GCP_PD_CSI_BREAKING_CHANGES
type: troubleshooting
title: "gcp-pd-csi: declared breaking changes by release"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.5.1 <=0.7.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - gcp-pd-csi breaking changes
  - gcp-pd-csi upgrade broke
  - gcp-pd-csi action required upgrade
  - what breaks upgrading gcp-pd-csi
tags:
  - upgrade
  - breaking-change
  - gcp-pd-csi
sources:
  - type: docs
    path: kubernetes-sigs/gcp-compute-persistent-disk-csi-driver release notes — entries marked breaking / action required
    url: https://github.com/kubernetes-sigs/gcp-compute-persistent-disk-csi-driver/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# gcp-pd-csi: declared breaking changes by release

## Summary

**5 behaviour changes** the project itself marked as breaking or action-required, across
3 releases from 0.5.1 to 0.7.0. These are not defects: they work as designed and still break
a configuration that worked yesterday. An upgrade crossing any of them needs a decision, not just a
rollout.

## Problem

The upgrade itself usually succeeds. The damage shows up afterwards — a setting silently ignored, a
default flipped, an API version withdrawn, a variable that must now be set explicitly.

## Context

### 0.5.1

- BREAKING: The driver now enforces AccessMode validation for all calls, supported access modes are SINGLE_NODE_WRITER, SINGLE_NODE_READER_ONLY, MULTI_NODE_READER_ONLY

### 0.6.0

- Some of the API objects in the deployment specs have changed names/labels/namespaces, please tear down old driver before deploying this version to avoid orphaning old objects. You will also no longer see the driver in the `default` namespace
- Some error codes have been changed, please see below for details if you rely on specific error codes of the driver

### 0.7.0

- Adding `PodSecurityPoliciy` to allow `csi-gce-pd-node` in clusters with policies enabled
- BREAKING CHANGE: All deployment objects in setup-cluster.yaml have been renamed. When deleting the deployment using ./delete-driver.sh, make sure to use specs from your previous deployment version to ensure the correct objects are cleaned up. ([#405](https://github.com/kubernetes-sigs/gcp-compute-persistent-disk-csi-driver/pull/405), [@verult](https://github.com/verult))


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

- Upstream releases of `kubernetes-sigs/gcp-compute-persistent-disk-csi-driver`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/gcp-pd-csi.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].

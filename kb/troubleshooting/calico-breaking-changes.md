---
id: TROUBLE-CALICO_BREAKING_CHANGES
type: troubleshooting
title: "calico: declared breaking changes by release"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=3.28.0 <=3.32.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - calico breaking changes
  - calico upgrade broke
  - calico action required upgrade
  - what breaks upgrading calico
tags:
  - upgrade
  - breaking-change
  - calico
sources:
  - type: docs
    path: projectcalico/calico release notes — entries marked breaking / action required
    url: https://github.com/projectcalico/calico/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# calico: declared breaking changes by release

## Summary

**3 behaviour changes** the project itself marked as breaking or action-required, across
2 releases from 3.28.0 to 3.32.0. These are not defects: they work as designed and still break
a configuration that worked yesterday. An upgrade crossing any of them needs a decision, not just a
rollout.

## Problem

The upgrade itself usually succeeds. The damage shows up afterwards — a setting silently ignored, a
default flipped, an API version withdrawn, a variable that must now be set explicitly.

## Context

### 3.28.0

- **Breaking change:** On upgrade, the UID of projectcalico.org/v3 resources will change. If you are using the Calico API server, it is recommended that you restart any controllers that manage projectcalico.org/v3 API resources after upgrading Calico, including the kube-controller-manager. This change was necessary in order to fix an issue where duplicate UIDs could be seen on different API resources, confusing Kubernetes garbage collection. [calico #8586](https://github.com/projectcalico/calico/pull/8586) (@caseydavenport)

### 3.32.0

- The `tigera-operator` Helm chart no longer includes custom resource definitions for Calico. A new `crd.projectcalico.org.v1` companion Helm chart has been introduced which includes the CRDs instead. [calico 11727](https://github.com/projectcalico/calico/pull/11727) (@caseydavenport)
- BREAKING: The `tigera-operator` Helm chart no longer includes custom resource definitions for Calico. A new `crd.projectcalico.org.v1` companion Helm chart has been introduced which includes the CRDs instead. [calico 11727](https://github.com/projectcalico/calico/pull/11727) (@caseydavenport)


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

- Upstream releases of `projectcalico/calico`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/calico.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].

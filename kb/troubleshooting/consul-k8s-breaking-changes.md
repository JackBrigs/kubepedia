---
id: TROUBLE-CONSUL_K8S_BREAKING_CHANGES
type: troubleshooting
title: "consul-k8s: declared breaking changes by release"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.5.0 <=0.5.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - consul-k8s breaking changes
  - consul-k8s upgrade broke
  - consul-k8s action required upgrade
  - what breaks upgrading consul-k8s
tags:
  - upgrade
  - breaking-change
  - consul-k8s
sources:
  - type: docs
    path: hashicorp/consul-k8s release notes — entries marked breaking / action required
    url: https://github.com/hashicorp/consul-k8s/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# consul-k8s: declared breaking changes by release

## Summary

**4 behaviour changes** the project itself marked as breaking or action-required, across
1 releases from 0.5.0 to 0.5.0. These are not defects: they work as designed and still break
a configuration that worked yesterday. An upgrade crossing any of them needs a decision, not just a
rollout.

## Problem

The upgrade itself usually succeeds. The damage shows up afterwards — a setting silently ignored, a
default flipped, an API version withdrawn, a variable that must now be set explicitly.

## Context

### 0.5.0

- Breaking Changes Validation improvements Internal type cleanup
- The v1alpha1 API version was deprecated and removed. [#1197](https://github.com/kubernetes-sigs/gateway-api/pull/1197) [#906](https://github.com/kubernetes-sigs/gateway-api/issues/906)
- The `NamedAddress` value for `Gateway`'s `spec.addresses[].type` field has been deprecated, and support for domain-prefixed values (like `example.com/NamedAddress`) has been added instead to better represent the custom nature of this support. [#1178](https://github.com/kubernetes-sigs/gateway-api/pull/1178)
- Implementations are now expected to use `500` instead of `503` responses when the data-plane has no matching route. [#1151](https://github.com/kubernetes-sigs/gateway-api/pull/1151), [#1258](https://github.com/kubernetes-sigs/gateway-api/pull/1258)


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

- Upstream releases of `hashicorp/consul-k8s`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/consul-k8s.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].

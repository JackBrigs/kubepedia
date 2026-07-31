---
id: TROUBLE-CONSUL_K8S_0_9_DEFECTS
type: troubleshooting
title: "consul-k8s 0.9: defects fixed in the 0.9 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.9.0 <0.10.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - consul-k8s 0.9 known issues
  - consul-k8s 0.9 fixed in
  - is this consul-k8s bug already fixed
tags:
  - troubleshooting
  - upgrade
  - consul-k8s
sources:
  - type: docs
    path: hashicorp/consul-k8s release notes for the 0.9 line — bug-fix entries
    url: https://github.com/hashicorp/consul-k8s/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# consul-k8s 0.9: defects fixed in the 0.9 line

## Summary

**6 defects** the project fixed across **3 releases** of the 0.9 line, from 0.9.1 to
0.9.3. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.9.1

- Fix bootstrap acl issue when Consul was installed into a namespace other than `default` [[GH-106](https://github.com/hashicorp/consul-k8s/issues/106)]
- Fix sync bug where `ClusterIP` services had their `Service` port instead of their `Endpoint` port registered. If the `Service`'s `targetPort` was different then `port` then the wrong port would be registered [[GH-132](https://github.com/hashicorp/consul-k8s/issues/132)]

### 0.9.2

- Fix bug during connect-inject where the `-default-protocol` flag was being ignored [[GH-141](https://github.com/hashicorp/consul-k8s/pull/141)]
- Fix bug during connect-inject where service-tag annotations were being ignored [[GH-141](https://github.com/hashicorp/consul-k8s/pull/141)]
- Fix bug during `server-acl-init` where if any step errored then the command would exit and subsequent commands would fail. Now this command runs until completion, i.e. it retries failed steps indefinitely and is idempotent [[GH-138](https://github.com/hashicorp/consul-k8s/issues/138)]

### 0.9.3

- Fixes a bug where even if the ACL Tokens for the other components existed (e.g. client or sync-catalog) we'd try to generate new tokens and update the secrets. [[GH-152](https://github.com/hashicorp/consul-k8s/pull/152)]


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **0.9.3**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `hashicorp/consul-k8s`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/consul-k8s.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].

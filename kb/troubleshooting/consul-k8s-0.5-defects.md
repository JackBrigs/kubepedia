---
id: TROUBLE-CONSUL_K8S_0_5_DEFECTS
type: troubleshooting
title: "consul-k8s 0.5: defects fixed in the 0.5 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.5.0 <0.6.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - consul-k8s 0.5 known issues
  - consul-k8s 0.5 fixed in
  - is this consul-k8s bug already fixed
tags:
  - troubleshooting
  - upgrade
  - consul-k8s
sources:
  - type: docs
    path: hashicorp/consul-k8s release notes for the 0.5 line — bug-fix entries
    url: https://github.com/hashicorp/consul-k8s/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# consul-k8s 0.5: defects fixed in the 0.5 line

## Summary

**6 defects** the project fixed across **1 releases** of the 0.5 line, from 0.5.0 to
0.5.0. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.5.0

- Fix service registration naming when using Connect [[GH 36](https://github.com/hashicorp/consul-k8s/issues/36)]
- Fix catalog sync so that agents don't incorrectly deregister Kubernetes services [[GH 40](https://github.com/hashicorp/consul-k8s/issues/40)][[GH 59](https://github.com/hashicorp/consul-k8s/issues/59)]
- Fix performance issue for the k8s -> Consul catalog sync [[GH 60](https://github.com/hashicorp/consul-k8s/issues/60)]
- Fixes a problem that would cause webhook deployment to fail on Kubernetes v1.22 and greater. [#991](https://github.com/kubernetes-sigs/gateway-api/pull/991)
- Fixes a bug where the `Namespace` could be unspecified in `ReferencePolicy` [#964](https://github.com/kubernetes-sigs/gateway-api/pull/964)
- Fixes a bug where v1alpha2 GatewayClass controller names were not being shown in the output of `kubectl get gatewayclasses` [#909](https://github.com/kubernetes-sigs/gateway-api/pull/909)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **0.5.0**, the newest release recorded here for this line.

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

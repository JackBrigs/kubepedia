---
id: TROUBLE-CONSUL_K8S_0_4_DEFECTS
type: troubleshooting
title: "consul-k8s 0.4: defects fixed in the 0.4 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.4.0 <0.5.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - consul-k8s 0.4 known issues
  - consul-k8s 0.4 fixed in
  - is this consul-k8s bug already fixed
tags:
  - troubleshooting
  - upgrade
  - consul-k8s
sources:
  - type: docs
    path: hashicorp/consul-k8s release notes for the 0.4 line — bug-fix entries
    url: https://github.com/hashicorp/consul-k8s/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# consul-k8s 0.4: defects fixed in the 0.4 line

## Summary

**11 defects** the project fixed across **4 releases** of the 0.4 line, from 0.4.0 to
0.4.3. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.4.0

- [#777](https://github.com/kubernetes-sigs/gateway-api/pull/777) : Fix typo
- [#875](https://github.com/kubernetes-sigs/gateway-api/pull/875) : Fix HTTP path match documentation
- [#845](https://github.com/kubernetes-sigs/gateway-api/pull/845) : Fix markdown list formatting
- [#834](https://github.com/kubernetes-sigs/gateway-api/pull/834) : Fixes some broken links
- [#885](https://github.com/kubernetes-sigs/gateway-api/pull/885) : Fix incorrect urls
- [#748](https://github.com/kubernetes-sigs/gateway-api/pull/748) : fix kustomize to install v1a2 crds

### 0.4.1

- ControllerName now prints correctly in kubectl output for GatewayClass [#909](https://github.com/kubernetes-sigs/gateway-api/pull/909)
- Namespace can no longer be left unspecified in ReferencePolicy [#964](https://github.com/kubernetes-sigs/gateway-api/pull/964)
- Wildcard characters can no longer be used in redirect Hostname values [#956](https://github.com/kubernetes-sigs/gateway-api/pull/956)

### 0.4.2

- Update image generation process with more consistent naming [#1034](https://github.com/kubernetes-sigs/gateway-api/pull/1034)

### 0.4.3

- A fix to ensure that Path match validation actually works [#1071](https://github.com/kubernetes-sigs/gateway-api/pull/1071)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **0.4.3**, the newest release recorded here for this line.

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

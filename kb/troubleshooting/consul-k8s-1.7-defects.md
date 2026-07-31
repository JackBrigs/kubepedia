---
id: TROUBLE-CONSUL_K8S_1_7_DEFECTS
type: troubleshooting
title: "consul-k8s 1.7: defects fixed in the 1.7 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.7.0 <1.8.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - consul-k8s 1.7 known issues
  - consul-k8s 1.7 fixed in
  - is this consul-k8s bug already fixed
tags:
  - troubleshooting
  - upgrade
  - consul-k8s
sources:
  - type: docs
    path: hashicorp/consul-k8s release notes for the 1.7 line — bug-fix entries
    url: https://github.com/hashicorp/consul-k8s/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# consul-k8s 1.7: defects fixed in the 1.7 line

## Summary

**5 defects** the project fixed across **5 releases** of the 1.7 line, from 1.7.0 to
1.7.13. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.7.0

- Upgrade to Go 1.23.8 to fix CVE [GO-2025-3563](https://pkg.go.dev/vuln/GO-2025-3563)

### 1.7.1

- cni: CNI update strategy to be fixed to pod by pod rolling update and removed older CNI updateStrategy configuration

### 1.7.4

- control-plane: Fixed bug in TerminatingGateway controller workflow for handling AdminPartition enabled cluster ACL policies for associated TerminatingGateway services

### 1.7.8

- cni: fixed race conditions with older versions where no cleanup was done for binary

### 1.7.13

- api-gateway: Fix cross-namespace ACL resource collisions by keying policy/role/binding-rule caches with gatewayName + namespace. Managed resource names are now namespace-scoped to prevent one gateway from affecting another when deployed in different Kubernetes namespaces. [[GH-5140](https://github.com/hashicorp/consul-k8s/pull/5140)]


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.7.13**, the newest release recorded here for this line.

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

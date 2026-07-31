---
id: TROUBLE-CONSUL_K8S_1_6_DEFECTS
type: troubleshooting
title: "consul-k8s 1.6: defects fixed in the 1.6 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.6.0 <1.7.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - consul-k8s 1.6 known issues
  - consul-k8s 1.6 fixed in
  - is this consul-k8s bug already fixed
tags:
  - troubleshooting
  - upgrade
  - consul-k8s
sources:
  - type: docs
    path: hashicorp/consul-k8s release notes for the 1.6 line — bug-fix entries
    url: https://github.com/hashicorp/consul-k8s/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# consul-k8s 1.6: defects fixed in the 1.6 line

## Summary

**7 defects** the project fixed across **5 releases** of the 1.6 line, from 1.6.0 to
1.6.8. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.6.0

- helm: Fix ArgoCD hooks related annotations on server-acl-init Job, they must be added at Job definition and not template level. [[GH-3989](https://github.com/hashicorp/consul-k8s/issues/3989)]

### 1.6.1

- helm: fix issue where the API Gateway GatewayClassConfig tolerations can not be parsed by the Helm chart. [[GH-4315](https://github.com/hashicorp/consul-k8s/issues/4315)]

### 1.6.2

- cli: fix issue where the `consul-k8s proxy list` command does not include API gateways. [[GH-4426](https://github.com/hashicorp/consul-k8s/issues/4426)]
- connect-inject: fix issue where the ACL policy for the connect-injector included the `acl = "write"` rule twice when namespaces were not enabled. [[GH-4434](https://github.com/hashicorp/consul-k8s/issues/4434)]
- updated golang.org/x/net dependency to 0.34.0 to fix vulnerability [[GO-2024-3333](https://pkg.go.dev/vuln/GO-2024-3333)] in CLI, CNI, acceptance and control-plane submodule.[[PR-4452](https://github.com/hashicorp/consul-k8s/pull/4452)]

### 1.6.4

- Upgrade to Go 1.23.8 to fix CVE [GO-2025-3563](https://pkg.go.dev/vuln/GO-2025-3563)

### 1.6.8

- control-plane: Fixed bug in TerminatingGateway controller workflow for handling AdminPartition enabled cluster ACL policies for associated TerminatingGateway services


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.6.8**, the newest release recorded here for this line.

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

---
id: TROUBLE-CONSUL_K8S_1_8_DEFECTS
type: troubleshooting
title: "consul-k8s 1.8: defects fixed in the 1.8 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.8.0 <1.9.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - consul-k8s 1.8 known issues
  - consul-k8s 1.8 fixed in
  - is this consul-k8s bug already fixed
tags:
  - troubleshooting
  - upgrade
  - consul-k8s
sources:
  - type: docs
    path: hashicorp/consul-k8s release notes for the 1.8 line — bug-fix entries
    url: https://github.com/hashicorp/consul-k8s/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# consul-k8s 1.8: defects fixed in the 1.8 line

## Summary

**6 defects** the project fixed across **4 releases** of the 1.8 line, from 1.8.0 to
1.8.13. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.8.0

- updated golang.org/x/net dependency to 0.37.0 to fix vulnerability [[GO-2025-3503](https://pkg.go.dev/vuln/GO-2025-3503)] in CLI, CNI, acceptance and control-plane submodule. [[PR-4502](https://github.com/hashicorp/consul-k8s/pull/4502)] [[GH-4502](https://github.com/hashicorp/consul-k8s/issues/4502)]
- control-plane: Fixed bug in TerminatingGateway controller workflow for handling AdminPartition enabled cluster ACL policies for associated TerminatingGateway services. [[GH-4468](https://github.com/hashicorp/consul-k8s/issues/4468)]

### 1.8.6

- crypto: upgrade golang.org/x/crypto to v0.45.0 to fix GO-2025-4134, GO-2025-4135, GO-2025-4116, GHSA-f6x5-jh6r-wrfv
- cni: fixed race conditions with older versions where no cleanup was done for binary

### 1.8.11

- api-gateway: Fix cross-namespace ACL resource collisions by keying policy/role/binding-rule caches with gatewayName + namespace. Managed resource names are now namespace-scoped to prevent one gateway from affecting another when deployed in different Kubernetes namespaces. [[GH-5140](https://github.com/hashicorp/consul-k8s/pull/5140)]

### 1.8.13

- connect-init: fix incorrect FIPS Consul version check that caused misleading WARN messages in the `consul-connect-inject-init` init container logs even when a fully FIPS-compliant setup was used. The original check queried `/v1/agent/version` with a non-pointer map, so the response was never decoded and both FIPS warnings fired on every pod startup. The fix decodes the endpoint response correctly and checks the returned `FIPS` value. [[GH-5252](https://github.com/hashicorp/consul-k8s/issues/5252)]


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.8.13**, the newest release recorded here for this line.

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

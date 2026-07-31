---
id: TROUBLE-CONSUL_K8S_1_1_DEFECTS
type: troubleshooting
title: "consul-k8s 1.1: defects fixed in the 1.1 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.1.0 <1.2.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - consul-k8s 1.1 known issues
  - consul-k8s 1.1 fixed in
  - is this consul-k8s bug already fixed
tags:
  - troubleshooting
  - upgrade
  - consul-k8s
sources:
  - type: docs
    path: hashicorp/consul-k8s release notes for the 1.1 line — bug-fix entries
    url: https://github.com/hashicorp/consul-k8s/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# consul-k8s 1.1: defects fixed in the 1.1 line

## Summary

**19 defects** the project fixed across **9 releases** of the 1.1 line, from 1.1.1 to
1.1.16. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.1.1

- api-gateway: fix ACL issue where when adminPartitions and ACLs are enabled, API Gateway Controller is unable to create a new namespace in Consul [[GH-2029](https://github.com/hashicorp/consul-k8s/issues/2029)]
- api-gateway: fix issue where specifying an external server SNI name while using client nodes resulted in a TLS verification error. [[GH-2013](https://github.com/hashicorp/consul-k8s/issues/2013)]

### 1.1.2

- crd: fix bug on service intentions CRD causing some updates to be ignored. [[GH-2194](https://github.com/hashicorp/consul-k8s/issues/2083)]
- api-gateway: fix issue where the API Gateway controller is unable to start up successfully when Vault is configured as the secrets backend [[GH-2083](https://github.com/hashicorp/consul-k8s/issues/2083)]
- control-plane: fix issue with json tags of service defaults fields EnforcingConsecutive5xx, MaxEjectionPercent and BaseEjectionTime. [[GH-2160](https://github.com/hashicorp/consul-k8s/issues/2160)]
- control-plane: fix issue with multiport pods crashlooping due to dataplane port conflicts by ensuring dns redirection is disabled for non-tproxy pods [[GH-2176](https://github.com/hashicorp/consul-k8s/issues/2176)]
- sync-catalog: fix issue where the sync-catalog ACL token were set with an incorrect ENV VAR. [[GH-2068](https://github.com/hashicorp/consul-k8s/issues/2068)]

### 1.1.3

- control-plane: Fix casing of the Enforce Consecutive 5xx field on Service Defaults and acceptance test fixtures. [[GH-2266](https://github.com/hashicorp/consul-k8s/issues/2266)]

### 1.1.4

- control-plane: fix bug in endpoints controller when deregistering services from consul when a node is deleted. [[GH-2571](https://github.com/hashicorp/consul-k8s/issues/2571)]
- helm: fix CONSUL_LOGIN_DATACENTER for consul client-daemonset. [[GH-2652](https://github.com/hashicorp/consul-k8s/issues/2652)]
- helm: fix ui ingress manifest formatting, and exclude `ingressClass` when not defined. [[GH-2687](https://github.com/hashicorp/consul-k8s/issues/2687)]

### 1.1.6

- audit-log: fix parsing error for some audit log configuration fields fail with uncovertible string to integer errors. [[GH-2905](https://github.com/hashicorp/consul-k8s/issues/2905)]

### 1.1.8

- consul-telemetry-collector: fix deployments to non-default namespaces when global.enableConsulNamespaces [[GH-3215](https://github.com/hashicorp/consul-k8s/issues/3215)]
- consul-telemetry-collector: fix args to consul-dataplane when global.acls.manageSystemACLs [[GH-3184](https://github.com/hashicorp/consul-k8s/issues/3184)]
- control-plane: fixes an issue with the server-acl-init job where the job would fail on upgrades due to consul server ip address changes. [[GH-3137](https://github.com/hashicorp/consul-k8s/issues/3137)]

### 1.1.11

- control-plane: fix an issue where ACL token cleanup did not respect a pod's GracefulShutdownPeriodSeconds and
- control-plane: fix an issue where ACL tokens would prematurely be deleted and services would be deregistered if there

### 1.1.14

- cni: fix incorrect release version due to unstable submodule pinning [[GH-4091](https://github.com/hashicorp/consul-k8s/issues/4091)]

### 1.1.16

- sync-catalog: fix infinite retry loop when the catalog fails to connect to consul-server during the sync process [[GH-4266](https://github.com/hashicorp/consul-k8s/issues/4266)]


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.1.16**, the newest release recorded here for this line.

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

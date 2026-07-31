---
id: TROUBLE-CONSUL_K8S_1_3_DEFECTS
type: troubleshooting
title: "consul-k8s 1.3: defects fixed in the 1.3 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.3.0 <1.4.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - consul-k8s 1.3 known issues
  - consul-k8s 1.3 fixed in
  - is this consul-k8s bug already fixed
tags:
  - troubleshooting
  - upgrade
  - consul-k8s
sources:
  - type: docs
    path: hashicorp/consul-k8s release notes for the 1.3 line — bug-fix entries
    url: https://github.com/hashicorp/consul-k8s/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# consul-k8s 1.3: defects fixed in the 1.3 line

## Summary

**20 defects** the project fixed across **7 releases** of the 1.3 line, from 1.3.1 to
1.3.9. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.3.1

- consul-telemetry-collector: fix deployments to non-default namespaces when global.enableConsulNamespaces [[GH-3215](https://github.com/hashicorp/consul-k8s/issues/3215)]
- consul-telemetry-collector: fix args to consul-dataplane when global.acls.manageSystemACLs [[GH-3184](https://github.com/hashicorp/consul-k8s/issues/3184)]
- control-plane: Fixes a bug with the control-plane CLI validation where the consul-dataplane sidecar CPU request is compared against the memory limit instead of the CPU limit. [[GH-3209](https://github.com/hashicorp/consul-k8s/issues/3209)]
- control-plane: fixes an issue with the server-acl-init job where the job would fail on upgrades due to consul server ip address changes. [[GH-3137](https://github.com/hashicorp/consul-k8s/issues/3137)]

### 1.3.2

- api-gateway: fix issue where deleting an http-route in a non-default namespace would not remove the route from Consul. [[GH-3440](https://github.com/hashicorp/consul-k8s/issues/3440)]

### 1.3.3

- api-gateway: fix issue where external annotations and labels are being incorrectly deleted on services controlled by the API Gateway [[GH-3597](https://github.com/hashicorp/consul-k8s/issues/3597)]

### 1.3.4

- api-gateway: Fix order of initialization for creating ACL role/policy to avoid error logs in consul. [[GH-3779](https://github.com/hashicorp/consul-k8s/issues/3779)]
- control-plane: fix an issue where ACL token cleanup did not respect a pod's GracefulShutdownPeriodSeconds and
- control-plane: fix an issue where ACL tokens would prematurely be deleted and services would be deregistered if there

### 1.3.5

- api-gateway: Fix order of initialization for creating ACL role/policy to avoid error logs in consul when upgrading between versions. [[GH-3918](https://github.com/hashicorp/consul-k8s/issues/3918)]
- api-gateway: fix bug where multiple logical APIGateways would share the same ACL policy. [[GH-4001](https://github.com/hashicorp/consul-k8s/issues/4001)]
- control-plane: fix a panic when an upstream annotation is malformed. [[GH-3956](https://github.com/hashicorp/consul-k8s/issues/3956)]
- connect-inject: Fixed issue where on restart, if a managed-gateway-acl-role already existed the container would error [[GH-3978](https://github.com/hashicorp/consul-k8s/issues/3978)]

### 1.3.7

- api-gateway: fix issue where API Gateway specific acl roles/policy were not being cleaned up on deletion of an api-gateway [[GH-4060](https://github.com/hashicorp/consul-k8s/issues/4060)]
- cni: fix incorrect release version due to unstable submodule pinning [[GH-4091](https://github.com/hashicorp/consul-k8s/issues/4091)]
- endpoints-controller: graceful shutdown logic should not run on a new pod with the same name. Fixes a case where statefulset rollouts could get stuck in graceful shutdown when the new pods come up. [[GH-4059](https://github.com/hashicorp/consul-k8s/issues/4059)]

### 1.3.9

- Fixes install of Consul on GKE Autopilot where the option 'manageNonStandardCRDs' was not being used for the TCPRoute CRD. [[GH-4213](https://github.com/hashicorp/consul-k8s/issues/4213)]
- api-gateway: fix nil pointer deref bug when the section name in a gateway policy is not specified [[GH-4247](https://github.com/hashicorp/consul-k8s/issues/4247)]
- helm: Fix ArgoCD hooks related annotations on server-acl-init Job, they must be added at Job definition and not template level. [[GH-3989](https://github.com/hashicorp/consul-k8s/issues/3989)]
- sync-catalog: fix infinite retry loop when the catalog fails to connect to consul-server during the sync process [[GH-4266](https://github.com/hashicorp/consul-k8s/issues/4266)]


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.3.9**, the newest release recorded here for this line.

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

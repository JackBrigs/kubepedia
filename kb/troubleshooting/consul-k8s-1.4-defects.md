---
id: TROUBLE-CONSUL_K8S_1_4_DEFECTS
type: troubleshooting
title: "consul-k8s 1.4: defects fixed in the 1.4 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.4.0 <1.5.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - consul-k8s 1.4 known issues
  - consul-k8s 1.4 fixed in
  - is this consul-k8s bug already fixed
tags:
  - troubleshooting
  - upgrade
  - consul-k8s
sources:
  - type: docs
    path: hashicorp/consul-k8s release notes for the 1.4 line — bug-fix entries
    url: https://github.com/hashicorp/consul-k8s/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# consul-k8s 1.4: defects fixed in the 1.4 line

## Summary

**16 defects** the project fixed across **6 releases** of the 1.4 line, from 1.4.0 to
1.4.7. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.4.0

- consul-telemetry-collector: fix args to consul-dataplane when global.acls.manageSystemACLs [[GH-3184](https://github.com/hashicorp/consul-k8s/issues/3184)]

### 1.4.1

- api-gateway: Fix order of initialization for creating ACL role/policy to avoid error logs in consul. [[GH-3779](https://github.com/hashicorp/consul-k8s/issues/3779)]
- control-plane: fix an issue where ACL token cleanup did not respect a pod's GracefulShutdownPeriodSeconds and
- control-plane: fix an issue where ACL tokens would prematurely be deleted and services would be deregistered if there

### 1.4.2

- api-gateway: Fix order of initialization for creating ACL role/policy to avoid error logs in consul when upgrading between versions. [[GH-3918](https://github.com/hashicorp/consul-k8s/issues/3918)]
- api-gateway: fix bug where multiple logical APIGateways would share the same ACL policy. [[GH-4000](https://github.com/hashicorp/consul-k8s/issues/4000)]
- consul-cni: Fixed a bug where the output of `-version` did not include the version of the binary [[GH-3829](https://github.com/hashicorp/consul-k8s/issues/3829)]
- control-plane: fix a panic when an upstream annotation is malformed. [[GH-3956](https://github.com/hashicorp/consul-k8s/issues/3956)]
- connect-inject: Fixed issue where on restart, if a managed-gateway-acl-role already existed the container would error [[GH-3978](https://github.com/hashicorp/consul-k8s/issues/3978)]

### 1.4.4

- api-gateway: fix issue where API Gateway specific acl roles/policy were not being cleaned up on deletion of an api-gateway [[GH-4060](https://github.com/hashicorp/consul-k8s/issues/4060)]
- cni: fix incorrect release version due to unstable submodule pinning [[GH-4091](https://github.com/hashicorp/consul-k8s/issues/4091)]
- endpoints-controller: graceful shutdown logic should not run on a new pod with the same name. Fixes a case where statefulset rollouts could get stuck in graceful shutdown when the new pods come up. [[GH-4059](https://github.com/hashicorp/consul-k8s/issues/4059)]

### 1.4.6

- Fixes install of Consul on GKE Autopilot where the option 'manageNonStandardCRDs' was not being used for the TCPRoute CRD. [[GH-4213](https://github.com/hashicorp/consul-k8s/issues/4213)]
- api-gateway: fix nil pointer deref bug when the section name in a gateway policy is not specified [[GH-4247](https://github.com/hashicorp/consul-k8s/issues/4247)]
- sync-catalog: fix infinite retry loop when the catalog fails to connect to consul-server during the sync process [[GH-4266](https://github.com/hashicorp/consul-k8s/issues/4266)]

### 1.4.7

- helm: fix issue where the API Gateway GatewayClassConfig tolerations can not be parsed by the Helm chart. [[GH-4315](https://github.com/hashicorp/consul-k8s/issues/4315)]


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.4.7**, the newest release recorded here for this line.

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

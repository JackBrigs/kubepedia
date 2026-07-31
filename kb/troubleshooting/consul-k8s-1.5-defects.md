---
id: TROUBLE-CONSUL_K8S_1_5_DEFECTS
type: troubleshooting
title: "consul-k8s 1.5: defects fixed in the 1.5 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.5.0 <1.6.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - consul-k8s 1.5 known issues
  - consul-k8s 1.5 fixed in
  - is this consul-k8s bug already fixed
tags:
  - troubleshooting
  - upgrade
  - consul-k8s
sources:
  - type: docs
    path: hashicorp/consul-k8s release notes for the 1.5 line — bug-fix entries
    url: https://github.com/hashicorp/consul-k8s/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# consul-k8s 1.5: defects fixed in the 1.5 line

## Summary

**15 defects** the project fixed across **6 releases** of the 1.5 line, from 1.5.0 to
1.5.7. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.5.0

- api-gateway: fix bug where multiple logical APIGateways would share the same ACL policy. [[GH-4003](https://github.com/hashicorp/consul-k8s/issues/4003)]
- cni: fix incorrect release version due to unstable submodule pinning [[GH-4091](https://github.com/hashicorp/consul-k8s/issues/4091)]
- helm: bug fix for `prometheus.io` annotation omission while using datadog integration with openmetrics/prometheus and consul integration checks [[GH-3685](https://github.com/hashicorp/consul-k8s/issues/3685)]

### 1.5.1

- api-gateway: fix issue where API Gateway specific acl roles/policy were not being cleaned up on deletion of an api-gateway [[GH-4060](https://github.com/hashicorp/consul-k8s/issues/4060)]
- endpoints-controller: graceful shutdown logic should not run on a new pod with the same name. Fixes a case where statefulset rollouts could get stuck in graceful shutdown when the new pods come up. [[GH-4059](https://github.com/hashicorp/consul-k8s/issues/4059)]
- terminating-gateway: Fix generated acl policy for external services to include the namespace and partition block if they are enabled. [[GH-4153](https://github.com/hashicorp/consul-k8s/issues/4153)]

### 1.5.3

- Fixes install of Consul on GKE Autopilot where the option 'manageNonStandardCRDs' was not being used for the TCPRoute CRD. [[GH-4213](https://github.com/hashicorp/consul-k8s/issues/4213)]
- api-gateway: fix nil pointer deref bug when the section name in a gateway policy is not specified [[GH-4247](https://github.com/hashicorp/consul-k8s/issues/4247)]
- sync-catalog: fix infinite retry loop when the catalog fails to connect to consul-server during the sync process [[GH-4266](https://github.com/hashicorp/consul-k8s/issues/4266)]
- terminating-gateways: Fix bug where namespace field was not correctly set on ACL policies if using the `Registration` CRD with the service's namespace unset. [[GH-4224](https://github.com/hashicorp/consul-k8s/issues/4224)]

### 1.5.4

- helm: fix issue where the API Gateway GatewayClassConfig tolerations can not be parsed by the Helm chart. [[GH-4315](https://github.com/hashicorp/consul-k8s/issues/4315)]

### 1.5.5

- cli: fix issue where the `consul-k8s proxy list` command does not include API gateways. [[GH-4426](https://github.com/hashicorp/consul-k8s/issues/4426)]
- connect-inject: fix issue where the ACL policy for the connect-injector included the `acl = "write"` rule twice when namespaces were not enabled. [[GH-4434](https://github.com/hashicorp/consul-k8s/issues/4434)]
- updated golang.org/x/net dependency to 0.34.0 to fix vulnerability [[GO-2024-3333](https://pkg.go.dev/vuln/GO-2024-3333)] in CLI, CNI, acceptance and control-plane submodule.[[PR-4456](https://github.com/hashicorp/consul-k8s/pull/4456)]

### 1.5.7

- Upgrade to Go 1.23.8 to fix CVE [GO-2025-3563](https://pkg.go.dev/vuln/GO-2025-3563)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.5.7**, the newest release recorded here for this line.

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

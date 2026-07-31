---
id: TROUBLE-CONSUL_K8S_1_2_DEFECTS
type: troubleshooting
title: "consul-k8s 1.2: defects fixed in the 1.2 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.2.0 <1.3.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - consul-k8s 1.2 known issues
  - consul-k8s 1.2 fixed in
  - is this consul-k8s bug already fixed
tags:
  - troubleshooting
  - upgrade
  - consul-k8s
sources:
  - type: docs
    path: hashicorp/consul-k8s release notes for the 1.2 line — bug-fix entries
    url: https://github.com/hashicorp/consul-k8s/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# consul-k8s 1.2: defects fixed in the 1.2 line

## Summary

**25 defects** the project fixed across **9 releases** of the 1.2 line, from 1.2.0 to
1.2.8. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.2.0

- Fix Prometheus CVEs by bumping controller-runtime. [[GH-2183](https://github.com/hashicorp/consul-k8s/issues/2183)]
- control-plane: Fix casing of the Enforce Consecutive 5xx field on Service Defaults and acceptance test fixtures. [[GH-2266](https://github.com/hashicorp/consul-k8s/issues/2266)]
- control-plane: fix issue where consul-connect-injector acl token was unintentionally being deleted and not recreated when a container was restarted due to a livenessProbe failure. [[GH-1914](https://github.com/hashicorp/consul-k8s/issues/1914)]

### 1.2.1

- api-gateway: Fix creation of invalid Kubernetes Service when multiple Gateway listeners have the same port. [[GH-2413](https://github.com/hashicorp/consul-k8s/issues/2413)]
- api-gateway: fix helm install when setting copyAnnotations or nodeSelector [[GH-2597](https://github.com/hashicorp/consul-k8s/issues/2597)]
- api-gateway: fixes bug where envoy will silently reject RSA keys less than 2048 bits in length when not in FIPS mode, and will reject keys that are not 2048, 3072, or 4096 bits in length in FIPS mode. We now validate and reject invalid certs earlier. [[GH-2478](https://github.com/hashicorp/consul-k8s/issues/2478)]
- control-plane: fix bug in endpoints controller when deregistering services from consul when a node is deleted. [[GH-2571](https://github.com/hashicorp/consul-k8s/issues/2571)]
- helm: fix CONSUL_LOGIN_DATACENTER for consul client-daemonset. [[GH-2652](https://github.com/hashicorp/consul-k8s/issues/2652)]
- helm: fix ui ingress manifest formatting, and exclude `ingressClass` when not defined. [[GH-2687](https://github.com/hashicorp/consul-k8s/issues/2687)]
- transparent-proxy: Fix issue where connect-inject lacked sufficient `mesh:write` privileges in some deployments, which prevented virtual IPs from persisting properly. [[GH-2520](https://github.com/hashicorp/consul-k8s/issues/2520)]

### 1.2.2

- audit-log: fix parsing error for some audit log configuration fields fail with uncovertible string to integer errors. [[GH-2905](https://github.com/hashicorp/consul-k8s/issues/2905)]
- control-plane: Fix issue where ACL tokens would have an empty pod name that prevented proper token cleanup. [[GH-2808](https://github.com/hashicorp/consul-k8s/issues/2808)]

### 1.2.3

- api-gateway: fix issue where missing `NET_BIND_SERVICE` capability prevented api-gateway `Pod` from starting up when deployed to OpenShift [[GH-3070](https://github.com/hashicorp/consul-k8s/issues/3070)]
- crd: fix misspelling of preparedQuery field in ControlPlaneRequestLimit CRD [[GH-3001](https://github.com/hashicorp/consul-k8s/issues/3001)]

### 1.2.4

- consul-telemetry-collector: fix deployments to non-default namespaces when global.enableConsulNamespaces [[GH-3215](https://github.com/hashicorp/consul-k8s/issues/3215)]
- consul-telemetry-collector: fix args to consul-dataplane when global.acls.manageSystemACLs [[GH-3184](https://github.com/hashicorp/consul-k8s/issues/3215)]
- control-plane: fixes an issue with the server-acl-init job where the job would fail on upgrades due to consul server ip address changes. [[GH-3137](https://github.com/hashicorp/consul-k8s/issues/3137)]

### 1.2.5

- api-gateway: fix issue where deleting an http-route in a non-default namespace would not remove the route from Consul. [[GH-3440](https://github.com/hashicorp/consul-k8s/issues/3440)]

### 1.2.6

- api-gateway: fix issue where external annotations and labels are being incorrectly deleted on services controlled by the API Gateway [[GH-3597](https://github.com/hashicorp/consul-k8s/issues/3597)]

### 1.2.7

- api-gateway: Fix order of initialization for creating ACL role/policy to avoid error logs in consul. [[GH-3779](https://github.com/hashicorp/consul-k8s/issues/3779)]
- control-plane: fix an issue where ACL token cleanup did not respect a pod's GracefulShutdownPeriodSeconds and
- control-plane: fix an issue where ACL tokens would prematurely be deleted and services would be deregistered if there

### 1.2.8

- api-gateway: Fix order of initialization for creating ACL role/policy to avoid error logs in consul when upgrading between versions. [[GH-3918](https://github.com/hashicorp/consul-k8s/issues/3918)]
- api-gateway: fix bug where multiple logical APIGateways would share the same ACL policy. [[GH-4002](https://github.com/hashicorp/consul-k8s/issues/4002)]
- connect-inject: Fixed issue where on restart, if a managed-gateway-acl-role already existed the container would error [[GH-3978](https://github.com/hashicorp/consul-k8s/issues/3978)]


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.2.8**, the newest release recorded here for this line.

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

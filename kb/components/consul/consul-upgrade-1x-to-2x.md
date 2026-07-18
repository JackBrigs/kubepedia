---
id: TROUBLE-CONSUL_UPGRADE_1X_TO_2X
type: troubleshooting
title: "Consul-k8s 1.x → 2.x upgrade — lockstep versions, Gateway API bump, string-typed values"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: ">=1.22.7 <=2.0.2"
verified_at: "2026-07-18"
confidence: verified
aliases:
  - consul-k8s 2.0 upgrade
  - consul helm upgrade breaking
  - consul gateway api v1.5.1
  - consul values boolean string field
  - consul chart 2.0 breaking changes
tags:
  - consul
  - troubleshooting
  - upgrade
  - service-mesh
sources:
  - type: docs
    path: CHANGELOG.md
    url: https://github.com/hashicorp/consul-k8s/blob/v2.0.2/CHANGELOG.md
    note: "2.0.0 BREAKING: API Gateway -> gateway.networking.k8s.io v1.5.1; string-typed values regression; lockstep versioning NOTE"
  - type: code
    path: charts/consul/values.yaml
    url: https://github.com/hashicorp/consul-k8s/blob/v2.0.2/charts/consul/values.yaml
    note: "server.updatePartition gates rollout; disable_upgrade_migration true (rolling only)"
relations:
  - type: see_also
    target: CONCEPT-CONSUL_ON_K8S
  - type: see_also
    target: TROUBLE-CONSUL_ACL_BOOTSTRAP
---

# Consul-k8s 1.x → 2.x upgrade — lockstep versions, Gateway API bump, string-typed values

## Summary

consul-k8s **2.x is a rewrite** and the jump from 1.x is a hard, breaking upgrade — not a rolling bump.
Versions are **lockstep** (chart 2.0.x pins Consul 2.0.x + Dataplane 2.0.x; you can't mix a 1.x chart's
Consul with 2.x tooling), the **API Gateway** controller moved to `gateway.networking.k8s.io` **v1.5.1**
(Gateway API CRDs must move in lockstep), and **boolean-in-string-field** values that used to render now
**hard-fail**. Plan it as a version migration, not a patch.

## Problem

- `helm upgrade` to 2.x fails to render: type errors on strictly-typed string fields that hold booleans
  (previously accepted).
- After upgrade, **API Gateway** resources stop reconciling (Gateway API CRD version mismatch).
- `kubectl`/Argo CD hit CRD short-name ambiguity between Consul and Gateway-API HTTPRoute CRDs.

## Context

- Applies to the consul-k8s **1.9.x → 2.0.x** transition ([[CONCEPT-CONSUL_ON_K8S]]).
- **Lockstep versioning:** chart 2.0.2 = Consul 2.0.2 + consul-dataplane 2.0.2 (CHANGELOG@v2.0.2, 2.0.0
  NOTE). 1.9.10 = Consul 1.22.7. The chart↔Consul↔K8s compatibility matrix is HashiCorp-hosted docs
  (external, authoritative).
- **2.0.0 BREAKING — API Gateway:** the stable controller moved to `gateway.networking.k8s.io`
  **v1.5.1** (CHANGELOG@v2.0.2, GH-5181) — the Gateway API CRDs must be upgraded in lockstep or gateway
  reconciliation breaks.
- **String-typing regression fixed by tightening:** 2.0.0 fixed install/upgrade failures "caused by
  supplying boolean types to strictly typed string fields in custom helm values.yaml" (GH-5327) — your
  existing `values.yaml` may now hard-fail.
- **CRD naming collisions:** new CRDs under `consul.hashicorp.com` (shortnames like `chttproutes`)
  collide with Gateway-API `HTTPRoute` shortnames → `kubectl`/Argo CD ambiguity (several fixes,
  GH-5328/5458/5491).
- **Rolling only:** `disable_upgrade_migration: true` → rolling (not blue/green) upgrades; gate the
  server StatefulSet rollout with `server.updatePartition`. `server-acl-init` re-runs and **overwrites
  managed ACL policies** ([[TROUBLE-CONSUL_ACL_BOOTSTRAP]]).
- **RateLimit CRD gotcha:** in admin-partitions + ACL setups you must set `globalConfigACLToken`
  secretName/secretKey (operator token) or reconciliation fails even though `kubectl apply` succeeds.

## Diagnostics

- `helm template ... | ...` locally first — catch the string-field type errors before applying.
- Check installed Gateway API CRD version vs **v1.5.1** (`kubectl get crd gateways.gateway.networking.k8s.io -o jsonpath='{.spec.versions[*].name}'`).
- `kubectl api-resources | grep -Ei 'httproute|consul'` — spot the short-name collisions.

## Known Issues

- **Fix (values):** audit your custom `values.yaml` for booleans in string-typed fields (quote them)
  before upgrading; validate with `helm template`.
- **Fix (Gateway API):** upgrade the Gateway API CRDs to **v1.5.1** in lockstep with the chart.
- **Fix (ordering):** treat 1.x → 2.x as a planned migration — read HashiCorp's version-specific
  upgrade guide, gate the server rollout with `updatePartition`, and re-verify ACLs after (policies are
  reapplied on upgrade).
- **Do it in a window:** the mesh data path (Dataplane/Envoy) and API Gateway both change; expect
  disruption, not a seamless rolling patch.

## References

- consul-k8s `CHANGELOG.md`@v2.0.2 (2.0.0 BREAKING, GH-5181/5327/5328) + `values.yaml`@v2.0.2. Overview
  [[CONCEPT-CONSUL_ON_K8S]]; ACL overwrite on upgrade [[TROUBLE-CONSUL_ACL_BOOTSTRAP]].

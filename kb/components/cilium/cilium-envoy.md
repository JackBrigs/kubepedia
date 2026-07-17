---
id: CONCEPT-CILIUM_ENVOY
type: concept
title: "cilium-envoy — the Envoy L7 datapath inside Cilium (version matrix)"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: ">=1.15.9 <=1.19.3"
verified_at: "2026-07-17"
confidence: confirmed
aliases:
  - cilium-envoy
  - cilium envoy version
  - envoy in cilium
  - cilium l7 proxy
  - envoy.enabled daemonset
  - cilium envoy version mismatch
tags:
  - cilium
  - envoy
  - l7
  - servicemesh
sources:
  - type: code
    path: install/kubernetes/cilium/values.yaml
    url: https://github.com/cilium/cilium/blob/v1.19.3/install/kubernetes/cilium/values.yaml
    note: "envoy.image.tag (Envoy base version), envoy.enabled default, l7Proxy — read at tags v1.15.9/1.17.3/1.18.2/1.18.6/1.19.3"
  - type: code
    path: pkg/envoy/versioncheck.go
    url: https://github.com/cilium/cilium/blob/v1.19.3/pkg/envoy/
    note: "cilium-agent hard-checks the required cilium-envoy build SHA; mismatch blocks agent start"
  - type: docs
    path: Documentation/security/network/proxy/envoy.rst
    url: https://github.com/cilium/cilium/blob/v1.19.3/Documentation/security/network/proxy/envoy.rst
    note: "Envoy is Cilium's minimal custom distribution; DaemonSet vs embedded rationale"
relations:
  - type: part_of
    target: COMPONENT-CILIUM
  - type: see_also
    target: UPGRADE-CILIUM_1_15_TO_1_19
  - type: see_also
    target: CONCEPT-CILIUM_HUBBLE
  - type: see_also
    target: CONCEPT-CILIUM_LOADBALANCING
---

# cilium-envoy — the Envoy L7 datapath inside Cilium (version matrix)

## Summary

Cilium's L7 features — HTTP/gRPC network policy, the Cilium **Ingress** controller, **Gateway API**,
Envoy-based service mesh (traffic shifting, circuit breaking), and Hubble L7 visibility — are all
powered by an embedded, purpose-built Envoy called **cilium-envoy** (Cilium's minimal custom Envoy
distribution, not stock Envoy). Kubespray ships whatever cilium-envoy version its pinned Cilium
version bundles; you do **not** install or version Envoy separately. This doc pins the Envoy base
version per Cilium release and the one operational gotcha that bites on upgrade.

## Context

**Envoy base version per Cilium version** (from `envoy.image.tag` in `values.yaml`; the tag prefix
`vX.Y.Z` is the upstream Envoy release line):

| Kubespray | Cilium | cilium-envoy → Envoy base | source |
|-----------|--------|---------------------------|--------|
| v2.27.0 | 1.15.9 | `v1.29.9-…` → **Envoy 1.29** | `values.yaml`@v1.15.9 |
| v2.28.0 | 1.17.3 | `v1.32.5-…` → **Envoy 1.32** | `values.yaml`@v1.17.3 |
| v2.29.0 | 1.18.2 | `v1.34.7-…` → **Envoy 1.34** | `values.yaml`@v1.18.2 |
| v2.30.0 | 1.18.6 | `v1.35.9-…` → **Envoy 1.35** | `values.yaml`@v1.18.6 |
| v2.31.0 | 1.19.3 | `v1.36.6-…` → **Envoy 1.36** | `values.yaml`@v1.19.3 |

Envoy jumps **1.29 → 1.36** across the Kubespray range — each bump inherits upstream Envoy security
fixes; audit against Envoy 1.29–1.36 advisories.

**Deployment mode — the notable default flip.** `envoy.enabled` controls whether cilium-envoy runs as
a **standalone DaemonSet** (`cilium-envoy` pod per node) or **embedded** inside the cilium-agent pod:

- **Cilium 1.15.9** (`values.yaml`@v1.15.9): `envoy.enabled: false` → Envoy runs **embedded** in the
  agent by default; DaemonSet is opt-in.
- **Cilium 1.17.3+** (`values.yaml`@v1.17.3/1.18.x/1.19.3): `envoy.enabled: ~` with schema default
  "`true` for new installation" → **standalone DaemonSet is the default** for fresh installs (it
  decouples L7 traffic from the agent pod lifecycle). The flip lands in the **1.16 line** (bracketed
  by the two tags).
- **Upgrade impact:** a fresh install on v2.28.0+ schedules an extra DaemonSet (one pod/node);
  upgraders who want to keep Envoy embedded must set `envoy.enabled=false` explicitly
  ([[UPGRADE-CILIUM_1_15_TO_1_19]]).

**The version-mismatch footgun.** cilium-agent **hard-checks** the exact required cilium-envoy build
SHA (`pkg/envoy/versioncheck.go`) and **refuses to start** on mismatch. If an upgrade updates the
agent image but a cached/pinned `cilium-envoy` DaemonSet image lags, the agent won't come up — ensure
both images move together. Envoy is pinned by tag **and** `@sha256` digest in `values.yaml`.

**Master switch.** `l7Proxy: true` is the default in **all** pinned versions — the top-level enable
for the L7/Envoy datapath. Gateway API additionally requires `kubeProxyReplacement=true` and
`l7Proxy=true` (`gateway-api/installation.rst`).

**Envoy-powered features & maturity** (all shipped/enabled across the range unless noted):

- **L7 HTTP/gRPC policy** — GA all versions.
- **Cilium Ingress** (Envoy dataplane) — GA all versions.
- **Gateway API** — supported spec version rises: **v1.0.0** (1.15.9) → **v1.2.0** (1.17.3–1.18.6) →
  **v1.4.1** (1.19.3); GRPCRoute becomes Core from 1.17.3; GAMMA (mesh) from 1.17.3; TLSRoute stays
  experimental. (`Documentation/network/servicemesh/gateway-api/`)
- **Envoy service mesh** (CiliumEnvoyConfig: traffic mgmt/shifting, circuit breaking, load balancing)
  — present all versions.
- **Hubble L7 visibility** — Envoy streams access logs to Hubble ([[CONCEPT-CILIUM_HUBBLE]]).
- **Kafka L7** — historically Cilium's native Go proxylib, **not** Envoy (unverified that any pinned
  tag moved it to Envoy).

## References

- Cilium `install/kubernetes/cilium/values.yaml` (envoy.* keys, image tags) and
  `Documentation/security/network/proxy/envoy.rst`, `Documentation/network/servicemesh/gateway-api/`
  read at tags v1.15.9/v1.17.3/v1.18.2/v1.18.6/v1.19.3. Component [[COMPONENT-CILIUM]]; upgrade
  breaking changes [[UPGRADE-CILIUM_1_15_TO_1_19]]; Hubble [[CONCEPT-CILIUM_HUBBLE]].

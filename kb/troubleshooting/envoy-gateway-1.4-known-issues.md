---
id: TROUBLE-ENVOY_GATEWAY_1_4_KNOWN_ISSUES
type: troubleshooting
title: "Envoy Gateway 1.4: every defect fixed in the 1.4 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.4.0 <1.5.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - envoy gateway 1.4 known issues
  - envoy gateway 1.4 bugs
  - envoy gateway 1.4 fixed in
tags:
  - troubleshooting
  - envoy
  - gateway-api
  - upgrade
sources:
  - type: code
    path: envoyproxy/gateway release-notes/v1.4.*.yaml — "bug fixes" sections
    url: https://github.com/envoyproxy/gateway/tree/main/release-notes
    note: "7 releases on this line, 53 declared fixes"
relations:
  - type: see_also
    target: TROUBLE-ENVOY_GATEWAY_KNOWN_CVES
  - type: see_also
    target: TROUBLE-ENVOY_GATEWAY_BREAKING_CHANGES
  - type: see_also
    target: CONCEPT-ADDON_ENVOY_GATEWAY
---

# Envoy Gateway 1.4: every defect fixed in the 1.4 line

## Summary

The **1.4** maintenance line published **7 releases** carrying **53 defect fixes**,
5 breaking changes and 4 security updates (CVE-2025-58058).
Running anything below **1.4.6** on this line means carrying the remainder of the list
below.

Use this page the way a defect database is used: before filing "Envoy Gateway does X wrong", search
here — the odds are it is already named, with the exact patch that fixes it.

## Problem

Defects are grouped by the release that fixed them; a cluster on version *N* carries everything
listed under versions greater than *N*.

## Context

### v1.4.0 — 20

- Fixed traffic splitting when filters are attached to the `backendRef`.
- Added support for `Secret` and `ConfigMap` parsing in standalone mode.
- Bypassed overload manager for stats and ready listeners.
- Fixed translation of `backendSettings` for external authorization.
- Fixed an issue where the stats compressor was not working.
- Added support for `BackendTLSPolicy` and `EnvoyExtensionPolicy` parsing in standalone mode.
- Re-triggered reconciliation when a `backendRef` of type `ServiceImport` is updated or when `EndpointSlice` resources for a `ServiceImport` are updated.
- Fixed missing error logs and returns in the Kubernetes Reconcile method when a `GatewayClass` is not accepted.
- Allowed empty text field for OpenTelemetry sink when using JSON format.
- Fixed the `SamplingFraction` implementation within the Tracing API.
- Fixed Kubernetes resources not being deleted when a custom name was used.
- Prevented essential resources like `Namespace` from being treated as missing when loading from file.
- Avoided setting retriable status codes to 503 when `RetryOn` is configured in `BackendTrafficPolicy`.
- Fixed reconciliation logic to continue processing all `GatewayClasses` even after an error with one.
- Fixed an issue where a `ReferenceGrant` from a `SecurityPolicy` to a referenced `remoteJWKS` backend was not respected.
- Added additional newline validation for header values.
- Added validation to prevent duplicated API keys in API Key Auth.
- Fixed `HTTPRoute` precedence by correctly considering header and query match types.
- Ensured the TLS inspector filter is only added to TCP listeners (not UDP/QUIC) when HTTP/3 is enabled via `ClientTrafficPolicy`.
- Fix reconciling mirror backendRef endpoints once they've changed.

### v1.4.1 — 8

- Fixed OverlappingTLSConfig condition for merged Gateways.
- Fixed an issue with shared rules in the rate limit translator when `clientSelector` is not specified.
- Fixed an issue with handling integer values in zone annotations.
- Fixed an issue where routes without WASM in their EnvoyExtensionPolicies returned HTTP 500 responses when WASM cache initialization failed.
- Fixed an issue where UDP listeners were not created in the Envoy proxy’s xDS configuration.
- Fixed broken rate limit merging for `BackendTrafficPolicy` when the Gateway target defines rate limiting but the Route target does not.
- Fixed an issue that preserves ALPN configuration for listeners with overlapping certificates when ALPN is explicitly set in `ClientTrafficPolicy`.
- Replaced static UID with a dynamic UID for the global rate limit Grafana dashboard.

### v1.4.2 — 10

- Fixed issue where EnvoyExtensionPolicy ExtProc body processing mode was set to FullDuplexStreamed, but trailers were not sent.
- Fixed validation issue where EnvoyExtensionPolicy ExtProc with failOpen set to true did not reject the FullDuplexStreamed body processing mode.
- Fixed issue where EnvoyPatchPolicy could not replace the telemetry cluster.
- Added validation for section names in Gateway listeners.
- Added ConfigMap indexers for EnvoyExtensionPolicies to reconcile Lua changes.
- Fixed issue where the default access log format was not working.
- Fixed bug where backendRequestTimeout was incorrectly set when retries were enabled.
- Fixed certificate SANs overlap detection in listeners.
- Fixed issue where telemetry did not work when using host port.
- Fixed bug where BackendTLSPolicy incorrectly referenced ConfigMaps or Secrets across namespaces.

### v1.4.3 — 5

- Fixed issue where HTTPRoutes with sessionPersistence caused the Envoy listeners to drain.
- Fixed issue where EnvoyPatchPolicy CEL Validations around FullDuplexStreamed and FailOpen.
- Fixed issue where http filter was not being added for HTTP3 listeners.
- Fixed issue where http filters unstable order caused the Envoy listeners to drain.
- Fixed issue where missing secret in EnvoyProxy caused deployment not to be created.

### v1.4.4 — 5

- Fixed an issue in handling context-related transient errors to prevent incorrect state reconciliation and unintended behavior.
- Fixed an issue where the `exclusiveMaximum` field in the CRD was set incorrectly.
- Fixed validation for gRPC routes with extension ref filters.
- Fixed an issue where route status had dangling conditions and was not cleaned up.
- Added missing patch annotations to the `Compression` struct for proper `Merge`.

### v1.4.5 — 4

- Added a check to ensure that per proxy xds snapshot cache references are cleaned up when the connection is closed.
- Fixed an issue where use GRPCRoute with RequestMirror cause panic.
- Fixed an issue where certificate SAN overlap detection in gateway listeners.
- Disabled the default emission of `x-envoy-ratelimited` headers from the rate limit filter and re-enable with the `enableEnvoyHeaders` setting in ClientTrafficPolicy.

### v1.4.6 — 1

- Fixed 500 errors caused by partially invalid BackendRefs; traffic is now correctly routed between valid backends and 500 responses according to their configured weights.

## Diagnostics

```bash
kubectl -n <eg-ns> get deploy envoy-gateway \
  -o jsonpath='{.spec.template.spec.containers[0].image}{"\n"}'
```

Compare against **1.4.6** — the newest release of this line.

## Known Issues

Upgrading inside a maintenance line is the low-risk move, but this project ships behaviour changes
in patch releases as well; the full list is in [[TROUBLE-ENVOY_GATEWAY_BREAKING_CHANGES]] and the
security exposure in [[TROUBLE-ENVOY_GATEWAY_KNOWN_CVES]].

## References

- Upstream `release-notes/v1.4.*.yaml`, `bug fixes` sections, read at `origin/main` on 2026-07-31.
- Add-on: [[CONCEPT-ADDON_ENVOY_GATEWAY]].

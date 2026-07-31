---
id: TROUBLE-ENVOY_GATEWAY_1_6_KNOWN_ISSUES
type: troubleshooting
title: "Envoy Gateway 1.6.0: every defect fixed in 1.6.1–1.6.7"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.6.0 <1.7.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - envoy gateway known issues
  - envoy gateway 1.6 bugs
  - envoy gateway stale configuration after reconnection
  - envoy gateway ready before cache synced
  - grpcroute mirror service not found
  - envoy gateway 500 invalid backendrefs
tags:
  - troubleshooting
  - envoy
  - gateway-api
  - upgrade
sources:
  - type: code
    path: envoyproxy/gateway release-notes/v1.6.1.yaml … v1.6.7.yaml
    url: https://github.com/envoyproxy/gateway/tree/main/release-notes
    note: "upstream structured release notes: breaking changes / security updates / bug fixes per patch"
relations:
  - type: see_also
    target: TROUBLE-ENVOY_GATEWAY_KNOWN_CVES
  - type: see_also
    target: TROUBLE-ENVOY_GATEWAY_LEADER_LOSS_503
  - type: see_also
    target: CONCEPT-ADDON_ENVOY_GATEWAY
---

# Envoy Gateway 1.6.0: every defect fixed in 1.6.1–1.6.7

## Summary

Running **1.6.0** means carrying **49 known defects** (and 1.6.0 itself shipped 25 fixes for the 1.5 line) and missing **7 CVE fixes**; three
**breaking changes** landed inside the same patch line. All of it is closed by **1.6.7** without
leaving the 1.6 minor. This document is the full list, so that "is our problem already fixed
upstream?" is answered by reading rather than by reproducing.

Six entries deserve attention before the rest — they produce symptoms that look like network or
application faults and are routinely misdiagnosed as such:

| Fixed in | Defect | Why it misleads |
|---|---|---|
| 1.6.1 | xDS snapshot cache not cleared when streams close — **proxies keep serving stale configuration after reconnection** | looks like "routes did not update"; survives a controller restart |
| 1.6.4 | **the controller reported ready before its cache had synced** | it starts programming proxies from an incomplete view — the mechanism behind [[TROUBLE-ENVOY_GATEWAY_LEADER_LOSS_503]] |
| 1.6.3 | discovery errors on optional CRDs made the controller **reconcile incomplete resources** | same class: config built from a partial picture |
| 1.6.6 | GRPCRoute `RequestMirror` backend not indexed → **"service not found" for a mirror target that exists** | the error names a Service that is right there in the cluster |
| 1.6.1 / 1.6.6 | **500 errors from partially invalid BackendRefs** | one bad backend poisoned the whole route instead of being weighted out |
| 1.6.7 | **control-plane panic** from concurrent Status mutation racing the watchable map | shows up as an unexplained controller restart |

## Problem

Full list by patch, verbatim in substance from the upstream notes.

## Context

### 1.6.1 — 7 fixes

- xDS snapshot cache now cleared when streams close (no stale config after proxy reconnection)
- configured OIDC authorization endpoint no longer overridden by the issuer's discovered endpoints
- gateway ownership tracking when running multiple controllers
- default namespace handling when namespace is unset
- HTTPRoutes referencing gateways with multiple GatewayClasses had incomplete status conditions
- gateway status now treats "too many addresses" as programmed
- 500 errors from partially invalid BackendRefs — traffic now split by weight between valid backends

### 1.6.2 — 5 fixes

- `BackendTrafficPolicy` did not validate the maximum `requestBuffer` limit
- `observedGeneration` missing from `EnvoyPatchPolicy` status
- nil-pointer when applying `BackendTrafficPolicy` to HTTPRoutes with no `backendRefs`
- `ExternalTrafficPolicy` not applied to the Envoy Service when the service type is NodePort
- CRL reference not processed by the controller

### 1.6.3 — 8 fixes

- unrecoverable discovery errors on optional CRDs made the pod reconcile incomplete resources
- ExtProc discarded when `failOpen` is enabled for Wasm
- **sensitive data exposed in the control-plane config dump**
- upstream-protocol auto-detection broken with mixed HTTP + HTTPS backends
- race in server run causing goroutine leaks during config reloading
- default namespace for TLS secret object references now set to the owner namespace
- wrong cluster type used with mixed FQDN and Service backend refs
- routes with match-all rules were incorrectly merged with specific match rules

### 1.6.4 — 9 fixes, 1 breaking change

**Breaking:** the Gateway API CRD set was updated (upstream `gateway-api` issue #4490) — apply the
CRDs as part of the upgrade.

- shutdown manager ignored ready/stats listener metrics in its connection count (twice: counting and
  timely shutdown)
- `BackendTLSPolicy` `ResolvedRefs` status reason not aligned with the Gateway API spec
- custom response filters misplaced in the filter chain, breaking redirects in OAuth2 flows
- route-level idle timeout prevented configuring a listener-level idle timeout
- the message package ignored the configured logging level
- TCPRoute with mTLS broken by incorrect automatic HTTP protocol detection on TCP clusters
- an invalid `EnvoyPatchPolicy` stopped processing of the remaining xDS resources
- **the controller reported ready before the cache had synced**

### 1.6.5 — 6 fixes

- local object reference resolution from a parent policy in merged `BackendTrafficPolicies`
- route and policy status aggregation across multiple GatewayClasses managed by one controller —
  status is no longer overwritten by the last GatewayClass processed
- unmanaged route parents excluded from policy status ancestors
- `computeHosts` broken when both listener and route are wildcards
- ownership references added to the rate-limit ConfigMap and HPA
- `ConnectionLimit.Value` made optional, so `MaxConnectionDuration` / `MaxRequestsPerConnection` /
  `MaxStreamDuration` can be set without it

### 1.6.6 — 10 fixes, 2 breaking changes

**Breaking:** HTTPRoute and GRPCRoute with invalid filters now return **500 direct responses**;
HTTPRoute `Accepted` becomes False when `RequestMirror` is combined with `DirectResponse` or
`RequestRedirect`. Routes that silently half-worked before will now fail loudly — review filters
before upgrading.

- propagation of HTTPFilter translation errors to the outer layer
- 500 errors from partially invalid BackendRefs (weighted routing, as in 1.6.1)
- `SecurityPolicy` BasicAuth now rejects invalid `{SHA}` htpasswd entries
- GRPCRoute did not detect conflicting `RequestMirror` + `DirectResponse` — the mirror was silently
  dropped
- BasicAuth failed with CRLF line endings in htpasswd secrets
- **GRPCRoute `RequestMirror` backend not indexed → "service not found" for existing mirror targets**
- route status condition when a mirror filter's backend has no endpoints
- gateway-helm RBAC in GatewayNamespace mode with an explicit `watch.namespaces` list
- false metric increments on no-op delete and HPA reconcile paths
- missing failure-path metric recording for delete and HPA reconcile

### 1.6.7 — 4 fixes

- **control-plane panic caused by concurrent Status mutation racing the watchable map coalesce
  goroutine**
- status conditions not updated when a route is rejected for multiple reasons
- unresolved/unsupported HTTPRoute filters reported `BackendNotFound` instead of `UnsupportedValue`
- benchmark report emitted `0` for p99/p999

### v1.6.0 itself — 25 fixes shipped *in* 1.6.0

These closed defects of the 1.5 line; they are listed for completeness, so that the 1.6 line
is fully covered by this page.

- Fixed %ROUTE_KIND% operator to be properly lower-cased when used by clusterStatName in EnvoyProxy API, ensuring consistent metric naming conventions.
- Fixed maxAcceptPerSocketEvent configuration being ignored in ClientTrafficPolicy, now correctly applying the configured value to limit connections accepted per socket event.
- Fixed an issue where topologyInjectorDisabled was enabled but the local cluster was not defined, causing configuration inconsistencies.
- Fixed log formatting of improper key-value pairs to prevent DPANIC errors in controller-runtime logger, improving stability and log readability.
- Fixed handling of context-related transient errors to prevent incorrect state reconciliation and unintended behavior during API server communication interruptions.
- Fixed an issue where the controller could not read EnvoyProxy resources that are attached only to GatewayClass, improving resource discovery and reconciliation.
- Fixed adding metadata for proxyService and OIDC xDS clusters, ensuring proper metadata propagation for service discovery and authentication.
- Fixed handling of millisecond-level retry durations and token TTLs in OIDC authentication, ensuring precise time-based configuration values are correctly processed.
- Fixed indexer and controller crashing when BackendTrafficPolicy has a redirect response override, improving stability during policy configuration updates.
- Fixed Lua validator log level to be suppressed by default, reducing log noise and improving performance during Lua script validation.
- Fixed ProxyTopologyInjector cache sync race condition that caused injection failures, ensuring reliable topology injection during concurrent operations.
- Fixed validation for gRPC routes with extension reference filters, ensuring proper validation and processing of gRPC routes with extension integrations.
- Fixed service account token handling in GatewayNamespaceMode to use SDS (Secret Discovery Service) for properly refreshing expired tokens, ensuring continuous service availability.
- Fixed handling of regex meta characters in prefix match replace for URL rewrite, ensuring special characters are correctly processed during URL transformations.
- Disabled the default emission of `x-envoy-ratelimited` headers from the rate limit filter to reduce header bloat. Re-enable with the `enableEnvoyHeaders` setting in ClientTrafficPolicy if needed.
- Fixed a nil pointer panic in the XDS translator when building API key authentication filter configurations with `sanitize` enabled and no `forwardClientIDHeader` set, improving stability and error handling.
- Truncated Gateway API status condition messages to stay within Kubernetes limits and prevent update failures, ensuring reliable status updates for large message payloads.
- Fixed an issue in EnvoyPatchPolicy where it didn't match the target Gateway or GatewayClass due to an incorrect name reference, ensuring proper policy application.
- Fixed certificate SAN (Subject Alternative Name) overlap detection in gateway listeners, improving TLS certificate validation and error reporting.
- Fixed description and translation behavior for PreserveXRequestID configuration, ensuring consistent request ID preservation across HTTP requests.
- Fixed race condition in proxy context map used in host mode, preventing concurrent access issues and ensuring reliable proxy context management.
- Fixed Listener port limit typo 65353 -> 65535.
- Fixed issue where reloading invalid envoy gateway configuration.
- Fixed missing JWT provider configuration when JWT authentication is configured on multiple HTTP listeners sharing the same port.
- Fixed issue where header modifier doesn't permit multiple values with commas.

## Diagnostics

```bash
kubectl -n <eg-ns> get deploy envoy-gateway \
  -o jsonpath='{.spec.template.spec.containers[0].image}{"\n"}'
```

Anything below `v1.6.7` carries the remainder of this list. Before assuming a novel bug, search this
page for the symptom — "service not found" for an existing Service, stale routing after a proxy
reconnect, 500 on a route with one bad backend and an unexplained controller panic are all known and
fixed.

## Known Issues

**Upgrading inside the 1.6 line is the cheap move**, but it is not free: 1.6.4 changes the Gateway
API CRDs, and 1.6.6 turns previously-silent filter mistakes into 500 responses and rejected routes.
Both are recorded above; check your `HTTPRoute`/`GRPCRoute` filters — especially any combination of
`RequestMirror` with `DirectResponse` or `RequestRedirect` — before rolling it out.

**Ordering:** apply the Gateway API CRDs first, then the controller, then confirm the proxy
Deployments actually rolled — the data-plane image ships with the release but old proxy pods keep
running until restarted.

Security exposure for the same versions is tracked separately in
[[TROUBLE-ENVOY_GATEWAY_KNOWN_CVES]].

## References

- Upstream `release-notes/v1.6.1.yaml` … `v1.6.7.yaml` (`breaking changes`, `security updates`,
  `bug fixes` sections), read at `origin/main` on 2026-07-31.
- Breaking CRD change of 1.6.4: kubernetes-sigs/gateway-api issue #4490.
- CVEs: [[TROUBLE-ENVOY_GATEWAY_KNOWN_CVES]]; add-on: [[CONCEPT-ADDON_ENVOY_GATEWAY]].

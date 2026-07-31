---
id: TROUBLE-ENVOY_GATEWAY_1_5_KNOWN_ISSUES
type: troubleshooting
title: "Envoy Gateway 1.5: every defect fixed in the 1.5 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.5.0 <1.6.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - envoy gateway 1.5 known issues
  - envoy gateway 1.5 bugs
  - envoy gateway 1.5 fixed in
tags:
  - troubleshooting
  - envoy
  - gateway-api
  - upgrade
sources:
  - type: code
    path: envoyproxy/gateway release-notes/v1.5.*.yaml — "bug fixes" sections
    url: https://github.com/envoyproxy/gateway/tree/main/release-notes
    note: "10 releases on this line, 66 declared fixes"
relations:
  - type: see_also
    target: TROUBLE-ENVOY_GATEWAY_KNOWN_CVES
  - type: see_also
    target: TROUBLE-ENVOY_GATEWAY_BREAKING_CHANGES
  - type: see_also
    target: CONCEPT-ADDON_ENVOY_GATEWAY
---

# Envoy Gateway 1.5: every defect fixed in the 1.5 line

## Summary

The **1.5** maintenance line published **10 releases** carrying **66 defect fixes**,
5 breaking changes and 13 security updates (CVE-2025-64527, CVE-2025-64763, CVE-2025-66220, CVE-2026-22771).
Running anything below **1.5.9** on this line means carrying the remainder of the list
below.

Use this page the way a defect database is used: before filing "Envoy Gateway does X wrong", search
here — the odds are it is already named, with the exact patch that fixes it.

## Problem

Defects are grouped by the release that fixed them; a cluster on version *N* carries everything
listed under versions greater than *N*.

## Context

### v1.5.0 — 19

- Fixed issue where WASM cache init failure caused routes with WASM-less EnvoyExtensionPolicies to have 500 direct responses.
- Fixed issue which UDP listeners were not created in the Envoy proxy config when Gateway was created.
- Keep ALPN configuration for listeners with overlapping certificates when ALPN is explicitly set in ClientTrafficPolicy.
- Fixed issue that switch on wrong SubjectAltNameType enum value in BackendTLSPolicy.
- Fixed issue that BackendTLSPolicy should not reference ConfigMap or Secret across namespace.
- Fixed bug in certificate SANs overlap detection in listeners.
- Fixed issue where EnvoyExtensionPolicy ExtProc body processing mode is set to FullDuplexStreamed, but trailers were not sent.
- Fixed validation issue where EnvoyExtensionPolicy ExtProc failOpen is true, and body processing mode FullDuplexStreamed is not rejected.
- Add ConfigMap indexers for EnvoyExtensionPolicies to reconcile Lua changes
- Fixed issue that default accesslog format not working.
- Fixed validation errors when the rateLimit url for Redis in the EnvoyGateway API includes multiple comma separated hosts.
- Fixes addresses in status of DualStack NodePort Gateways.
- Fixed issue that not able to override the prometheus annotation in EnvoyProxy CRD.
- Skipped ExtProc, Wasm, and ExtAuth when they are configured FailOpen and the configuration is invalid, e.g. missing backendRefs or invalid port.
- Fixed issue that failed to update policy status when there are more than 16 ancestors.
- Fixed race condition in watchable.Map Snapshot subscription.
- Fixed issue where HTTPRoutes with sessionPersistence caused the Envoy listeners to drain.
- Fixed deployment creation blocking when EnvoyProxy secret is missing.
- Increased earlyRequestHeaders limit from 16 to 64.

### v1.5.1 — 7

- Fixed cluster stat name generation to use lowercase names.
- Resolved nil pointer dereference in configmap indexer.
- Corrected log formatting to avoid DPANIC errors.
- Improved context error handling throughout the codebase.
- Fixed issues with topology injector and local cluster configuration.
- Updated HTTP status code validation maximum from 600 to 599.
- Enhanced proxy protocol filter placement as first listener filter.

### v1.5.2 — 6

- Fixed service account token handling in GatewayNamespaceMode to use SDS for properly refreshing expired token.
- Fixed preserve route parent status for multi-parent routes.
- Fixed weighted cluster generation in RouteAction when URLRewrite filter is applied.
- Fixed handling of regex meta characters in prefix match replace for URL rewrite.
- Disabled the default emission of `x-envoy-ratelimited` headers from the rate limit filter; re-enable with the `enableEnvoyHeaders` setting in ClientTrafficPolicy.
- Fixed race condition when accessing `mergeGateways` set.

### v1.5.3 — 3

- Fixed a nil pointer panic in the XDS translator when building API key authentication filter configurations with `sanitize` enabled and no `forwardClientIDHeader` set.
- Truncated Gateway API status condition messages to stay within Kubernetes limits and prevent update failures.
- Fixed an issue in EnvoyPatchPolicy where it didn't match the target Gateway/GatewayClass due to an incorrect name reference.

### v1.5.5 — 8

- Fixed 500 errors caused by partially invalid BackendRefs; traffic is now correctly routed between valid backends and 500 responses according to their configured weights.
- Fixed certificate SAN overlap detection in gateway listeners.
- Fixed panic with request mirror with GRPCRoute.
- Fixed listener port limit typo 65353 -> 65535.
- Fixed validating EnvoyGateway configuration during a config update.
- Fixed missing JWT provider configuration when JWT authentication is configured on multiple HTTP listeners sharing the same port.
- Fixed IP family not set in UDPListener.
- Fixed issue where didn't watch change for the ca cert in the Backend.

### v1.5.6 — 6

- Fixed xDS snapshot cache to clear snapshots when streams close, preventing proxies from receiving stale configuration after reconnection.
- Fixed configured OIDC authorization endpoint being overridden by discovered endpoints from issuer's well-known URL.
- Fixed an issue with gateway ownership tracking when running multiple controllers.
- Fixed default namespace handling when namespace is unset.
- Fixed a bug where HTTPRoutes referencing gateways with multiple different GatewayClasses would have incomplete status conditions.
- Fixed gateway status to treat too many addresses as programmed.

### v1.5.7 — 5

- Fixed an issue where observedGeneration is missing from the EnvoyPatchPolicy status.
- Fixed ExternalTrafficPolicy not being applied to Envoy Service when ServiceType is NodePort.
- Fixed an issue where BackendTrafficPolicy does not validate maximum value of requestBuffer limit.
- Fixed an issue where port forward not working on OpenTelemetry collector pods.
- Fixed a potential goroutine leak when config reloads.

### v1.5.8 — 6

- Fixed an issue where unrecoverable discovery errors on checking optional CRDs caused the EG pod to reconcile incomplete resources.
- Fixed an issue where ExtProc is discarded when failOpen is enabled for Wasm.
- Fixed an issue where sensitive data was exposed in control plane config dump.
- Fixed a server run race condition that could cause goroutine leaks during config reloading.
- Fixed an issue where wrong cluster type was used with mixed FQDN backend and service backend refs.
- Fixed an issue where routes with match-all rules were incorrectly merged with specific match rules.

### v1.5.9 — 6

- Fixes an issue where shutdown manager didn't ignore ready and stats listener metrics in connection calculation.
- Fixed an issue where shutdown manager incorrectly counted ready and stats listener connections, preventing timely shutdown.
- Fixed an issue where custom response filters were not properly positioned in the filter chain, causing redirect functionality to fail in OAuth2 flows.
- Fixed an issue where route-level idle timeout prevented users from configuring listener-level idle timeout.
- Fixed an issue where the message package did not adopt the configured logging level.
- Fixed an issue where the controller reported ready before cache synced.

## Diagnostics

```bash
kubectl -n <eg-ns> get deploy envoy-gateway \
  -o jsonpath='{.spec.template.spec.containers[0].image}{"\n"}'
```

Compare against **1.5.9** — the newest release of this line.

## Known Issues

Upgrading inside a maintenance line is the low-risk move, but this project ships behaviour changes
in patch releases as well; the full list is in [[TROUBLE-ENVOY_GATEWAY_BREAKING_CHANGES]] and the
security exposure in [[TROUBLE-ENVOY_GATEWAY_KNOWN_CVES]].

## References

- Upstream `release-notes/v1.5.*.yaml`, `bug fixes` sections, read at `origin/main` on 2026-07-31.
- Add-on: [[CONCEPT-ADDON_ENVOY_GATEWAY]].
